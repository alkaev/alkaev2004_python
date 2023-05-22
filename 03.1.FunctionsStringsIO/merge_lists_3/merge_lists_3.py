import typing as tp
import re
import heapq


def merge(input_streams: tp.Sequence[tp.IO[bytes]], output_stream: tp.IO[bytes]) -> None:
    """
    Merge input_streams in output_stream
    :param input_streams: list of input streams. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :param output_stream: output stream. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :return: None
    """
    all_numbers = []
    for stream in input_streams:
        stream_numbers = re.findall(r'\d+', bytes.decode(stream.read(), encoding='utf-8'))
        all_numbers.append([int(num) for num in stream_numbers])

    merged_numbers = list(heapq.merge(*all_numbers))

    out_str = ''
    for number in merged_numbers:
        out_str += str(number) + '\n'

    if len(merged_numbers) == 0:
        out_str += '\n'

    output_stream.write(str.encode(out_str, encoding='utf-8'))
    return
