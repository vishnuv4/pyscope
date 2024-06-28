# This is the json file containing the signal you want to save
param(
    $filename
)

$fullFileName = $filename + ".json"
.venv\Scripts\python.exe -m add_signal $fullFileName