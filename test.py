import time

starttime = time.time()

for i in range(3):
    time.sleep(1)

endtime = time.time()
print("Working Time :",endtime-starttime)
print("Working Time : {}".format(endtime-starttime))
print(f"Working Time : {endtime-starttime}")