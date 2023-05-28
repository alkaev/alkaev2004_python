import math
import sys
from typing import Any, Dict, Optional
PROMPT = '>>> '


def run_calc(context: Optional[Dict[str, Any]] = None) -> None:
    """Run interactive calculator session in specified namespace"""

    while True:
        sys.stdout.write(PROMPT)
        string = sys.stdin.readline()
        if string == "":
            break
        sys.stdout.write(str(eval(string, {"__builtins__": {}}, context)) + "\n")
    sys.stdout.write("\n")


if __name__ == '__main__':
    context = {'math': math}
    run_calc(context)
