# This is the json file containing the signal you want to display on different channels
param(
    $filename
)

$fullFileName = "signals\" + $filename + ".json"
.venv\Scripts\python.exe -m scope $fullFileName
