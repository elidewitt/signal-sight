import ntplib, time
from datetime import datetime

def init_clock(attempts):
    print("Getting time data...")
    try:
        client = ntplib.NTPClient()
        response = client.request("pool.ntp.org")
        startTime = response.tx_time
        print("Successfully retrieved time data")
        return startTime
    except:
        if (attempts > 0):
            print("Time data retrieval failed. Retrying...")
            return init_clock(attempts+1)
        else:
            print("unable to get time data. Exiting...")
            exit()

startTime = init_clock(3) # attempt n times to connect
t0 = datetime.now().timestamp()

def updateTime(freq):
    time.sleep(freq)
    deltaTime = datetime.now().timestamp() - t0
    currentTime = startTime + deltaTime
    return currentTime
