import time

num = 0
while True:
    
    if(num <= 0):
        time.sleep(1)
        num+=1
    else:
        print(num)
        num+=1
