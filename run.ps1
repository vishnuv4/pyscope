# This is the json file containing the signal you want to display on different channels
$filename = "signals"

$fullFileName = $filename + ".json"
.venv\Scripts\python.exe -m scope $fullFileName
