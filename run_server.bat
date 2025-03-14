@echo off

start cmd
call .\venv\Scripts\activate
call python run.py server

@pause