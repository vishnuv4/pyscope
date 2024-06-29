## Description

Tool to simulate digital signals on an oscilloscope. Runs on Windows.

## Usage

The tool is intended to be used with a Powershell CLI set to the repository root.

Each set of channels is stored as a string of 1s and 0s in a json file. All signals are saved in the ```signals\``` directory.

To display the channels for a signal, open a powershell terminal in the repo root, and execute ```.\run <filename>```. Do not add the ".json" extension.

To save a set of channels, modify the strings in ```scripts\add_signal.py```  and execute ```.\add <filename>``` to save it as a new signal/json file. Do not add the ".json" extension.

The keys in the json file must be one out of ```ch0```, ```ch1```, ```ch2```, or ```ch3```. No more than 4 channels are supported. The order of channels in the json file does not matter.

Whitespace in the strings also do not matter, so we can group the channel strings of 1s and 0s however it's convenient.

There is also a utility that can be used to convert a hexadecimal string to a binary string. Change the string at the top of ```scripts\hex2bin.py``` and run ```.\convert``` from the powershell terminal (in the repo root). The corresponding binary string will be printed on the console and will be saved in a file called "hex2bin_output.json" in the repo root.