import firebase

class ScheduledLight:
    def __init__(self, light_id):

        self.id = light_id

        self.scheduleData = firebase.db.child(self.id).child("schedule").get().val()[0] # only considers first schedule

        self.offset = self.scheduleData["offset"]
        self.schedule = self.scheduleData["schedule"]

        self.cycleLength = 0
        for event in self.schedule:
            self.cycleLength += event["duration"]

    def getStatus(self, t):
        timeToday = t % 86400    
        sum = 0
        status = ""
        for event in self.schedule:
            sum += event["duration"]
            if ((timeToday - self.offset) % self.cycleLength < sum):
                status = event["status"]
                break
        return status

def init_light(light_id, attempts):
    print("Getting light data...")
    try:
        target = ScheduledLight(light_id)
        print("Successfully retrieved light data")
        return target
    except:
        if (attempts > 0):
            print("Light data retrieval failed. Retrying...")
            init_light(light_id, attempts-1)
        else:
            print("Unable to get light data. Exiting...")
            exit()
