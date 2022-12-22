
import paramiko
from scp import SCPClient
from ___mdms import backupfiles


files = backupfiles()

# 定义函数 建立 ssh链接
def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client
 

from  ___mdms import get_host,get_server
qty_of_server = 1
servers = [get_server(i) for i in range(0,qty_of_server)] 

# 上传文件到静态站
ssh = createSSHClient(servers[0][0], 22, servers[0][1], servers[0][2])
scp = SCPClient(ssh.get_transport())  

for index,file in enumerate(files):

    scp.put(file, '/root/myroot/python/')
    print(index+1, "  成功上传 {0} 文件到{1}".format(file, servers[0][0]))



