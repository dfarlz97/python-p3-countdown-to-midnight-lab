import time

def countdown(nummy):
    while nummy != 0:
        print(f"{nummy} SECOND(S)!")
        nummy -= 1 
        if nummy == 0: 
            print("HAPPY NEW YEAR!")


def countdown_with_sleep(nummy):
    while nummy != 0:
        print(f"{nummy} SECOND(S)!")
        nummy -= 1
        time.sleep(1)
        if nummy == 0: 
            print("HAPPY NEW YEAR!")
