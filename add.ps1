# This is the json file containing the signal you want to save
param(
    [Parameter(Mandatory=$true)]
    [string]$filename
)

$fullFileName = "signals\" + $filename + ".json"
.venv\Scripts\python.exe -m "scripts.add_signal" $fullFileName
