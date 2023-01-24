import os

def is_download_complete():

    entries = os.listdir('G:\Toy_etl_project\masters_data')
    length=len(entries)

    cur=len
   
    while(True):
        cur=len(os.listdir('G:\Toy_etl_project\masters_data'))
        if(cur==length+1 and check()):
            break
        

    return

def check():
    entries = os.listdir('G:\Toy_etl_project\masters_data')
    for file in entries:

        split_tup = os.path.splitext(file)
        #print(split_tup[1],split_tup)
        if(split_tup[1].lower()!='.tsv'):
            
            return False
        
    return True