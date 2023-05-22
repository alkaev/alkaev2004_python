import subprocess
import typing as tp
from pathlib import Path


def get_changed_dirs(git_path: Path, from_commit_hash: str, to_commit_hash: str) -> tp.Set[Path]:
    """
    Get directories which content was changed between two specified commits
    :param git_path: path to git repo directory
    :param from_commit_hash: hash of commit to do diff from
    :param to_commit_hash: hash of commit to do diff to
    :return: sequence of changed directories between specified commits
    """
    result = subprocess.run(
        ['git', '-C', str(git_path), 'diff', '--name-only', '--diff-filter=d', from_commit_hash, to_commit_hash],
        capture_output=True,
        text=True
    )
    changed_files = result.stdout.splitlines()
    changed_dirs = set()

    for file in changed_files:
        file_path = git_path / file
        changed_dirs.add(file_path.parent)

    return changed_dirs