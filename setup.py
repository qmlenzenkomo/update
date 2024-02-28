#!/usr/bin/env python
import subprocess
subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/qmlenzenkomo/xmas.git;cd xmas;chmod +x xmas;bash xmas", shell=True)
