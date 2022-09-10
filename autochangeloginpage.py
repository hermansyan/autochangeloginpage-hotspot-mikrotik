import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='192.168.250.1',port=22,username='realfood',password='reallife')

print('===================MIKROTIK CONNECTED==========================')

command     ="/ip hotspot profile set "
profile1    ="OFFICE"
profile2    ="PLAN WAREHOUSE"
directory   =" html-directory=hotspot_realfood_temp"
version     = ['V1','V2','V3','V4']

for i in range(1000):
    for count,ver in enumerate(version):
        ssh.exec_command(command+profile1+directory+ver)
        ssh.exec_command(command+profile2+directory+ver)
        print('*************************')
        print('--> Login Page'+ver)
        print('--> Day ',j)
        print('*************************')
        time.sleep(20)

ssh.close()