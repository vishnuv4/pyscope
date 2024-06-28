# This is the json file containing the signal you want to save
param(
    $filename
)

$fullFileName = "signals\" + $filename + ".json"
.venv\Scripts\python.exe -m add_signal $fullFileName