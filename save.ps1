param(
    [Parameter(Mandatory=$true)]
    [string]$filename
)

$saveFilename = "signals\" + $filename + ".json"
Copy-Item -Path "hex2bin_outputs.json" -Destination $saveFilename