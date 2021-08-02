import sys
import os 
from cx_Freeze import executable, setup, Executable

files = ['main.ico']

target = Executable(
    script="app.py",
    base = "WIN32GUI",
    icon="main.ico"
)


setup(
    name='MCORD GUI',
    version="0.5",
    description = 'GUI for AFE Hubs',
    author = "MK",
    options = {'build.exe': {'include_files':files}},
    executables = [target]
)