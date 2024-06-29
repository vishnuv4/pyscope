## Description

Tool to simulate digital signals on an oscilloscope. Runs on Windows.

## Usage

The tool is intended to be used with a Powershell CLI set to the repository root.
Each signal (a collection of channels) must be stored as a json file of bitstrings in the ```signals\``` folder.

There are 3 commands:
- ```.\run [filename]```
    - Displays the signal with the specified name in ```signals\```
- ```.\convert```
    - Converts the hex strings in ```hex2bin_inputs.json``` and saves it in ```hex2bin_outputs.json```
- ```.\save [filename]```
    - Saves the contents of ```hex2bin_outputs.json``` to a file with the specified name in the ```signals\``` folder.

For the commands requiring a filename, do not add the ```.json``` file extension - the script will do that.

The keys in the json file must be one out of ```ch0```, ```ch1```, ```ch2```, or ```ch3```. No more than 4 channels are supported. The order of channels in the json file does not matter.

Whitespace in the strings also do not matter, so we can group the channel strings of 1s and 0s however it's convenient.