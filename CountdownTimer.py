import time
countdown = int(input("Insert time in seconds: "))
for x in range(countdown,0,-1):
    seconds= x%60
    minute=int((x/60))%60
    hr = int((x/60)/60)
    print(f"{hr:02}:{minute:02}:{seconds:02}")
    time.sleep(1)
print("Time's UP")