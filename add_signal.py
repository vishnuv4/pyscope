# Use this script to automate the creation of the json file 
# Remember to change the filename after each modification, if you do not want to overwrite the previously saved signal.

import json
import argparse

parser = argparse.ArgumentParser(description='Signals')
parser.add_argument('file', type=str, help="Name of the signal file")

args = parser.parse_args()
filename = args.file

signals = {}
signals["ch0"] = " 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000"
signals["ch1"] = " 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(signals, file, indent=4, sort_keys=True)