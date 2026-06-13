import pygame
from Graphics import *
from TicTacToe import TicTacToe
from State import State
from Human_Agent import Human_Agent
from Random_Agent import Random_Agent
from AI_Agent import AI_Agent

PATH = 'Data/Q_Agent_As_O.pth' # ודא שהנתיב לתיקייה מדויק

pygame.init()
clock = pygame.time.Clock()
graphics = Graphics()
env = TicTacToe(State())

# הגדרת השחקנים
player1 = Human_Agent(1, env, graphics)
player2 = AI_Agent(-1, env, graphics, Q_table_PATH=PATH, train=False)

def main ():
    player = player1
    run = True
    
    while (run):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False
        
        # ניהול מהלכים לפי סוג השחקן הנוכחי
        if player == player1:
            # תור האדם: מחכים לאירוע לחיצה (MOUSEBUTTONDOWN)
            action = player1.get_action(events)
        else:
            # תור ה-AI: הוא לא צריך אירועים, רק את מצב הלוח
            pygame.time.wait(500) # השהייה קלה של חצי שנייה כדי שהמהלך של ה-AI לא יהיה מיידי ומלחיץ
            action = player2.get_action(state=env.state)
            
        if action:
            env.move(action)
            player = switch_players(player)
            
            # בדיקה אם המשחק הסתיים
            if env.state.end_of_game != 0:
                graphics(env.state)
                pygame.time.wait(2000)            
                env.state.reset()
                player = player1  # האדם פותח שוב
                
        graphics(env.state)
        clock.tick(FPS)
        
    pygame.quit()

def switch_players(player):
    if player == player1:
        return player2
    else:
        return player1

if __name__ == '__main__':
    main()