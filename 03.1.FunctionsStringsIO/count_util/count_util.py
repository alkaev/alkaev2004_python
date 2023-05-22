import typing as tp
import io
import re


def count_util(text: str, flags: tp.Optional[str] = None) -> dict[str, int]:
    """
    :param text: text to count entities
    :param flags: flags in command-like format - can be:
        * -m stands for counting characters
        * -l stands for counting lines
        * -L stands for getting length of the longest line
        * -w stands for counting words
    More than one flag can be passed at the same time, for example:
        * "-l -m"
        * "-lLw"
    Ommiting flags or passing empty string is equivalent to "-mlLw"
    :return: mapping from string keys to corresponding counter, where
    keys are selected according to the received flags:
        * "chars" - amount of characters
        * "lines" - amount of lines
        * "longest_line" - the longest line length
        * "words" - amount of words
    """
    if flags is None:
        flags = ''
    flags_list = re.findall(r'\w', flags)
    counters = {'w': 'words', 'm': 'chars', 'l': 'lines', 'L': 'longest_line'}
    for flag in flags_list:
        counters.pop(flag)
    text_stream = io.StringIO(text)
    info = {'chars': 0, 'words': 0, 'lines': 0, 'longest_line': 0}
    for line in text_stream.readlines():
        info['words'] += len(line.split())
        info['lines'] += 1
        info['chars'] += len(line)
        if len(line) > info['longest_line']:
            info['longest_line'] = len(line) - 1
    if flags_list:
        for counter in counters.values():
            info.pop(counter)
    return info



