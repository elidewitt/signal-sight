

import ntplib
def clock(i):
    print("Getting time data...")
    try:
        client = ntplib.NTPClient()
        response = client.request("pool.ntp.org")
        startTime = response.tx_time
        print("Successfully retrieved time data")
        return startTime
    except:
        if (i < 10):
            print("Time data retrieval failed. Retrying...")
            clock(i+1)
        else:
            print("unable to get time data. Exiting...")
            exit()
