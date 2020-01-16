import pygame,sys,time,copy,pickle,os
from pygame.locals import *

def count(monster): #战斗计算
    global atk
    global defend
    if monster==11:
        monster_hp=15
        monster_atk=3
        monster_def=0
    if monster==12:
        monster_hp=50
        monster_atk=5
        monster_def=1
    if monster==13:
        monster_hp=100
        monster_atk=10
        monster_def=2
    if monster==14:
        monster_hp=50
        monster_atk=17
        monster_def=8
    if monster==15:
        monster_hp=150
        monster_atk=defend+10
        monster_def=5
    if monster==16:
        monster_hp=300
        monster_atk=20
        monster_def=8
    if atk<=monster_def:
        return 9999
    if monster_atk<=defend:
        return 0
    if monster_hp%(atk - monster_def)==0:
        return int((monster_hp/(atk - monster_def)-1)*(monster_atk - defend))
    else:
        return int((monster_hp//(atk - monster_def))*(monster_atk - defend))

def battle(monster): #战斗
    global hp
    global money
    #怪物属性
    if monster==11:
        monster_money=1
    if monster==12:
        monster_money=2
    if monster==13:
        monster_money=3
    if monster==14:
        monster_money=4
    if monster==15:
        monster_money=5
    if monster==16:
        monster_money=35
    hp=hp-count(monster)
    if hp<=0:
        return 0
    money+=monster_money
    return 1

def judge(now,a,b):#各类事件 空地0 墙壁1 上楼2 下楼3 血瓶4 钥匙5 门6 攻击7 防御8 胜利五角星9 商店10 怪物11-20 对话NPC21-
    global x
    global y
    global key
    global victory
    global lose
    global storey
    global text1
    global text2
    global hp
    global atk
    global defend
    global message
    global message0
    if now[a][b]==2: 
        storey+=1
    if now[a][b]==3: 
        storey-=1
    if now[a][b]==4: 
        hp+=30
        pygame.mixer.music.load('get.mp3')
        pygame.mixer.music.play()
        now[a][b]=0
    if now[a][b]==5: 
        key+=1
        pygame.mixer.music.load('get.mp3')
        pygame.mixer.music.play()
        now[a][b]=0
    if now[a][b]==6: 
        if key>0:
            key-=1
            now[a][b]=0
    if now[a][b]==7: 
        pygame.mixer.music.load('get.mp3')
        pygame.mixer.music.play()
        atk+=1
        now[a][b]=0
    if now[a][b]==8: 
        pygame.mixer.music.load('get.mp3')
        pygame.mixer.music.play()
        defend+=1
        now[a][b]=0
    if now[a][b]==9:
        victory=1
    if now[a][b]==10:
        message='10金币可交换：(1)30生命'
        text1=1
        message0='(2)1攻击 (3)1防御'
        text2=1
    if now[a][b]>10 and now[a][b]<21:
        pygame.mixer.music.load('atk.mp3')
        pygame.mixer.music.play()
        if battle(now[a][b])==0:
            lose=1
        else:
            now[a][b]=0
    if now[a][b]>20:
        if now[a][b]==21:
            message='按0可打开怪物手册'
        if now[a][b]==22:
            message='战斗为回合制，攻防决定伤害'
        if now[a][b]==23:
            message='法师攻击无视你的防御'
        text1=1

def remap(m1,m2,m3): #地图重置
    global map1
    global map2
    global map3
    for i in range(0,15):
        for j in range(0,15):
            map1[i][j]=m1[j][i]
    for i in range(0,15):
        for j in range(0,15):
            map2[i][j]=m2[j][i]
    for i in range(0,15):
        for j in range(0,15):
            map3[i][j]=m3[j][i]

pygame.init()
FPS=30
fpsClock=pygame.time.Clock()
DISPLAYSURF=pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('Game（S存档，L读档）')

WHITE=(255,255,255)
BLACK=(0,0,0)
GREY=(230,230,230)
BLUE=(0,0,125)
RED=(150,0,0)
WALLCOLOR=(75,40,40)

upImg=pygame.image.load('up.jpg')
downImg=pygame.image.load('down.jpg')
leftImg=pygame.image.load('left.jpg')
rightImg=pygame.image.load('right.jpg')
starImg=pygame.image.load('star.jpg')
keyImg=pygame.image.load('key.jpg')
doorImg=pygame.image.load('door.jpg')
mon1Img=pygame.image.load('monster1.jpg')
mon2Img=pygame.image.load('monster2.jpg')
mon3Img=pygame.image.load('monster3.jpg')
mon4Img=pygame.image.load('monster4.jpg')
mon5Img=pygame.image.load('monster5.jpg')
mon6Img=pygame.image.load('monster6.jpg')
shopImg=pygame.image.load('shop.jpg')
upsImg=pygame.image.load('upstairs.jpg')
downsImg=pygame.image.load('downstairs.jpg')
npcImg=pygame.image.load('smile.jpg')
bloodImg=pygame.image.load('blood.jpg')
manImg=downImg

font1=pygame.font.Font('freesansbold.ttf',20)
font2=pygame.font.SysFont('simsunnsimsun',20)
font3=pygame.font.SysFont('simsunnsimsun',16)
victory1=font1.render('Congratulations!',True,RED,GREY)
rect1=victory1.get_rect()
rect1.center=(400,300)
lose1=font1.render('Game Over!',True,RED,GREY)
rect2=lose1.get_rect()
rect2.center=(400,300)
key1=font1.render('× 0',True,RED,WHITE)
rect3=key1.get_rect()
rect3.center=(720,470)
floor1=font2.render('1楼',True,BLACK,WHITE)
rect4=floor1.get_rect()
rect4.center=(700,100)
#message=''
#message1=font3.render(message,True,BLACK,WHITE)
#rect5=message1.get_rect()
#rect5.center=(700,520)
hp1=font2.render('生命：20',True,BLACK,WHITE)
rect6=hp1.get_rect()
rect6.center=(700,140)
atk1=font2.render('攻击：2',True,BLACK,WHITE)
rect7=atk1.get_rect()
rect7.center=(700,180)
def1=font2.render('防御：0',True,BLACK,WHITE)
rect8=def1.get_rect()
rect8.center=(700,220)
money1=font2.render('金钱：0',True,BLACK,WHITE)
rect9=money1.get_rect()
rect9.center=(700,260)
#message0=''
#message2=font3.render(message0,True,BLACK,WHITE)
#rect10=message2.get_rect()
#rect10.center=(700,540)

storey1=[[ 4, 1, 4, 1, 0, 0, 1, 2, 1, 0, 1, 0, 7, 0, 5],
         [13, 0,12, 0, 0, 0, 1,12, 1, 0, 1,13, 0, 7, 0],
         [ 1, 1, 1, 1, 0, 0, 1, 6, 1, 0, 1, 6, 1, 1, 1],
         [ 0, 8, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
         [ 8, 0,13, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [ 1, 1, 6, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 4],
         [ 0,11, 0, 6, 0, 1, 5, 5, 5, 1, 0, 0,11,11,10],
         [ 8,11,11, 1, 0, 1,11,12,11, 1, 0, 0, 1, 0, 4],
         [ 4, 7, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
         [ 1, 1, 1, 1, 0, 1, 1,11, 1, 1, 0, 0, 0, 1, 7],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [ 6, 1, 1, 1, 0, 0, 0,11, 0, 0, 0, 1, 1, 1, 1],
         [12, 0, 0, 1, 0, 1, 1, 6, 1, 1, 0, 0, 0, 0,21],
         [ 0, 8, 7, 1, 0, 1, 0, 0, 5, 1, 0, 1, 1, 1, 1],
         [ 0, 8, 7, 1, 4, 1, 0, 0, 0, 1, 0, 0, 0, 0,22]]

storey2=[[ 4, 4, 0, 1, 7, 1, 0, 3, 0, 1, 7, 1, 4, 4, 4],
         [ 4, 4, 0, 1, 7, 1, 4, 4, 4, 1, 7, 1, 4, 7, 4],
         [ 0, 0,14, 1,13, 1, 1, 0, 1, 1, 0, 1, 8, 5, 8],
         [ 1, 1, 6, 1, 0, 1,23, 0, 0, 0, 0, 1, 1, 6, 1],
         [ 5, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 5,15, 5],
         [ 1, 1, 1, 1, 0, 1, 4, 1, 5, 1, 0, 1, 0, 8, 0],
         [ 0,13, 5, 1, 0, 1, 0, 1, 0, 6, 5, 1, 0,14, 0],
         [13, 1, 1, 1, 0, 1, 0, 1, 5, 1, 0, 1, 1, 6, 1],
         [ 0, 1,13,13, 0, 1,14, 1, 1, 1, 0, 1,12,12,12],
         [13, 1,15, 1, 0, 0, 0, 0, 0, 0, 0, 1,12,12,12],
         [ 0, 0, 0, 1, 0, 1, 1, 6, 1, 1, 0, 1,12,12,12],
         [ 1, 1, 6, 1, 0, 1, 0,13, 0, 1, 0, 1, 1, 6, 1],
         [ 4, 0, 7, 1, 0, 1, 0, 4, 0, 1, 0, 0, 0, 0, 8],
         [ 0, 4, 0, 1, 0, 1,12,12,12, 1, 0, 1, 1, 1, 1],
         [ 8, 0, 4, 1, 5, 1, 7, 0, 7, 1, 0,14,15, 6, 2],]

storey3=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,9,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,16,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,4,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,0,0,0,0,0,0,0,3]]
map1=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
map2=copy.deepcopy(map1)
map3=copy.deepcopy(map1)
for i in range(0,15):
    for j in range(0,15):
        map1[i][j]=storey1[j][i]
for i in range(0,15):
    for j in range(0,15):
        map2[i][j]=storey2[j][i]
for i in range(0,15):
    for j in range(0,15):
        map3[i][j]=storey3[j][i]

x=7
y=14
victory=0
key=0
lose=0
storey=1
text1=0
text2=0
hp=50
atk=2
defend=0
money=0

book=0

while True:
    #绘制界面
    DISPLAYSURF.fill(WHITE)
    pygame.draw.line(DISPLAYSURF,BLACK,(600,0),(600,600),5)
    DISPLAYSURF.blit(keyImg,(650,450))
    key1=font1.render('× '+str(key),True,RED,WHITE)
    DISPLAYSURF.blit(key1,rect3)
    floor1=font2.render(str(storey)+'楼',True,BLACK,WHITE)
    DISPLAYSURF.blit(floor1,rect4)
    hp1=font2.render('生命：'+str(hp),True,BLACK,WHITE)
    DISPLAYSURF.blit(hp1,rect6)
    atk1=font2.render('攻击：'+str(atk),True,BLACK,WHITE)
    DISPLAYSURF.blit(atk1,rect7)
    def1=font2.render('防御：'+str(defend),True,BLACK,WHITE)
    DISPLAYSURF.blit(def1,rect8)
    money1=font2.render('金钱：'+str(money),True,BLACK,WHITE)
    DISPLAYSURF.blit(money1,rect9)
    if text1:
        message1=font3.render(message,True,BLACK,WHITE)
        rect5=message1.get_rect()
        rect5.center=(700,520)
        DISPLAYSURF.blit(message1,rect5)
    if text2:
        message2=font3.render(message0,True,BLACK,WHITE)
        rect10=message2.get_rect()
        rect10.center=(700,540)
        DISPLAYSURF.blit(message2,rect10)
    #绘制地图
    if storey==1:
        now=map1
    if storey==2:
        now=map2
    if storey==3:
        now=map3

    for i in range(0,15):
        for j in range(0,15):
            if now[i][j]==0:
                pygame.draw.rect(DISPLAYSURF,GREY,(i*40,j*40,40,40))
            if now[i][j]==1:
                pygame.draw.rect(DISPLAYSURF,WALLCOLOR,(i*40,j*40,40,40))
            if now[i][j]==2:
                DISPLAYSURF.blit(upsImg,(i*40,j*40))
            if now[i][j]==3:
                DISPLAYSURF.blit(downsImg,(i*40,j*40))
            if now[i][j]==4:
                DISPLAYSURF.blit(bloodImg,(i*40,j*40))
            if now[i][j]==5:
                DISPLAYSURF.blit(keyImg,(i*40,j*40))
            if now[i][j]==6:
                DISPLAYSURF.blit(doorImg,(i*40,j*40))
            if now[i][j]==7:
                pygame.draw.rect(DISPLAYSURF,GREY,(i*40,j*40,40,40))
                pygame.draw.polygon(DISPLAYSURF,RED,((i*40+20,j*40+10),(i*40+10,j*40+20),(i*40+20,j*40+30),(i*40+30,j*40+20)))
            if now[i][j]==8:
                pygame.draw.rect(DISPLAYSURF,GREY,(i*40,j*40,40,40))
                pygame.draw.polygon(DISPLAYSURF,BLUE,((i*40+20,j*40+10),(i*40+10,j*40+20),(i*40+20,j*40+30),(i*40+30,j*40+20)))
            if now[i][j]==9:
                DISPLAYSURF.blit(starImg,(i*40,j*40))
            if now[i][j]==10:
                DISPLAYSURF.blit(shopImg,(i*40,j*40))
            if now[i][j]==11:
                DISPLAYSURF.blit(mon1Img,(i*40,j*40))
            if now[i][j]==12:
                DISPLAYSURF.blit(mon2Img,(i*40,j*40))
            if now[i][j]==13:
                DISPLAYSURF.blit(mon3Img,(i*40,j*40))
            if now[i][j]==14:
                DISPLAYSURF.blit(mon4Img,(i*40,j*40))
            if now[i][j]==15:
                DISPLAYSURF.blit(mon5Img,(i*40,j*40))
            if now[i][j]==16:
                DISPLAYSURF.blit(mon6Img,(i*40,j*40))
            if now[i][j]>20:
                DISPLAYSURF.blit(npcImg,(i*40,j*40))
    DISPLAYSURF.blit(manImg,(x*40,y*40))

    #怪物手册
    if book:
        pygame.draw.rect(DISPLAYSURF,WHITE,(50,50,500,500))
        book1=font2.render('怪物手册：',True,BLACK,WHITE)
        rect11=book1.get_rect()
        rect11.center=(120,80)
        DISPLAYSURF.blit(book1,rect11)

        DISPLAYSURF.blit(mon1Img,(135,120))
        book2=font2.render('生命：30 攻击：3 防御：0',True,BLACK,WHITE)
        rect12=book2.get_rect()
        rect12.center=(330,130)
        DISPLAYSURF.blit(book2,rect12)
        book3=font2.render('金钱：1 伤害：'+str(count(11)),True,BLACK,WHITE)
        rect13=book3.get_rect()
        rect13.center=(380,170)
        DISPLAYSURF.blit(book3,rect13)

        DISPLAYSURF.blit(mon2Img,(135,190))
        book4=font2.render('生命：50 攻击：5 防御：1',True,BLACK,WHITE)
        rect14=book4.get_rect()
        rect14.center=(330,200)
        DISPLAYSURF.blit(book4,rect14)
        book5=font2.render('金钱：2 伤害：'+str(count(12)),True,BLACK,WHITE)
        rect15=book3.get_rect()
        rect15.center=(380,240)
        DISPLAYSURF.blit(book5,rect15)

        DISPLAYSURF.blit(mon3Img,(135,260))
        book6=font2.render('生命：100 攻击：10 防御：2',True,BLACK,WHITE)
        rect16=book6.get_rect()
        rect16.center=(330,270)
        DISPLAYSURF.blit(book6,rect16)
        book7=font2.render('金钱：3 伤害：'+str(count(13)),True,BLACK,WHITE)
        rect17=book7.get_rect()
        rect17.center=(380,310)
        DISPLAYSURF.blit(book7,rect17)

        DISPLAYSURF.blit(mon4Img,(135,330))
        book8=font2.render('生命：50 攻击：17 防御：8',True,BLACK,WHITE)
        rect18=book8.get_rect()
        rect18.center=(330,340)
        DISPLAYSURF.blit(book8,rect18)
        book9=font2.render('金钱：4 伤害：'+str(count(14)),True,BLACK,WHITE)
        rect19=book9.get_rect()
        rect19.center=(380,380)
        DISPLAYSURF.blit(book9,rect19)

        DISPLAYSURF.blit(mon5Img,(135,400))
        book9=font2.render('生命：150 攻击：10 防御：5',True,BLACK,WHITE)
        rect19=book9.get_rect()
        rect19.center=(330,410)
        DISPLAYSURF.blit(book9,rect19)
        book10=font2.render('金钱：5 伤害：'+str(count(15)),True,BLACK,WHITE)
        rect20=book10.get_rect()
        rect20.center=(380,450)
        DISPLAYSURF.blit(book10,rect20)

        DISPLAYSURF.blit(mon6Img,(135,470))
        book11=font2.render('生命：300 攻击：20 防御：8',True,BLACK,WHITE)
        rect21=book11.get_rect()
        rect21.center=(330,480)
        DISPLAYSURF.blit(book11,rect21)
        book12=font2.render('金钱：35 伤害：'+str(count(16)),True,BLACK,WHITE)
        rect22=book12.get_rect()
        rect22.center=(380,520)
        DISPLAYSURF.blit(book12,rect22)
    #行走
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_0]:
        if book==0:
            book=1
            time.sleep(0.2)
        else:
            book=0
            time.sleep(0.2)
    if key_pressed[pygame.K_LEFT]:
        time.sleep(0.06)
        if x>=1:
            judge(now,x-1,y)
            if now[x-1][y]in(0,2,3) and lose==0 and victory==0:
                x-=1
                manImg=leftImg
                text1=0
                text2=0
    if key_pressed[pygame.K_RIGHT]:
        time.sleep(0.06)
        if x<=13:
            judge(now,x+1,y)
            if now[x+1][y]in(0,2,3) and lose==0 and victory==0:
                x+=1
                manImg=rightImg
                text1=0
                text2=0
    if key_pressed[pygame.K_UP]:
        time.sleep(0.06)
        if y>=1:
            judge(now,x,y-1)
            if now[x][y-1]in(0,2,3) and lose==0 and victory==0:
                y-=1
                manImg=upImg
                text1=0
                text2=0
    if key_pressed[pygame.K_DOWN]:
        time.sleep(0.06)
        if y<=13:
            judge(now,x,y+1)
            if now[x][y+1]in(0,2,3) and lose==0 and victory==0:
                y+=1
                manImg=downImg
                text1=0
                text2=0
    if text2: #买
        if money>9 and key_pressed[pygame.K_1]:
            hp+=30
            money-=10
            time.sleep(0.2)
        if money>9 and key_pressed[pygame.K_2]:
            atk+=1
            money-=10
            time.sleep(0.2)
        if money>9 and key_pressed[pygame.K_3]:
            defend+=1
            money-=10
            time.sleep(0.2)
    #重新开始
    if lose or victory:
        if victory:
            DISPLAYSURF.blit(victory1,rect1)
            pygame.mixer.music.load('002.mid')
        else:
            pygame.draw.rect(DISPLAYSURF,WHITE,(640,120,120,40))
            hp1=font2.render('生命：0',True,BLACK,WHITE)
            DISPLAYSURF.blit(hp1,rect6)
            DISPLAYSURF.blit(lose1,rect2)
            pygame.mixer.music.load('001.mid')
        pygame.mixer.music.play()
        pygame.display.update()
        time.sleep(5)
        remap(storey1,storey2,storey3)
        x=7
        y=14
        victory=0
        lose=0
        key=0
        storey=1
        text1=0
        text2=0
        hp=50
        atk=2
        defend=0
        money=0
        manImg=downImg
    if key_pressed[pygame.K_s]:
        save=open('save\\save.bin','wb')
        pickle.dump(map1,save)
        pickle.dump(map2,save)
        pickle.dump(map3,save)
        pickle.dump(x,save)
        pickle.dump(y,save)
        pickle.dump(key,save)
        pickle.dump(storey,save)
        pickle.dump(hp,save)
        pickle.dump(atk,save)
        pickle.dump(defend,save)
        pickle.dump(money,save)
        save.close()
        time.sleep(0.5)
        message='存档成功！'
        text1=1
    if key_pressed[pygame.K_l]:
        if os.path.exists('save\\save.bin'):
            load_s=open('save\\save.bin','rb')
            map1=pickle.load(load_s)
            map2=pickle.load(load_s)
            for i in range(0,15):
                for j in range(0,15):
                    map2[i][j]=storey2[j][i]
            map3=pickle.load(load_s)
            x=pickle.load(load_s)
            y=pickle.load(load_s)
            key=pickle.load(load_s)
            storey=pickle.load(load_s)
            hp=pickle.load(load_s)
            atk=pickle.load(load_s)
            defend=pickle.load(load_s)
            money=pickle.load(load_s)
            victory=0
            lose=0
            text1=0
            text2=0
            manImg=downImg
            load_s.close()
            time.sleep(0.5)
            message='读档成功！'
            text1=1
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
