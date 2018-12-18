from util.bmob import *
import time
b = Bmob("948c56e3c177b6b30467f4c97500f4ef", "7bb090c10ddb12c81b29a714fc610156")

def stampToTime(stamp):
    # datatime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(str(stamp)[0:10])))
    datatime = time.strftime("%Y-%m-%d",time.localtime(float(str(stamp)[0:10])))
    return datatime

def getDate():
    c = b.cloudCode("getDtae").jsonData
    stamp = c["result"]
    return stampToTime(stamp)

def insert(classname,data):
    pass
