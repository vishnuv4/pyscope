## Description

Tool to simulate digital signals on an oscilloscope. Runs on Windows.

## Usage

Each set of channels is stored as a string of 1s and 0s in a json file. The project can support multiple json files for different signals, saved in the "signals" directory of the repo.

To display the channels for a signal, open a powershell terminal in the repo root, and execute ```.\run <filename>```. Do not add the ".json" extension.

To save a set of channels, modify the strings in add_signal.py  and run ```.\add <filename>``` to save it as a new signal/json file. Do not add the ".json" extension.

The keys in the json object do not matter as long as they are distinct. Whitespace in the strings also do not matter, so we can group the channel strings of 1s and 0s however it's convenient.
