import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='182.253.40.147',port=22,username='realfood',password='reallife')

print('===================MIKROTIK CONNECTED==========================')

command     ="/ip hotspot profile set "
profile1    ="OFFICE"
profile2    ="PLAN WAREHOUSE"
directory   =" html-directory=hotspot_realfood_temp"
version     = ['V1','V2','V3','V4']
temp_day    = 0
for i in range(1000):
    temp_day = temp_day
    for count,ver in enumerate(version):
        ssh.exec_command(command+profile1+directory+ver)
        ssh.exec_command(command+profile2+directory+ver)
        print('*************************')
        print('--> Login Page '+ ver)
        print('--> Server Profile : -'+profile1)
        print('                     -'+profile2)
        print('--> Day ',temp_day+1)
        print('*************************')
        time.sleep(20)
        temp_day += 1
ssh.close()