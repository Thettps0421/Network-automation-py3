## https://github.com/ktbyers/netmiko
## recommendation using on Windows machine work well more than linux

# 1 Install lastest version of Python
# 2 Install Anaconda (https://www.anaconda.com/download/)
# 3 From Anaconda Shell, run "conda install paramiko"
# 4 From Anaconda Shell, run "pip  install scp"
# 5 Now install the Git for Windows (https://www.git-scm.com/downloads)
# 6 From Git Bash window, Clone Netmiko using the following command
# 7 Once the installation is completed, change the directory to Netmiko "using cd netmiko" command.
# 8 Execute "python setup.py install" from Git Bash Window. Once the instllation is completed, go to your Windows Command prompt or Anaconda shell and check Netmiko from Python Interprerter shell.
# 9 Finally "import paramiko" and "import netmiko", and start using it for python coding.

import paramiko
import netmiko


print("Netmiko introduction")
print("let's use Windows machines for better experience")
