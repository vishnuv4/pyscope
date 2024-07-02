param(
    [Parameter(Mandatory=$true)]
    [string]$filename
)

$saveFilename = "signals\" + $filename + ".yml"
Copy-Item -Path "outputs_hex2bin.yml" -Destination $saveFilename