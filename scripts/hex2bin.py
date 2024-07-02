# Utility to convert a hex string to a binary string.
# Converts all the strings in hex2bin_inputs.yml
# Saves them in hex2bin_outputs.yml

import yaml

def convert_hex2bin(hex_str):

    hex_str = "".join(hex_str.split())
    if not all(char in "0123456789abcdefABCDEF" for char in hex_str):
        raise ValueError("Input string is not a valid hexadecimal number.")

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
        raise RuntimeError("No input file found. Create a file called hex2bin_inputs.yml in the repository root.")

    bin_strings = {}
    for input in hex_strings:
        bin_strings[input] = convert_hex2bin(hex_strings[input])

    with open("outputs_hex2bin.yml", "w", encoding="utf-8") as file:
        yaml.dump(bin_strings, file, default_flow_style=False)
    
    for key, val in bin_strings.items():
        print(f"{key} : {val}")