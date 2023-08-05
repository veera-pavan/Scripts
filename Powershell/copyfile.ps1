$remotePath = "\\<remoteservername>\<sharedfoldername>$\<Targetdirectory>\package.sha256.sha256"
$localPath = "C:\package\package.sha256.sha256"

Copy-Item -Path $remotePath -Destination $localPath -Force