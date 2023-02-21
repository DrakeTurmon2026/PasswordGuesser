import string
import time
MAX_LENGTH = 20
AVAILCHARS = string.printable
AVAILCHARS = list(AVAILCHARS)
AVAILCHARS.insert(0,"")
ToBrute = input("Input a password to bruteforce (20 chars): ")
Curstring = []
tim = 0
Curtime = time.time()
prevtime = Curtime
#setup curstring
for i in range(MAX_LENGTH):
    Curstring.append(0)

def main():
    global MAX_LENGTH,tim,Curtime,prevtime,ToBrute,AVAILCHARS,Curstring
    while AVAILCHARS[Curstring[MAX_LENGTH-1]] != AVAILCHARS[len(AVAILCHARS)-1]:
        for bigL in AVAILCHARS:
            for Char in range(len(Curstring),0,-1):
                if Char == 20:
                    Curstring[Char-1] += 1
                else:
                    if Curstring[Char] == (len(AVAILCHARS) - 1):
                        Curstring[Char-1] += 1
                        Curstring[Char] = 1

            Curtime = time.time()
            tim += Curtime - prevtime
            prevtime = Curtime
            
            returnstring = ""
            for char in Curstring:
                returnstring += AVAILCHARS[char]
            
            print(returnstring)

            if returnstring == ToBrute:
                print("Guessed '" + ToBrute + "' in time " + str(tim))
                return

    

main()