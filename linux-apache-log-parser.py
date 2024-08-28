# 8.2.1
# Linux Apache Log Parser in Python

import re
import os.path

centos_apache_log_file_path = "/var/log/httpd/access_log"
ubuntu_apache_log_file_path = "/var/log/apache2/access.log"

httpd_log_path = [centos_apache_log_file_path, ubuntu_apache_log_file_path]

regex = '([(\d\.)]+) - - \[(.*?)\] \"(.*?)\" (\d+) (\d+) \"(.*?)\" \"(.*?)\"'

for log_file in httpd_log_path:
    if os.path.isfile(log_file) :
        with open(log_file, "r") as file:
            for line in file:
                for match in re.finditer(regex, line, re.S):
                    log_line = (re.match(regex, line)).groups()
                    print(log_line)