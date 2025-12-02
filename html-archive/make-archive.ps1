# Make a zip archive of the current folder's contents as ../html-archive.zip
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Push-Location $scriptDir
$dest = Join-Path (Resolve-Path ..).Path "html-archive.zip"
if (Test-Path $dest) { Remove-Item $dest -Force }
Compress-Archive -Path * -DestinationPath $dest -Force
Pop-Location
Write-Host "Created archive: $dest"