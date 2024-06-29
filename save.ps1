param(
    [Parameter(Mandatory=$true)]
    [string]$filename
)

$saveFilename = "signals\" + $filename + ".json"
Copy-Item -Path "outputs_hex2bin.json" -Destination $saveFilename