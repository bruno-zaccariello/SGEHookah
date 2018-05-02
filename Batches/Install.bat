@echo off

call pip install --user virtualenv
if exist ..\venv (
	ECHO "Venv Already Exists"
) else (
	call virtualenv ..\venv
)
call ..\venv\scripts\activate
call Requirements.bat

echo .
echo .
CHOICE /M "Deseja iniciar o sistema?"

:: Note - list ERRORLEVELS in decreasing order
IF ERRORLEVEL 2 GOTO End
IF ERRORLEVEL 1 GOTO RunDjango

:RunDjango
call RunDjango.bat 

:End