Tool to simulate digital signals on an oscilloscope.

## Usage: 

Open a powershell terminal in the repo root, and execute ```.\run``` to display the scope simulation. The file name in the ```run.ps1``` script will be displayed.

If you want to save a signal, modify it in ```add_signal.py```, change the file name (if necessary) in ```add.ps1```, and run ```.\add```.

The channels are stored in the json file and the python script (which is run by ```run.ps1```) reads the json file provided as an argument in the powershell script and displays it.

Keys in the json file do not matter. Spaces in the strings also do not matter.

Adding new signals can be automated using the ```add_signal.py``` script.