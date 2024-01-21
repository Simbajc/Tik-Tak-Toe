# display the game board
def displayGameBoard(top , middle, bottom):
    print("Game Board:\n")
    print("    1   2   3\n")
    print("A   "+ top[0] + " | " + top[1] + " | " + top[2] + " ")
    print("   -----------")
    print("B   "+ middle[0] + " | " + middle[1] + " | " + middle[2] + " ")
    print("   -----------")
    print("C   "+ bottom[0] + " | " + bottom[1] + " | " + bottom[2] + " ")

# changes the board to make is display the valid player move
def boardChange(move, T, M, B, Pl):
    piece = "X"
    if(Pl == 1):
        piece = "X"
    else:
        piece = "O"

    if(move[0].lower() == 'a'):
        T[int(move[1]) - 1] = piece
    elif(move[0].lower() == 'b'):
        M[int(move[1]) - 1] = piece
    elif(move[0].lower() == 'c'):
        B[int(move[1]) - 1] = piece


# checks if player makes a valid move
def validMove(move, T, M, B):
    if(move.lower() == "w"):
        return True
    if(len(move) != 2):
        return False
    elif(move[0].isalpha() == False or move[1].isdigit() == False):
        return False
    elif(int(move[1]) < 1 or int(move[1]) > 3):
        return False
    elif(str(move[0]).lower() != 'a' and str(move[0]).lower() != 'b' and str(move[0]).lower() != 'c'):
        return False
    else:
        if(move[0].lower() == 'a'):
            if(T[int(move[1]) - 1] != " "):
                return False
        elif(move[0].lower() == 'b'):
            if(M[int(move[1]) - 1] != " "):
                return False
        elif(move[0].lower() == 'c'):
            if(B[int(move[1]) - 1] != " "):
                return False
    return True

def winCondition(T, M, B):
    # win condition for rows
    if(T[0] == T[1] and T[0] == T[2] and T[0] != " "):
        return True
    elif(M[0] == M[1] and M[0] == M[2] and M[0] != " "):
        return True
    elif(B[0] == B[1] and B[0] == B[2] and B[0] != " "):
        return True
    # win conditions for columns
    elif(T[0] == M[0] and T[0] == B[0] and T[0] != " "):
        return True
    elif(T[1] == M[1] and T[1] == B[1] and T[1] != " "):
        return True
    elif(T[2] == M[2] and T[2] == B[2] and T[2] != " "):
        return True
    # win condition for diagonal
    elif(T[0] == M[1] and T[0] == B[2] and T[0] != " "):
        return True
    elif(T[2] == M[1] and T[2] == B[0] and T[2] != " "):
        return True
    else:
        return False
    
def drawCondition(T, M, B):
    # win condition for rows
    if(T[0] != " " and T[1] != " " and T[2] != " "):
        if(M[0] != " " and M[1] != " " and M[2] != " "):
            if(B[0] != " " and B[1] != " " and B[2] != " "):
                return True
    return False

def main():
    player = 1
    topBoard = [ " ", " ", " "]
    middleBoard = [ " ", " ", " "]
    bottomBoard = [ " ", " ", " "]
    gameStart = False
    gameEnd = False
    validM = False
    print("Welcome to Tic-Tak-Toe")
    # Starts game
    while(gameStart == False):
        userStart = input("Would you like to start? (Y/N): ")
        if(userStart.lower() == "y"):
            gameStart = True;
    

    x = 0
    # game function
    while(gameEnd == False):
        print("Player 1: X  Player 2: O EndGame: W")
        print("Player " + str(player) + " turn: ")
        displayGameBoard(topBoard, middleBoard, bottomBoard)
        # check if move is valid or not
        while(validM == False): 
            move = input("Make your move: ")
            if( validMove(move, topBoard, middleBoard, bottomBoard) == True):
                validM = True
        if(move.lower() == "w"):
            break
    
        boardChange(move, topBoard, middleBoard, bottomBoard, player)
        if( winCondition(topBoard, middleBoard, bottomBoard) or drawCondition(topBoard, middleBoard, bottomBoard)):
            if(winCondition(topBoard, middleBoard, bottomBoard) ):
                print("Player " + str(player) + " Wins!")
            else:
                print("It's a Draw!")
            displayGameBoard(topBoard, middleBoard, bottomBoard)
            endChoice = input("Restart= 1 End Game= 2 : ")
            while(endChoice != "1" and endChoice != "2"):
                endChoice = input("Restart= 1 End Game= 2 : ")
            
            if(endChoice == "1"):
                topBoard = [ " ", " ", " "]
                middleBoard = [ " ", " ", " "]
                bottomBoard = [ " ", " ", " "]
                player = 2
            else:
                gameEnd = True
        if(player == 1):
            player+=1
        else:
            player-=1
        validM = False

    print("Game End")











if __name__ == "__main__":
    main()