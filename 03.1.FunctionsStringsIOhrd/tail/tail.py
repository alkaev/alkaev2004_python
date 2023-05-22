import typing as tp
from pathlib import Path
import sys


def tail(filename: Path, lines_amount: int = 10, output: tp.Any = None) -> None:
    """
    :param filename: file to read lines from (the file can be very large)
    :param lines_amount: number of lines to read
    :param output: stream to write requested amount of last lines from file
                   (if nothing specified stdout will be used)
    """
    file_size = filename.stat().st_size
    file = open(filename, 'r')

    chunks = []
    chunks_size = file_size // 512
    lines_counter = 0
    for chunk_id in range(chunks_size + 1):
        chunks.append(file.read(512))
    needs_chunks = 0
    if file_size > 0:
        while chunks[-1] == '\n' or chunks[-1] == '':
            chunks.pop(-1)
        chunks[-1] = chunks[-1].rstrip('\n')
    while lines_counter < lines_amount and needs_chunks < len(chunks):
        lines_counter += chunks[len(chunks) - needs_chunks - 1].count('\n')
        needs_chunks += 1
    if lines_counter < lines_amount:
        if output:
            file.seek(0)
            output.write(bytes(file.read(), 'utf-8'))
        else:
            print(''.join(chunks[len(chunks) - needs_chunks::]))
    else:
        pre_ans_lines = ''.join(chunks[len(chunks) - needs_chunks::]).split('\n')
        if output:
            output.write(bytes('\n'.join(pre_ans_lines[len(pre_ans_lines) - lines_amount:]), 'utf-8'))
        else:
            print('\n'.join(pre_ans_lines[len(pre_ans_lines) - lines_amount:]))

