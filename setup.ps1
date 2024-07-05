$venv_name = ".venv"
$venv_python = Join-Path -Path $venv_name -ChildPath "Scripts\python.exe"

if(Test-Path $venv_name){
    Remove-Item -Recurse $venv_name
}
python -m venv $venv_name
& $venv_python -m pip install -r requirements.txt