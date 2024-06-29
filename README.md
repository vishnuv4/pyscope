## Description

Tool to simulate digital signals on an oscilloscope. Runs on Windows.

## Usage

The tool is intended to be used with a Powershell CLI set to the repository root.

Each set of channels is stored as a string of 1s and 0s in a json file. All signals are saved in the ```signals\``` directory.

To display the channels for a signal, open a powershell terminal in the repo root, and execute ```.\run <filename>```. Do not add the ".json" extension.

To save a set of channels, modify the strings in ```scripts\add_signal.py```  and execute ```.\add <filename>``` to save it as a new signal/json file. Do not add the ".json" extension.

The keys in the json file must be one out of ```ch0```, ```ch1```, ```ch2```, or ```ch3```. No more than 4 channels are supported. The order of channels in the json file does not matter.

Whitespace in the strings also do not matter, so we can group the channel strings of 1s and 0s however it's convenient.

There is also a utility that can be used to convert hexadecimal strings to a binary strings. List the strings you want to convert in json format in ```hex2bin_inputs.json``` in the repository root and run ```.\convert``` in the terminal. The corresponding binary strings will be saved in ```hex2bin_outputs.json```.