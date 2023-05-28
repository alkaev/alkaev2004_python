import types
import dis
import typing as tp


def count_operations(source_code: types.CodeType) -> dict[str, int]:
    """Count byte code operations in given source code.

    :param source_code: the bytecode operation names to be extracted from
    :return: operation counts
    """
    ans = {}
    line_code = [source_code]
    while True:
        if len(line_code) == 0:
            return ans
        for instruction in dis.get_instructions(line_code.pop(-1)):
            if instruction.opname in ans:
                ans[instruction.opname] += 1
            else:
                ans[instruction.opname] = 1

            if isinstance(instruction.argval, types.CodeType):
                line_code = [instruction.argval] + line_code

