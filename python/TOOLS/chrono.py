import time

print("WELCOME IN MINUTOR")

sec = 0
secint = 0

print("Ok to start")
go = (input('GO?: '))
char = 'Ok'
sec2 = 3
while sec2 > 0:
            print(sec2)
            sec2 -= 1
            time.sleep(1)#temps en secondes d'intervalles

while go == char:
    if go == char:
        sec = int(input('Enter a time in seconds: '))
        secint = float(input('Enter an interval of seconds between each secondes: '))
        print("MINUTOR ON") 
        while sec > 0:
            print(sec)
            sec -= 1
            time.sleep(secint)#temps en secondes d'intervalles 
           
        else:
            print("You quit the MINUTOR")
            break