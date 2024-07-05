param(
    [Parameter(Mandatory=$true)]
    [string]$filename
)

# If you want to change the name of the virtual environment, do it here.
$venv_name = ".venv"

$venv_python = Join-Path -Path $venv_name -ChildPath "Scripts\python.exe"

$fullFileName = "signals\" + $filename + ".yml"
& $venv_python -m "scripts.scope" $fullFileName
