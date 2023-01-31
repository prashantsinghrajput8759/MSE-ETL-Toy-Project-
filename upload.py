import pysftp
import os
host='ftp.increff.com'
username='increff'
password='!CL@Pgkh2Xt8'

Cnopts=pysftp.CnOpts()
Cnopts.hostkeys=None
def upload_files():

    with pysftp.Connection(host=host, username=username, password=password,cnopts=Cnopts) as sftp:
        print('connection established')
        
        with sftp.cd('/irisx-etl/ToyETL/Masters'):
            
            entries = os.listdir('G:\Toy_etl_project\masters_data')
            for file in entries:
                if(file.find('N-Interns-140')==-1 or (file.find('EAN_MASTER')==-1 and file.find('STORE_MASTER')==-1)):continue
                sftp.put("G:/Toy_etl_project/masters_data/"+file,preserve_mtime=True)
        
            


 

##only put specific files


#  x=sftp.listdir()
#         print(x)
# print('dir changed')
        # print(sftp.pwd)
        # sftp.get('remote_file')
        # x=sftp.listdir()
        # print(x)