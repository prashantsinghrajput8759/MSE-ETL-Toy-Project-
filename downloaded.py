import os

def is_download_complete(path):

    entries = os.listdir(path)
    print('is_download ',entries)
    length=len(entries)

    cur=len
    return
    while(True):
        
        entries = os.listdir(path)
        if(len(entries)==0):
            continue
        for file in entries:

            split_tup = os.path.splitext(file)
            #print(split_tup[1],split_tup)
            if(split_tup[1].lower()!='.tsv'):
                
                continue
            else:
                break
        break
    
            
        




    


# check name pattern / date is mandatory
# check for parallel downloads
# check if 1st file is downloaded then go for next
#presence of element
#srinath

# solution for parallel downloads or some 
#manually adding the file in the download directory

# can we create a random directory for
# temporarily storing the downloaded file
# then rename it and transfer it to the main download dirctory

# why to do this?
# because the main download directory path is known 
#so in case of parallel download every file will
#be directly downloaded there
#once we create temp downlpad folder 
#each file will first get into their respective folder