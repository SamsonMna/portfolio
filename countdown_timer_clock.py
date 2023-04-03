# Time is money Tik-Tok...I mean tic toc...
# CountDown Timer clock
import time
# ⌚ = user_time
def countdown(⌚): # Replace the watch with the term user_time above
    while ⌚ >= 0:
        mins, secs = divmod(⌚, 60)
        timer = '{02d}:{02d}'.format(mins, secs) # Add a third {02d} if you wanna have your timer run for hours
        print(timer, end='\r')
        time.sleep(1)
        ⌚ -= 1
    print("3, 2, 1, 0 We have the lift off!!!") # The timer starts
    
if__name__ == '__main__':
    ⌚ = int(input("Enter a time in seconds: "))
    contdown(⌚)
    
    
    
