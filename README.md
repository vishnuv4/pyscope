## Description

Tool to simulate signals on an oscilloscope. Runs on Windows.

## Requirements

Python 3.12 

It must be accessible by powershell - run ```python --version``` in a powershell window to confirm. Not tested with versions below 3.12, but it may work.

## Setup

Run these commands in a Powershell CLI in the repo root:

```
python -m venv .venv; .venv\Scripts\python.exe -m pip install -r requirements.txt
```

Note: Avoid changing the name of the virtual environment. If you must, then update the name in the .ps1 scripts (analog, conv, run, save) in the repo root. And the .gitignore as well.

## Usage

The tool is intended to be used with a Powershell CLI set to the repository root.
Each digital signal (a collection of channels) must be stored as a yml file of bitstrings in the ```signals\``` folder. The analog signals must be provided within the python script itself, details mentioned below.

There are 4 CLI commands:
- ```.\run [filename]```
    - Displays the digital signal with the specified name in ```signals\```
- ```.\conv```
    - Converts the hex strings in ```hex2bin_inputs.yml``` and saves it in ```hex2bin_outputs.yml```
- ```.\save [filename]```
    - Saves the contents of ```hex2bin_outputs.yml``` to a file with the specified name in the ```signals\``` folder.
- ```.\analog```
    - Runs the analog scope. The signal to be modified is within ```generate_signal()``` function of the ```scripts\analog_scope.py``` file.

For the commands requiring a filename, do not add the ```.yml``` file extension - the script will do that.

The keys in the yml files within ```signals\``` must be one out of ```ch0```, ```ch1```, ```ch2```, or ```ch3```. No more than 4 channels are supported. The order of channels in the yml file does not matter.

Whitespace in the strings also do not matter, so we can group the channel strings of 1s and 0s however it's convenient. This applies to both the yml files in the ```signals``` folder and the hex2bin input file.