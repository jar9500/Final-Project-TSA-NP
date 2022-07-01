from netmiko import Netmiko
from netmiko import ConnectHandler
import os
from datetime import datetime

today = datetime.today().strftime('%d-%m-%Y-%H:%M:%S')
path = "../Backup Configuration"

csr1kv = {
        "device_type": "cisco_ios",
        "ip": "192.168.56.117",
        "username": 'cisco',
        "password": 'cisco123!',
}
try:
    net_connect = ConnectHandler(**csr1kv)
except NetMikoTimeoutException:
    print ('Connection Time Out, Silahkan Cek Koneksi')
except AuthenticationException:
    print ('Authentication Failed, Silahkan Cek Username/Password')
except SSHException:
    print ('SSH Failed, Pastikan SSH Aktif')

print ('Memulai Backup Konfigurasi')
runningconfig = net_connect.send_command('show running-config')
savefile = os.path.join(path, "csr1kv-"+str(today)+".txt")
save = open(savefile,"w")
save.write(runningconfig)
save.close
print ('Selesai Backup')
