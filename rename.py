import os
import time
import datetime
     
# using now() to get current time
current_time = datetime.datetime.now()


def rename_downloaded_files():
        entries = os.listdir('G:\Toy_etl_project\masters_data')
        
        
        for file in entries:
            cnt=0
        # Path to the file
            old_name = 'G:/Toy_etl_project/masters_data'+'/'+file
            name=''
            for char in file:
                if(char=='_'):
                    cnt=cnt+1
                    if(cnt>3):
                        name+=char
                    continue
                if(cnt>=3):
                    if(char=='.'):
                        break
                    name+=char
            cur_time=datetime.datetime.now()
            day=cur_time.day
            month=cur_time.month
            year=cur_time.year
            day=str(day)
            month=str(month)
            year=str(year)
            if(len(day)==1):day='0'+day
            if(len(month)==1):month='0'+month
            day=day.upper()
            month=month.upper()
            year=year.upper()
            name=name.upper()
            new_name='G:/Toy_etl_project/masters_data'+'/'+name+'_'+year+month+day+'_'+'N-Interns-140 Prashant Singh'+'.tsv'
            os.rename(old_name, new_name)


        





    # # Both the variables would contain time
    # # elapsed since EPOCH in float
    #         ti_c = os.path.getctime(path)
    #         ti_m = os.path.getmtime(path)

    # # Converting the time in seconds to a timestamp
    #         c_ti = time.ctime(ti_c)
    #         m_ti = time.ctime(ti_m)
    #         list.append([m_ti,file])
    #         #print(file,m_ti,"\n")

    #     list.sort(reverse=True)
    #     new_list=[]
    #     cnt=0
    #     for lists in list:
    #         if(cnt==2):  #extracting first 2
    #             break
    #         else:
    #             new_list.append(lists[1])
    #         cnt=cnt+1
    #     #print(new_list)
    #     directory='G:/Toy_etl_project/masters_data'
    #     #print(len(list))
    #     cnt1=max(0,len(list)-2)//2
    #     cnt1=cnt1+1
    #     cnt2=cnt1
    #     #print(cnt1,cnt2)
    #     file_cnt=0
    #     for file in new_list:
    #         file_cnt=file_cnt+1
    #         old_file = os.path.join(directory, file)
    #         if(file_cnt%2==1):
    #             new_file = os.path.join(directory, "store "+str(cnt1)+'.tsv')
    #             cnt1=cnt+1
    #         else:
    #             new_file = os.path.join(directory, "ean "+str(cnt2)+'.tsv')
    #             cnt2=cnt2+1
            
           