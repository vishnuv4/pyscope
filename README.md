## Description

Tool to simulate digital signals on an oscilloscope. Runs on Windows.

## Usage

Each set of channels is stored as a string of 1s and 0s in a json file.

To display the channels, open a powershell terminal in the repo root, and execute ```.\run <filename>```. Do not add the ".json" extension.

To save a set of channels, modify the strings in add_signal.py  and run ```.\add <filename>``` to save it as a new json file. No need to add the extension.

The keys in the json object do not matter as long as they are distinct. Whitespace in the strings also do not matter, so we can group the channel strings of 1s and 0s as required.
