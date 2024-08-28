# 8.2.1
# Linux SSH Log Parser in Python

import re
import os.path

centOS_ssh_log_file_path = "/var/log/secure"
ubuntu_shh_log_file_path = "/var/log/auth.log"

log_path = [centOS_ssh_log_file_path, ubuntu_shh_log_file_path]

regex_pattern = 'sshd\[.*\]'

for log_file in log_path:
    if os.path.isfile(log_file) :
        with open(log_file, "r") as file:
            for line in file:
                for match in re.finditer(regex_pattern, line, re.S):
                    print(line,end = '')