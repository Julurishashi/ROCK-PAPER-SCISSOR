def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])% 3
    p2=int(num2[bit2])% 3
    if(player_one[p1]==player_two[p2]):
        print ("DRAW")
    elif(player_one[p1]=="ROCK" and player_two[p2]=="SCISSOR"):
        print("PLAYER ONE WINS!")
    elif(player_one[p1]=="ROCK" and player_two[p2]=="PAPER"):
        print("PLAYER TWO WINS!")
    elif(player_one[p1]=="paper" and player_two[p2]=="SCISSOR"):
        print("player two wins!")
    elif(player_one[p1]=="PAPER" and player_two[p2]=="ROCK"):
        print("player one wins!")
    elif(player_one[p1]=="SCISSOR" and player_two[p2]=="PAPER"):
        print("player one wins!")
    elif(player_one[p1]=="SCISSOR" and player_two[p2]=="ROCK"):
        print("player two wins!")
    

player_one={0:'ROCK',1:'PAPER',2:'SCISSOR'}
player_two={0:'PAPER',1:'ROCK',2:'SCISSOR'}
while(1):
    num1=(input("player 1 enter your choice"))
    num2=(input("player 2 enter your choice"))
    bit1=int(input(" player 1 , enter your bit position  "))
    bit2=int(input("player2,enter your bit position"))
    rock_paper_scissor(num1,num2,bit1,bit2)
                                         
    ch=(input("do you want to continue y/n"))
    if (ch=='n'):
        break
