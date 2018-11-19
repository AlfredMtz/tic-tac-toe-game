import game_func


def play():

    # Full body structure of the game, with its corresponding functions
    print("LET'S GO!")

    while True:
        # set board to empty strings and ask player for prefer symbol
        theBoard = [' '] * 10
        player1_marker, player2_marker = game_func.player_input()
        
        # Randomly select a player to go first
        turn = game_func.choose_first()
        print(str(turn), "will go first.")
        play_game = input("Are you ready to play? y or n? ")
        
        # Ask player weather it is ready to play or not
        if play_game == 'y':
            game_on = True
        else:
            game_on = False

        
        while game_on:
            
            # Proceed to statement if player one gets to go first
            if turn == 'Player 1':
                
                game_func.display_board(theBoard)
                position = game_func.player_choice(theBoard)
                game_func.place_marker(theBoard, player1_marker, position)

                if game_func.win_check(theBoard, player1_marker):
                    game_func.display_board(theBoard)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if game_func.full_board_check(theBoard):
                        game_func.display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:

                # Proceed with statement if its Player 2s' turn
                game_func.display_board(theBoard)
                position = game_func.player_choice(theBoard)
                game_func.place_marker(theBoard, player2_marker, position)

                if game_func.win_check(theBoard, player2_marker):
                    game_func.display_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if game_func.full_board_check(theBoard):
                        game_func.display_board(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 1'
                        
        # Ask players weather they want to play again or not!
        if not game_func.replay():
            break   


# start the game
play()