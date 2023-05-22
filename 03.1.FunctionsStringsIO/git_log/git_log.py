import typing as tp


def reformat_git_log(inp: tp.IO[str], out: tp.IO[str]) -> None:
    """Reads git log from `inp` stream, reformats it and prints to `out` stream

    Expected input format: `<sha-1>\t<date>\t<author>\t<email>\t<message>`
    Output format: `<first 7 symbols of sha-1>.....<message>`
    """
    for lines in inp.readlines():
        line = lines.split('\t')
        empty = 80 - len(line[0][:7]) - len(line[-1]) + 1
        result = line[0][:7] + '.' * empty + line[-1]
        print(result)
        out.write(result)
    return
