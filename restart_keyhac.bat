@echo off

taskkill /IM keyhac.exe /F
timeout /T 0.5 /NOBREAK >nul

start "" "%~dp0keyhac.exe"