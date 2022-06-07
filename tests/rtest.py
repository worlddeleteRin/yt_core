#!/usr/bin/python
# pyenv exec pytest --show-capture=no -o log_cli=true test_client.py 
import sys
import subprocess

file_name = sys.argv[1]
cmnd = f"pyenv exec pytest --show-capture=no -o log_cli=true {file_name}"

subprocess.run(
    cmnd,
    shell=True
)

