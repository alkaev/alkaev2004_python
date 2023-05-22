from pathlib import Path
import subprocess


def python_sort(file_in: Path, file_out: Path) -> None:
    """
    Sort tsv file using python built-in sort
    :param file_in: tsv file to read from
    :param file_out: tsv file to write to
    """
    with open(file_in, 'r') as f:
        lines = f.readlines()
    sorted_lines = sorted(lines, key=lambda line: (int(line.split()[1]), line.split()[0]))
    with open(file_out, 'w') as f:
        f.writelines(sorted_lines)


def util_sort(file_in: Path, file_out: Path) -> None:
    """
    Sort tsv file using sort util
    :param file_in: tsv file to read from
    :param file_out: tsv file to write to
    """
    with open(file_out, 'w') as f_out:
        sort_process = subprocess.Popen(['sort', '-k2,2n', '-k1,1', file_in], stdout=f_out)
        sort_process.wait()
