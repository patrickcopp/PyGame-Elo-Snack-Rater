# Author: Patrick Copp
#
import pygame
import os
import random



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
add_pics(random.sample(range(0, 30), 2))
pygame.display.update()

run = True
while run:
    pygame.time.delay(80)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                win.fill((0, 0, 0))
                pygame.draw.rect(win, (255, 0, 0), (501, 0, 2, 500))
                competitors=random.sample(range(0, 30), 2)
                add_pics(competitors)
                pygame.display.update()

            if event.key == pygame.K_RIGHT:
                win.fill((0, 0, 0))
                pygame.draw.rect(win, (255, 0, 0), (501, 0, 2, 500))
                competitors=random.sample(range(0, 30), 2)
                add_pics(competitors)
                pygame.display.update()
    
    keys = pygame.key.get_pressed()

    
    pygame.event.pump()

    



