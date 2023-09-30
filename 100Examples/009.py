import time

my_list = [1,2,3,4]
for i in my_list:
    print(time.strftime("%H:%M:%S",time.localtime()),":",i)
    time.sleep(1)