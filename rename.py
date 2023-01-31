import os
import datetime
import time
from datetime import datetime


# using now() to get current time
# current_time = datetime.datetime.now()


def rename_downloaded_files():
        entries = os.listdir('G:\Toy_etl_project\masters_data')
        
        
        for file in entries:
            cnt=0
            if(file!='export_masters_input_ean_master.tsv' and file!='export_masters_input_store_master.tsv'):continue
        # Path to the file
            old_name = 'G:/Toy_etl_project/masters_data'+'/'+file
            name=''
          
            date=datetime.today().strftime('%Y%m%d')
       
            if(file=='export_masters_input_ean_master.tsv'):name='EAN_MASTER'
            else:name='STORE_MASTER'
            new_name='G:/Toy_etl_project/masters_data'+'/'+name+'_'+date+'_'+'N-Interns-140.tsv'
            if(os.path.exists(new_name)):
                os.remove(new_name)
            
            os.rename(old_name, new_name)


        




