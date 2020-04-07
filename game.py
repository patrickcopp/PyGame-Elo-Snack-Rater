# Author: Patrick Copp
#
import pygame
import os
import random
import math


def elo_init(rankable):
    with open ('elo.txt','w+') as file:
        for each in rankable:
            file.write(each+'#1000'+'\n')
    print('Elo Initialized')

def add_pics(nums):
    pic1=nums[0]
    pic2=nums[1]
    win.blit(images[pic1][1],  (((500-images[pic1][1].get_size()[0])/2)    , ((500-images[pic1][1].get_size()[1])/2) ))
    win.blit(images[pic2][1],  (502+((500-images[pic2][1].get_size()[0])/2), ((500-images[pic2][1].get_size()[1])/2) ))

def elo_update(competitors, K, d):
    left_name =  images[competitors[0]][0]
    right_name = images[competitors[1]][0]

    left_rating=0
    right_rating=0

    file_copy=[]

    with open('elo.txt','r') as file:
        for line in file:
            file_copy.append(line)
            if line.split('#')[0] == left_name:
                left_rating=float(line.split('#')[1])
            if line.split('#')[0] == right_name:
                right_rating=float(line.split('#')[1])
    
    prob_left=Probability(right_rating,left_rating)
    prob_right=Probability(left_rating,right_rating)

    print('Left: '+str(left_rating)+', '+str(prob_left))
    print('Right: '+str(right_rating)+', '+str(prob_right))

    if d==0:
        left_rating = left_rating + K * (1-prob_right)
        right_rating = right_rating + K * (0-prob_left)
    if d==1:
        left_rating = left_rating + K * (0-prob_right)
        right_rating = right_rating + K * (1-prob_left)

    with open('elo.txt','w+') as file:
        for each in file_copy:
            copier=each
            if each.split('#')[0]==left_name:
                copier=left_name+'#'+str(left_rating)+'\n'
                print('Writing: '+copier)
            if each.split('#')[0]==right_name:
                copier=right_name+'#'+str(right_rating)+'\n'
                print('Writing: '+copier)
            
            file.write(copier)

def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400)) 


pygame.init()
win=pygame.display.set_mode((1002, 500))

pygame.display.set_caption('Snack Ranker')

rankable=os.listdir('img/')
print(len(rankable))
images=[]

for each in rankable:
    images.append((each,pygame.image.load('img/'+each)))

if not os.path.exists('elo.txt'):
    elo_init(rankable)


pygame.draw.rect(win, (255, 0, 0), (501, 0, 2, 500))
competitors=random.sample(range(0, 30), 2)
add_pics(competitors)
pygame.display.update()

run = True
while run:
    pygame.time.delay(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:

                elo_update(competitors,30,0)

                win.fill((0, 0, 0))
                pygame.draw.rect(win, (255, 0, 0), (501, 0, 2, 500))
                competitors=random.sample(range(0, 30), 2)
                add_pics(competitors)
                pygame.display.update()

            if event.key == pygame.K_RIGHT:

                elo_update(competitors,30,1)

                win.fill((0, 0, 0))
                pygame.draw.rect(win, (255, 0, 0), (501, 0, 2, 500))
                competitors=random.sample(range(0, 30), 2)
                add_pics(competitors)
                pygame.display.update()
    
    keys = pygame.key.get_pressed()

    
    pygame.event.pump()

    



