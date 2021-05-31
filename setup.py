import sys
import os
from cx_Freeze import setup, Executable

files = ['icon.ico','icons/']

target = Executable(
    script="main.py",
    base="Win32GUI",
)

setup(
    name="Psutil Manager",
    version="1.0.0",
    description="Psutil to monitor system",
    options= { 'build_exe':{'include_files':files}},
    executables = [target]
)
