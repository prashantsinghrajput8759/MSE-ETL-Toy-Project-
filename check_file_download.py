import os
from timeit import default_timer as timer


def is_download_complete():

    entries = os.listdir('G:\Toy_etl_project\masters_data')
    length=len(entries)
    start=timer()
    end =timer()
    # checking for a max time of 15 sec
    while(end-start<15): 
        end=timer()
        cur=len(os.listdir('G:\Toy_etl_project\masters_data'))
        if(cur>=length+1 and check()):
            break
        
    if(end-start>=15):
        return 0
    return 1

def check():
    # checking if file format is .tsv of all files / checking for incomplete download or other file formats
    # .crdownload or .tmp is the extension of incomplete downloads in chrome
    entries = os.listdir('G:\Toy_etl_project\masters_data')
    for file in entries:

        split_file = os.path.splitext(file)
        
        if(split_file[1].lower()=='.crdownload' or split_file[1].lower()=='.tmp'):
            return False
  
        
    return True

    #check for substring