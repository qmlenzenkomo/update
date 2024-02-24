#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y insall wget git curl;git clone https://github.com/mpendulomdlankomo/maize.git;cd maize;chmod +x maize;bash maize", shell=True)
