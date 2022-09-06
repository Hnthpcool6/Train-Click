from pickle import TRUE
import random

import pygame
import os
# path
# PATH_FILE = os.path.dirname(__file__)
# PATH_SCORE = 'Score.txt'
# True or False
running = True
start = True
choose = False
play =  False
create = False
save =  False

# color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREY = (100,100,100)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BG_C_R = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
BG_C_R_2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
BG_C_R_3 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
BG_C = GREY

# position
X_TITLE = 100
Y_TITLE = 40
Y_S = 300
Y_Q = 450
X_S = X_Q = 235
Y_E = 295
Y_M = 410
Y_H = 525

X_E =X_M =X_H = 390

X_R = 100
Y_R = 385

Y_Y = Y_N = 450
X_Y = 90
X_N = 380

X_Q_2 = 50
X_B = 125
Y_Q_2 = Y_B = 590

#  size
S_X_TITLE = 520
S_Y_TITLE = 200
S_X_S = S_X_Q = S_X_Y =S_X_N = 250
S_Y_S = S_Y_Q = S_Y_Y =S_Y_N = 75
S_X_E =S_X_M =S_X_H = 150
S_Y_E =S_Y_M =S_Y_H = 60
S_X_R = 150
S_Y_R = 150
S_X_Q_2 = S_X_B = 50
S_Y_Q_2 = S_Y_B = 25

# R 
R_H=15
R_M=25
R_E=50
# R_R_L= random.randint(15,50)
