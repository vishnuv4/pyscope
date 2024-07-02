# Utility to convert a hex string to a binary string.
# Converts all the strings in hex2bin_inputs.yml
# Saves them in hex2bin_outputs.yml

import yaml
import scripts.error as error

def convert_hex2bin(hex_str):
    """
    Converts a hexadecimal string to binary string
    """

    if not all(char in "0123456789abcdefABCDEF" for char in hex_str):
        error.fatal("Input string is not a valid hexadecimal number")

    # Dictionary to map hexadecimal digits to their 4-bit binary equivalents
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
        'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101',
        'e': '1110', 'f': '1111'
    }

    binary_groups = [hex_to_bin_map[ch] for ch in hex_str]
    binary_output = " ".join(binary_groups)
    return binary_output

if __name__ == "__main__":

    try:
        with open("inputs_hex2bin.yml", "r", encoding="utf-8") as file:
            hex_strings = yaml.safe_load(file)
    except FileNotFoundError:
        error.fatal("No input file found. Create a file called inputs_hex2bin.yml in the repository root.")

    for ch in hex_strings:
        hex_strings[ch] = "".join(hex_strings[ch].split())

    lengths = [len(lst) for lst in hex_strings.values()]
    if not all(length is lengths[0] for length in lengths):
        print("\n")
        error.warning("Signal lengths are not the same")
        for ch,sig in hex_strings.items():
            print(f"{ch} : {len(sig)} characters")

    bin_strings = {}
    for string in hex_strings:
        bin_strings[string] = convert_hex2bin(hex_strings[string])

    with open("outputs_hex2bin.yml", "w", encoding="utf-8") as file:
        yaml.dump(bin_strings, file, default_flow_style=False)
    
    print("\n")
    for key, val in bin_strings.items():
        print(f"{key} : {val}")
    print("\n")