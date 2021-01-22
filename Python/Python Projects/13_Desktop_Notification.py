#Apply 20-20-20 rule
#Look 20 feet distance for 20 seconds for every 20 minutes
import time
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break! Look 20 feet distance for 20sec!",
            timeout = 20
        )
        time.sleep(1200)