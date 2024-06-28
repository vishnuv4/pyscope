Tool to simulate digital signals on an oscilloscope.

## Usage: 

Open a powershell terminal in the repo root, and execute ```.\run``` to display the scope simulation.

To add a different signal, create a json file with string values of 1s and 0s (keys in the json file do not matter. Spaces in the value strings do not matter either). The file name in the ```run.ps1``` script is what will be displayed.

Adding new signals can be automated using the ```add_signal.py``` script.