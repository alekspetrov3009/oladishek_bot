@echo off 

call %~dp0oladishek_bot\venv\Scripts\activate

cd %~dp0oladishek_bot

set TOKEN=5078645740:AAHk5BOmbNY3DGeDh1W6vtZDmlDrMBDZc3U

python oladishek_bot.py

pause