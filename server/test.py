from datetime import *
def showtime(time):
    now = datetime.now()
    now_15 = now + timedelta(seconds=int(time))
    return now_15

print(showtime(0))
print(showtime(10))