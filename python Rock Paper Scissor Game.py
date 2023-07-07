#python Rock Paper Scissor Game
import Rock_Paper_Scissor_game.Ascii as Ascii
import random as ran
def Rock_Paper_Scissor():
    inp1=int(input("Enter a whole number between (0-2),where 0 = Rock ,1=Paper,2=Scissor: "))   
    a=ran.randint(0,2)
    print(inp1)
    print(Ascii.Ascii1[(inp1)])
    print(a)
    print(Ascii.Ascii1[a])
    if inp1==a:
        print("Try Again")
        Rock_Paper_Scissor(inp1)
    elif inp1 !=a:
        if inp1==1 and a==2:
            print("computer wins")
            play_again(inp2=input("Press Y or 'y' to play more: "))
        elif inp1==0 and a==1:
            print("User Wins")
            play_again(inp2=input("Press Y or 'y' to play more: "))
        elif inp1==1 and a==0:
            print("Computer Wins")
            play_again(inp2=input("Press Y or 'y' to play more: "))
        elif inp1==2 and a==1:
            print("User Wins")
            play_again(inp2=input("Press Y or 'y' to play more: "))
        elif inp1==0 and a==2:
            print("User Wins")
            play_again(inp2=input("Press Y or 'y' to play more: "))
        elif inp1==2 and a==0:
            print("Computer Wins")
            play_again(inp2=input("Press Y or 'y' to play more: "))
def play_again(inp2):
    if inp2=="Y" or inp2=="y":
        Rock_Paper_Scissor()
    else:
        print("Game Over")
Rock_Paper_Scissor()