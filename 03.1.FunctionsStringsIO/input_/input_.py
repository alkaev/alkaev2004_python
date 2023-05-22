import sys
import typing as tp


def input_(prompt: tp.Optional[str] = None,
           inp: tp.Any = None,
           out: tp.Any = None) -> tp.Optional[str]:
    """Read a string from `inp` stream. The trailing newline is stripped.

    The `prompt` string, if given, is printed to `out` stream without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), return None.

    `inp` and `out` arguments are optional and should default to `sys.stdin`
    and `sys.stdout` respectively.
    """
    if out:
        sys.stdout = out
    if prompt:
        sys.stdout.write(prompt)
        sys.stdout.flush()
    if inp:
        sys.stdin = inp
    result: tp.Any = sys.stdin.read().rstrip('\n')
    if result:
        return result
    else:
        return None
