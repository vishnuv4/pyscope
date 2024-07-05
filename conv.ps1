# If you want to change the name of the virtual environment, do it here.
$venv_name = ".venv"

$venv_python = Join-Path -Path $venv_name -ChildPath "Scripts\python.exe"
& $venv_python -m "scripts.hex2bin"