
import paramiko
from scp import SCPClient
import os

from ___mdms import backupfiles
files = backupfiles()

'''
文件服务器下载文件到本地  ./download/ 文件夹下面
'''

# 定义函数 建立 ssh链接
def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client
 
# 导入服务器信息
from  ___mdms import get_server
qty_of_server = 1
servers = [get_server(i) for i in range(0,qty_of_server)] 


# 上传文件到静态站
ssh = createSSHClient(servers[0][0], 22, servers[0][1], servers[0][2])
scp = SCPClient(ssh.get_transport())  

if not os.path.isdir('./download/'):
    os.makedirs('./download/')

for index,file in enumerate(files):

    scp.get('/root/myroot/python/' + file,'./download/')
    print(index+1, "  成功从{1}下载 {0} 文件".format(file,servers[0][0]))



