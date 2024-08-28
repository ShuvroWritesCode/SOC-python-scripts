# 8.2.1
# CentOS Apache Log Parser in Python

import re
import os.path

centos_httpd_log_file_path = "/var/log/httpd/access_log"

regex = '([(\d\.)]+) - - \[(.*?)\] \"(.*?)\" (\d+) (\d+) \"(.*?)\" \"(.*?)\"'

if os.path.isfile(centos_httpd_log_file_path):
    with open(centos_httpd_log_file_path, "r") as file :
        for line in file :
            for match in re.finditer(regex, line, re.S):
                    log_line = (re.match(regex, line)).groups()
                    print(log_line)

