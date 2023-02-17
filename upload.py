import pysftp
import os

# credentials to login
host = 'ftp.increff.com'
username = 'increff'
password = '!CL@Pgkh2Xt8'

Cnopts = pysftp.CnOpts()
Cnopts.hostkeys = None


def upload_files():
    # establishing connection
    with pysftp.Connection(host=host, username=username, password=password, cnopts=Cnopts) as sftp:
        print('connection established')

        with sftp.cd('/irisx-etl/ToyETL/Masters'):

            entries = os.listdir('G:\Toy_etl_project\masters_data')

            # loop over each file in directory
            for file in entries:

                # if files are present other than recently downloaded then skip uploading it  
                if (file.find('N-Interns-140') == -1 or (file.find('EAN_MASTER') == -1 and file.find('STORE_MASTER') == -1)):
                    continue

                # upload file
                sftp.put("G:/Toy_etl_project/masters_data/" +file, preserve_mtime=True)
