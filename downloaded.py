import os
from timeit import default_timer as timer
def is_download_complete():

    entries = os.listdir('G:\Toy_etl_project\masters_data')
    length=len(entries)

    cur=length
    
    start=timer()
    end =timer()
    # checking for a max time of 5 mins
    while(end-start<300):
        end=timer()
        cur=len(os.listdir('G:\Toy_etl_project\masters_data'))
        if(cur>=length+1 and check()):
            break
        
    if(end-start>=300):
        return 0
    return 1

def check(): # checking if file format is .tsv of all files / checking for incomplete download or other file formats
    entries = os.listdir('G:\Toy_etl_project\masters_data')
    for file in entries:

        split_tup = os.path.splitext(file)
        
        if(split_tup[1].lower()=='.crdownload' or split_tup[1].lower()=='.tmp'):
            return False
  
        
    return True

    #check for substring