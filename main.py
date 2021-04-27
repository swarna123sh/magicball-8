import random
def answers(ch):
  if ch==1:
    print("It is certain")
  elif ch==2:
    print("Good outlook")  
  elif ch==3:
    print("Most likely")
  elif ch==4:
    print("Reply hazy")    
  elif ch==5:
    print("Cannot predict now")
  elif ch==6:
    print("ConceNtrate and ask again")
  elif ch==7:
    print("My reply is no")  
  elif ch==8:
    print("Very doubtful")  
  elif ch==9:
    print("Better not tell you now")  
  elif ch==10:
    print("Dont count on it")  
  elif ch==11:
    print("As I see it, Yes")
  elif ch==12:
    print("Without a doubt")
  elif 13:
    print("Not sure") 
  else:
    print("Ask again later")   

print("Hello There, I am the Magic 8 Ball, What is your name?")
name = input()
print('Hello ' + name)

def MagicBall8():
    print('Ask me a question.')
    input()
    p=random.randint(1, 14)
    answers(p)
    print('I hope that helped!')
    Replay()

def Replay():
    print ('Do you have another question? [Y/N] ')
    reply = input()
    if reply.upper() == 'Y':
        MagicBall8()
    elif reply.upper() == 'N':
        print("Great playing with you")
    else:
        print('Sorry, didnt get the question. Can you please repeat.')
        Replay()
	
MagicBall8()
