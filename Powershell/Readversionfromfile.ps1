$dynamicPart = Get-ChildItem "C:\filepath" | Where-Object { $_.Name -like "filename*.prn" } | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($dynamicPart) {
$value = Get-Content $dynamicPart.FullName | Select-String -Pattern "version2.0" | ForEach-Object { $_.Matches.Value }
if ($value) {
$uniqueValue = $value | Select-Object -Unique
$outputFile = "C:\Version.txt"

New-Item -Path $outputFile -ItemType File -Force
Set-Content -Path $outputFile -Value $uniqueValue

Write-Host $uniqueValue

# Move "output.txt" to Jenkins agent
$jenkinsAgentPath = "\\Jenkinsagentvmname\C$\specificfoldername"
copy-Item -Path $outputFile -Destination "$jenkinsAgentPath\Version.txt"

# Delete the file from the Windows VM
Remove-Item -Path $outputFile
} else {
Write-Host "Error: Value 'version2.0' not found in the .prn file."
}
} else {
Write-Host "Error: No matching .prn files found."
}