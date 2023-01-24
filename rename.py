import os
import time


def rename_downloaded_files():
        entries = os.listdir('G:\Toy_etl_project\masters_data')
        list=[]
        for file in entries:
            #print(file)
        # Path to the file/directory
            path = 'G:/Toy_etl_project/masters_data'+'/'+file
            

    # Both the variables would contain time
    # elapsed since EPOCH in float
            ti_c = os.path.getctime(path)
            ti_m = os.path.getmtime(path)

    # Converting the time in seconds to a timestamp
            c_ti = time.ctime(ti_c)
            m_ti = time.ctime(ti_m)
            list.append([m_ti,file])
            #print(file,m_ti,"\n")

        list.sort(reverse=True)
        new_list=[]
        cnt=0
        for lists in list:
            if(cnt==2):  #extracting first 2
                break
            else:
                new_list.append(lists[1])
            cnt=cnt+1
        #print(new_list)
        directory='G:/Toy_etl_project/masters_data'
        #print(len(list))
        cnt1=max(0,len(list)-2)//2
        cnt1=cnt1+1
        cnt2=cnt1
        #print(cnt1,cnt2)
        file_cnt=0
        for file in new_list:
            file_cnt=file_cnt+1
            old_file = os.path.join(directory, file)
            if(file_cnt%2==1):
                new_file = os.path.join(directory, "store "+str(cnt1)+'.tsv')
                cnt1=cnt+1
            else:
                new_file = os.path.join(directory, "ean "+str(cnt2)+'.tsv')
                cnt2=cnt2+1
            
           
            os.rename(old_file, new_file)