import zlib
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import typing as tp


class BlobType(Enum):
    """Helper class for holding blob type"""
    COMMIT = b'commit'
    TREE = b'tree'
    DATA = b'blob'

    @classmethod
    def from_bytes(cls, type_: bytes) -> 'BlobType':
        for member in cls:
            if member.value == type_:
                return member
        assert False, f'Unknown type {type_.decode("utf-8")}'


@dataclass
class Blob:
    """Any blob holder"""
    type_: BlobType
    content: bytes


@dataclass
class Commit:
    """Commit blob holder"""
    tree_hash: str
    parents: list[str]
    author: str
    committer: str
    message: str


@dataclass
class Tree:
    """Tree blob holder"""
    children: dict[str, Blob]


def read_blob(path: Path) -> Blob:
    """
    Read blob-file, decompress and parse header
    :param path: path to blob-file
    :return: blob-file type and content
    """
    blob_file = open(path, 'rb')
    blob_in_bytes = zlib.decompress(blob_file.read())
    blob_type_and_length, blob_body = blob_in_bytes.split(b'\x00', maxsplit=1)
    blob_type = blob_type_and_length.split(b' ', maxsplit=1)[0]
    blob_file.close()
    return Blob(BlobType(blob_type), blob_body)


def traverse_objects(obj_dir: Path) -> dict[str, Blob]:
    """
    Traverse directory with git objects and load them
    :param obj_dir: path to git "objects" directory
    :return: mapping from hash to blob with every blob found
    """
    blobs_paths_array = []
    blobs_dict_hash_data = dict()

    for file in obj_dir.glob('*/*'):
        blobs_paths_array.append(str(file))
    for blob_path in blobs_paths_array:
        blob_path_split = blob_path.split('/')
        sha_1 = ''.join([blob_path_split[len(blob_path_split) - 2], blob_path_split[len(blob_path_split) - 1]])
        blob_info = read_blob(Path(blob_path))
        blobs_dict_hash_data[sha_1] = blob_info

    return blobs_dict_hash_data


def parse_commit(blob: Blob) -> Commit:
    """
    Parse commit blob
    :param blob: blob with commit type
    :return: parsed commit
    """
    parsed_commit = Commit(tree_hash='', parents=[], author='', committer='', message='')
    blob_name, blob_body = blob.content.split(b'\n\n')
    for line in blob_name.split(b'\n'):
        if not line.isspace():
            identifier = line.split()[0]
            if identifier == b'tree':
                parsed_commit.tree_hash = line.split()[1].decode('utf-8')
            if identifier == b'parent':
                parsed_commit.parents.append(line.split()[1].decode('utf-8'))
            if identifier == b'author':
                parsed_commit.author = line.decode('utf-8')[len("author "):]
            if identifier == b'committer':
                parsed_commit.committer = line.decode('utf-8')[len("committer "):]
    parsed_commit.message = blob_body.decode('utf-8').rstrip('\n')
    return parsed_commit


def parse_tree(blobs: tp.Any, tree_root: Blob, ignore_missing: bool = True) -> Tree:
    """
    Parse tree blob
    :param blobs: all read blobs (by traverse_objects)
    :param tree_root: tree blob to parse
    :param ignore_missing: ignore blobs which were not found in objects directory
    :return: tree contains children blobs (or only part of them found in objects directory)
    NB. Children blobs are not being parsed according to type.
        Also nested tree blobs are not being traversed.
    """
    line_of_blobs_children = tree_root.content.split(b' ')[1:]
    blobs_of_children: tp.Any = []
    tree: tp.Any = Tree(children=dict())
    for blob in line_of_blobs_children:
        blob_name, blob_body = blob.split(b'\x00', maxsplit=1)
        blobs_of_children.append([blob_name.decode('utf-8'), blob_body[:20].hex()])
    for blob in blobs_of_children:
        if blob[1] in list(blobs.keys()):
            tree.children[blob[0]] = blobs[blob[1]]
    return tree


def find_initial_commit(blobs: dict[str, Blob]) -> tp.Any:
    """
    Iterate over blobs and find initial commit (without parents)
    :param blobs: blobs read from objects dir
    :return: initial commit
    """
    for blob in blobs.items():
        if blob[1].type_ == BlobType(b'commit'):
            commit = parse_commit(blob[1])
            if len(commit.parents) == 0:
                return commit


def search_file(blobs: dict[str, Blob], tree_root: Blob, filename: str) -> tp.Any:
    """
    Traverse tree blob (can have nested tree blobs) and find requested file,
    check if file was not found (assertion).
    :param blobs: blobs read from objects dir
    :param tree_root: root blob for traversal
    :param filename: requested file
    :return: requested file blob
    """
    tree = parse_tree(blobs, tree_root)
    while list(tree.children.items()):
        blob = list(tree.children.items())[0]
        if blob[0] == filename:
            return tree.children[blob[0]]
        else:
            if blob[1].type_ != BlobType(b'tree'):
                tree.children.pop(blob[0])
            else:
                tree.children.update(parse_tree(blobs, blob[1]).children)
                tree.children.pop(blob[0])
