# This is the json file containing the signal you want to display on different channels
param(
    [Parameter(Mandatory=$true)]
    [string]$filename
)

$fullFileName = "signals\" + $filename + ".json"
.venv\Scripts\python.exe -m "scripts.scope" $fullFileName
