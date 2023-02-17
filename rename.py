import os
import datetime
from datetime import datetime


def rename_downloaded_files():
        
        # list that contains each file present in masters_ data directory 
        entries = os.listdir('G:\Toy_etl_project\masters_data')
        
        
        for file in entries:
            cnt=0

            # if file doesnt contain required pattern as substring then skip
            if(file!='export_masters_input_ean_master.tsv' and file!='export_masters_input_store_master.tsv'):continue

            # name of the downloaded file 
            old_name = 'G:/Toy_etl_project/masters_data'+'/'+file

            name=''
            date=datetime.today().strftime('%Y%m%d')
       
            if(file=='export_masters_input_ean_master.tsv'):name='EAN_MASTER'
            else:name='STORE_MASTER'
            new_name='G:/Toy_etl_project/masters_data'+'/'+name+'_'+date+'_'+'N-Interns-140.tsv'

            # removing previous file if any with same name 
            if(os.path.exists(new_name)):
                os.remove(new_name)
            
            # renaming current file
            os.rename(old_name, new_name)


        




