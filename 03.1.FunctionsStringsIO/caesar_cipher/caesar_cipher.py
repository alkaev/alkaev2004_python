def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """
    symbolH = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
                     12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
                     23: 'X', 24: 'Y', 25: 'Z'}
    symbolL = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
                    12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w',
                    23: 'x', 24: 'y', 25: 'z'}

    high = {}
    for key1 in symbolH:
        value1 = symbolH[key1]
        high[value1] = (key1 + n) % 26
    low = {}
    for key1 in symbolL:
        value1 = symbolL[key1]
        low[value1] = (key1 + n) % 26

    cstr = ""

    for symbol in message:
        if (symbol not in low) and (symbol not in high):
            cstr += symbol
        elif symbol.islower():
            new_num_of_symbol = low[symbol]
            cstr += symbolL[new_num_of_symbol]
        else:
            new_num_of_symbol = high[symbol]
            cstr += symbolH[new_num_of_symbol]

    return cstr
