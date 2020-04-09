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
            if each.split('#')[0]==right_name:
                copier=right_name+'#'+str(right_rating)+'\n'
            
            file.write(copier)

def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400)) 

def read_sort():
    with open('elo.txt','r') as file:
        lines=[line.rstrip() for line in file.readlines()]
    ranked=[tuple(i.split('#')) for i in lines]
    ranked=sorted(ranked, key=lambda tup: float(tup[1]))
    ranked.reverse()
    label=[]
    count=1
    font = pygame.font.Font(pygame.font.get_default_font(), 16) 
    for each in ranked:
        if count<10:
            label.append(font.render('  '+str(count)+'. '+each[0][:-4], True, (255, 255, 255)))
        else:
            label.append(font.render(str(count)+'. '+each[0][:-4], True, (255, 255, 255)))
        count+=1
    return label
        

pygame.init()
win=pygame.display.set_mode((1002, 500))  

pygame.display.set_caption('Snack Ranker')

rankable=os.listdir('img/')
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
exit=False
while run:
    pygame.time.delay(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not exit:

                elo_update(competitors,30,0)

                win.fill((0, 0, 0))
                pygame.draw.rect(win, (255, 0, 0), (501, 0, 2, 500))
                competitors=random.sample(range(0, 30), 2)
                add_pics(competitors)
                pygame.display.update()

            if event.key == pygame.K_RIGHT and not exit:

                elo_update(competitors,30,1)

                win.fill((0, 0, 0))
                pygame.draw.rect(win, (255, 0, 0), (501, 0, 2, 500))
                competitors=random.sample(range(0, 30), 2)
                add_pics(competitors)
                pygame.display.update()
            
            if event.key == pygame.K_ESCAPE and not exit:
                exit=True
                win.fill((0, 0, 0))
                
                text=read_sort()
                for line in range(len(text)):
                    win.blit(text[line], (50,10+(16*line)))
                pygame.display.update()
                pygame.time.delay(80)

            if event.key == pygame.K_ESCAPE and exit:
                run = False

    keys = pygame.key.get_pressed()

    
    pygame.event.pump()
