@echo off

REM below for loop is used to pickup latest created file name and store in a variable %LAST%
cd "<target directory path>"
for /f %%i in ('dir /b/ad/od/t:w') do set LAST=%%i
echo The most recently created folder is %LAST%
cd %LAST%

REM below command is used to rename the existing file
REN testfile testfileupdated.txt

REM below commands is used to copy files from local to remote VM

net use \\<remoteservername>\C$ /user:Domain_Name\Domain_User Domainpwd
robocopy /sec /s /e /j /Z /NOOFFLOAD /W:10 /MT:16 "%cd%" \\<remoteservername>\C$\targefolder /xd "<providefoldernamewhichareneededtoexcludefromcopying>"
IF %ERRORLEVEL% EQU 1 exit /B 0


REM batch script is used to download artifacts from nexus

@echo off

setlocal

set packageUrl=<artifacturl>
set destinationPath=<directorypath>
set token=<usertoken>
set passcode=<pwdtoken>

curl -o "%destinationPath%" -H "Authorization: Bearer %token% %passcode%" "%packageUrl%"

if %errorlevel% equ 0 (
    echo Package downloaded successfully.
) else (
    echo Failed to download package.
)

endlocal

