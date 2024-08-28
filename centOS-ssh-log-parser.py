# 8.2.1
# centOS SSH Log Parser in Python

import re
import os.path

centOS_log_file_path = "/var/log/secure"

regex_pattern = 'sshd\[.*\]'

if os.path.isfile(centOS_log_file_path) :
    with open(centOS_log_file_path, "r") as file:
        for line in file:
            for match in re.finditer(regex_pattern, line, re.S):
                print(line,end = '')