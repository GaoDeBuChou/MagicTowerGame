#!/usr/bin/env python3
import os
import sys
import time
import pickle
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (230, 230, 230)
BLUE = (0, 0, 125)
RED = (150, 0, 0)
WALL_COLOR = (75, 40, 40)

STOREY1 = [[4, 1, 4, 1, 0, 0, 1, 2, 1, 0, 1, 0, 7, 0, 5],
           [13, 0, 12, 0, 0, 0, 1, 12, 1, 0, 1, 13, 0, 7, 0],
           [1, 1, 1, 1, 0, 0, 1, 6, 1, 0, 1, 6, 1, 1, 1],
           [0, 8, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
           [8, 0, 13, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
           [1, 1, 6, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 4],
           [0, 11, 0, 6, 0, 1, 5, 5, 5, 1, 0, 0, 11, 11, 10],
           [8, 11, 11, 1, 0, 1, 11, 12, 11, 1, 0, 0, 1, 0, 4],
           [4, 7, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
           [1, 1, 1, 1, 0, 1, 1, 11, 1, 1, 0, 0, 0, 1, 7],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [6, 1, 1, 1, 0, 0, 0, 11, 0, 0, 0, 1, 1, 1, 1],
           [12, 0, 0, 1, 0, 1, 1, 6, 1, 1, 0, 0, 0, 0, 21],
           [0, 8, 7, 1, 0, 1, 0, 0, 5, 1, 0, 1, 1, 1, 1],
           [0, 8, 7, 1, 4, 1, 0, 0, 0, 1, 0, 0, 0, 0, 22]]
STOREY2 = [[4, 4, 0, 1, 7, 1, 0, 3, 0, 1, 7, 1, 4, 4, 4],
           [4, 4, 0, 1, 7, 1, 4, 4, 4, 1, 7, 1, 4, 7, 4],
           [0, 0, 14, 1, 13, 1, 1, 0, 1, 1, 0, 1, 8, 5, 8],
           [1, 1, 6, 1, 0, 1, 23, 0, 0, 0, 0, 1, 1, 6, 1],
           [5, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 5, 15, 5],
           [1, 1, 1, 1, 0, 1, 4, 1, 5, 1, 0, 1, 0, 8, 0],
           [0, 13, 5, 1, 0, 1, 0, 1, 0, 6, 5, 1, 0, 14, 0],
           [13, 1, 1, 1, 0, 1, 0, 1, 5, 1, 0, 1, 1, 6, 1],
           [0, 1, 13, 13, 0, 1, 14, 1, 1, 1, 0, 1, 12, 12, 12],
           [13, 1, 15, 1, 0, 0, 0, 0, 0, 0, 0, 1, 12, 12, 12],
           [0, 0, 0, 1, 0, 1, 1, 6, 1, 1, 0, 1, 12, 12, 12],
           [1, 1, 6, 1, 0, 1, 0, 13, 0, 1, 0, 1, 1, 6, 1],
           [4, 0, 7, 1, 0, 1, 0, 4, 0, 1, 0, 0, 0, 0, 8],
           [0, 4, 0, 1, 0, 1, 12, 12, 12, 1, 0, 1, 1, 1, 1],
           [8, 0, 4, 1, 5, 1, 7, 0, 7, 1, 0, 14, 15, 6, 2]]
STOREY3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 16, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 3]]

UP_Img = pygame.image.load("img/up.jpg")
DOWN_Img = pygame.image.load("img/down.jpg")
LEFT_Img = pygame.image.load("img/left.jpg")
RIGHT_Img = pygame.image.load("img/right.jpg")
STAR_Img = pygame.image.load("img/star.jpg")
KEY_Img = pygame.image.load("img/key.jpg")
DOOR_Img = pygame.image.load("img/door.jpg")
MON1_Img = pygame.image.load("img/monster1.jpg")
MON2_Img = pygame.image.load("img/monster2.jpg")
MON3_Img = pygame.image.load("img/monster3.jpg")
MON4_Img = pygame.image.load("img/monster4.jpg")
MON5_Img = pygame.image.load("img/monster5.jpg")
MON6_Img = pygame.image.load("img/monster6.jpg")
SHOP_Img = pygame.image.load("img/shop.jpg")
UPS_Img = pygame.image.load("img/upstairs.jpg")
DOWNS_Img = pygame.image.load("img/downstairs.jpg")
NPC_Img = pygame.image.load("img/smile.jpg")
BLOOD_Img = pygame.image.load("img/blood.jpg")

MONSTERS = [
    {"img": MON1_Img, "hp": 15, "atk": 3, "def": 0, "money": 1},
    {"img": MON2_Img, "hp": 50, "atk": 5, "def": 1, "money": 2},
    {"img": MON3_Img, "hp": 100, "atk": 10, "def": 2, "money": 3},
    {"img": MON4_Img, "hp": 50, "atk": 17, "def": 8, "money": 4},
    {"img": MON5_Img, "hp": 150, "atk": 10, "def": 5, "money": 5},
    {"img": MON6_Img, "hp": 300, "atk": 20, "def": 8, "money": 35}
]


def count(monster):
    """
    Calculate reduction of hp in battle
    :param monster: type of monster
    :return: reduction of hp
    """
    global atk, defend, MONSTERS
    monster_hp = MONSTERS[monster - 11]["hp"]
    monster_atk = MONSTERS[monster - 11]["atk"] if monster != 15 else defend + 10
    monster_def = MONSTERS[monster - 11]["def"]
    if atk <= monster_def:
        return 9999
    if monster_atk <= defend:
        return 0
    if monster_hp % (atk - monster_def) == 0:
        return int((monster_hp / (atk - monster_def) - 1) * (monster_atk - defend))
    else:
        return int((monster_hp // (atk - monster_def)) * (monster_atk - defend))


def battle(monster):
    """
    Battle
    :param monster: type of monster
    :return: True if monster is defeated; False otherwise
    """
    global hp, money
    hp = hp - count(monster)
    if hp <= 0:
        return False
    money += MONSTERS[monster - 11]["money"]
    return True


def judge(nw, a, b):
    """
    Events: 0 empty, 1 wall, 2 upstairs, 3 downstairs, 4 add blood, 5 key, 6 door, 7 add atk, 8 add defend,
            9 victory star, 10 shop, 11-20 monster, 21+ NPC dialog
    :param nw: current situation
    :param a: horizontal index
    :param b: vertical index
    """
    global x, y, key, victory, lose, storey, text1, text2, hp, atk, defend, msg, msg0
    if nw[a][b] == 2:
        storey += 1
    elif nw[a][b] == 3:
        storey -= 1
    elif nw[a][b] == 4:
        hp += 30
        pygame.mixer.music.load("aud/get.mp3")
        pygame.mixer.music.play()
        nw[a][b] = 0
    elif nw[a][b] == 5:
        key += 1
        pygame.mixer.music.load("aud/get.mp3")
        pygame.mixer.music.play()
        nw[a][b] = 0
    elif nw[a][b] == 6:
        if key > 0:
            key -= 1
            nw[a][b] = 0
    elif nw[a][b] == 7:
        pygame.mixer.music.load("aud/get.mp3")
        pygame.mixer.music.play()
        atk += 1
        nw[a][b] = 0
    elif nw[a][b] == 8:
        pygame.mixer.music.load("aud/get.mp3")
        pygame.mixer.music.play()
        defend += 1
        nw[a][b] = 0
    elif nw[a][b] == 9:
        victory = True
    elif nw[a][b] == 10:
        msg, msg0 = "10金币可交换：(1)30生命", "(2)1攻击 (3)1防御"
        text1, text2 = True, True
    elif 10 < nw[a][b] < 21:
        pygame.mixer.music.load("aud/atk.mp3")
        pygame.mixer.music.play()
        if battle(nw[a][b]):
            nw[a][b] = 0
        else:
            lose = True
    elif nw[a][b] > 20:
        if nw[a][b] == 21:
            msg = "按0可打开怪物手册"
        elif nw[a][b] == 22:
            msg = "战斗为回合制，攻防决定伤害"
        elif nw[a][b] == 23:
            msg = "法师攻击无视你的防御"
        text1 = True


def remap():
    """
    Reset maps
    """
    global maps
    maps[0] = [[STOREY1[j][i] for j in range(15)] for i in range(15)]
    maps[1] = [[STOREY2[j][i] for j in range(15)] for i in range(15)]
    maps[2] = [[STOREY3[j][i] for j in range(15)] for i in range(15)]


def draw_book(monster, hor, ver):
    """
    Draw information on monster book
    :param monster: type of monster
    :param hor: horizontal place
    :param ver: vertical place
    """
    mst = MONSTERS[monster - 11]
    DISPLAYSURF.blit(mst["img"], (hor, ver))
    book_m1 = font2.render("生命：" + str(mst["hp"]) + " 攻击：" + str(mst["atk"]) + " 防御：" + str(mst["def"]),
                           True, BLACK, WHITE)
    rect_m1 = book_m1.get_rect()
    rect_m1.center = (hor + 195, ver + 10)
    DISPLAYSURF.blit(book_m1, rect_m1)
    book_m2 = font2.render("金钱：" + str(mst["money"]) + " 伤害：" + str(count(monster)), True, BLACK, WHITE)
    rect_m2 = book_m2.get_rect()
    rect_m2.center = (hor + 245, ver + 40)
    DISPLAYSURF.blit(book_m2, rect_m2)


def draw7(i, j):
    """
    Draw add atk (red) diamond
    :param i: horizontal index
    :param j: vertical index
    """
    pygame.draw.rect(DISPLAYSURF, GREY, (i * 40, j * 40, 40, 40))
    pygame.draw.polygon(DISPLAYSURF, RED, ((i * 40 + 20, j * 40 + 10), (i * 40 + 10, j * 40 + 20),
                                           (i * 40 + 20, j * 40 + 30), (i * 40 + 30, j * 40 + 20)))


def draw8(i, j):
    """
    Draw add defend (blue) diamond
    :param i: horizontal index
    :param j: vertical index
    :return:
    """
    pygame.draw.rect(DISPLAYSURF, GREY, (i * 40, j * 40, 40, 40))
    pygame.draw.polygon(DISPLAYSURF, BLUE, ((i * 40 + 20, j * 40 + 10), (i * 40 + 10, j * 40 + 20),
                                            (i * 40 + 20, j * 40 + 30), (i * 40 + 30, j * 40 + 20)))


draws = [  # list of drawing functions
    lambda i, j: pygame.draw.rect(DISPLAYSURF, GREY, (i * 40, j * 40, 40, 40)),
    lambda i, j: pygame.draw.rect(DISPLAYSURF, WALL_COLOR, (i * 40, j * 40, 40, 40)),
    lambda i, j: DISPLAYSURF.blit(UPS_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(DOWNS_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(BLOOD_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(KEY_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(DOOR_Img, (i * 40, j * 40)),
    draw7,
    draw8,
    lambda i, j: DISPLAYSURF.blit(STAR_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(SHOP_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(MON1_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(MON2_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(MON3_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(MON4_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(MON5_Img, (i * 40, j * 40)),
    lambda i, j: DISPLAYSURF.blit(MON6_Img, (i * 40, j * 40))
]

if __name__ == "__main__":
    pygame.init()
    FPS = 30
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption("Magic Tower Game（S存档，L读档）")

    font1 = pygame.font.Font("freesansbold.ttf", 20)
    font2 = pygame.font.SysFont("simsunnsimsun", 20)
    font3 = pygame.font.SysFont("simsunnsimsun", 16)
    victory1 = font1.render("Congratulations!", True, RED, GREY)
    rect1 = victory1.get_rect()
    rect1.center = (400, 300)
    lose1 = font1.render("Game Over!", True, RED, GREY)
    rect2 = lose1.get_rect()
    rect2.center = (400, 300)
    key1 = font1.render("× 0", True, RED, WHITE)
    rect3 = key1.get_rect()
    rect3.center = (720, 470)
    floor1 = font2.render("1楼", True, BLACK, WHITE)
    rect4 = floor1.get_rect()
    rect4.center = (700, 100)
    msg = ""
    message1 = font3.render(msg, True, BLACK, WHITE)
    rect5 = message1.get_rect()
    rect5.center = (700, 520)
    hp1 = font2.render("生命：50", True, BLACK, WHITE)
    rect6 = hp1.get_rect()
    rect6.center = (700, 140)
    atk1 = font2.render("攻击：2", True, BLACK, WHITE)
    rect7 = atk1.get_rect()
    rect7.center = (700, 180)
    def1 = font2.render("防御：0", True, BLACK, WHITE)
    rect8 = def1.get_rect()
    rect8.center = (700, 220)
    money1 = font2.render("金钱：0", True, BLACK, WHITE)
    rect9 = money1.get_rect()
    rect9.center = (700, 260)
    msg0 = ""
    message2 = font3.render(msg0, True, BLACK, WHITE)
    rect10 = message2.get_rect()
    rect10.center = (700, 540)

    maps = [[[STOREY1[j][i] for j in range(15)] for i in range(15)],
            [[STOREY2[j][i] for j in range(15)] for i in range(15)],
            [[STOREY3[j][i] for j in range(15)] for i in range(15)]]
    x, y, key, victory, lose, storey, text1, text2 = 7, 14, 0, False, False, 1, False, False
    hp, atk, defend, money, book, manImg = 50, 2, 0, 0, False, DOWN_Img

    while True:
        # Draw interface
        DISPLAYSURF.fill(WHITE)
        pygame.draw.line(DISPLAYSURF, BLACK, (600, 0), (600, 600), 5)
        DISPLAYSURF.blit(KEY_Img, (650, 450))
        key1 = font1.render("× " + str(key), True, RED, WHITE)
        DISPLAYSURF.blit(key1, rect3)
        floor1 = font2.render(str(storey) + "楼", True, BLACK, WHITE)
        DISPLAYSURF.blit(floor1, rect4)
        hp1 = font2.render("生命：" + str(hp), True, BLACK, WHITE)
        DISPLAYSURF.blit(hp1, rect6)
        atk1 = font2.render("攻击：" + str(atk), True, BLACK, WHITE)
        DISPLAYSURF.blit(atk1, rect7)
        def1 = font2.render("防御：" + str(defend), True, BLACK, WHITE)
        DISPLAYSURF.blit(def1, rect8)
        money1 = font2.render("金钱：" + str(money), True, BLACK, WHITE)
        DISPLAYSURF.blit(money1, rect9)
        if text1:
            message1 = font3.render(msg, True, BLACK, WHITE)
            rect5 = message1.get_rect()
            rect5.center = (700, 520)
            DISPLAYSURF.blit(message1, rect5)
        if text2:
            message2 = font3.render(msg0, True, BLACK, WHITE)
            rect10 = message2.get_rect()
            rect10.center = (700, 540)
            DISPLAYSURF.blit(message2, rect10)

        # Draw map
        now = maps[storey - 1]
        for i in range(15):
            for j in range(15):
                if now[i][j] > 20:
                    DISPLAYSURF.blit(NPC_Img, (i * 40, j * 40))
                else:
                    draws[now[i][j]](i, j)
        DISPLAYSURF.blit(manImg, (x * 40, y * 40))

        # monster book
        if book:
            pygame.draw.rect(DISPLAYSURF, WHITE, (50, 50, 500, 500))
            book1 = font2.render("怪物手册：", True, BLACK, WHITE)
            rect11 = book1.get_rect()
            rect11.center = (120, 80)
            DISPLAYSURF.blit(book1, rect11)
            draw_book(11, 135, 120)
            draw_book(12, 135, 190)
            draw_book(13, 135, 260)
            draw_book(14, 135, 330)
            draw_book(15, 135, 400)
            draw_book(16, 135, 470)

        # Move
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_0]:
            book = not book
            time.sleep(0.2)
        if key_pressed[pygame.K_LEFT]:
            time.sleep(0.06)
            if x >= 1:
                judge(now, x - 1, y)
                if now[x - 1][y] in (0, 2, 3) and not lose and not victory:
                    x -= 1
                    text1, text2, manImg = False, False, LEFT_Img
        if key_pressed[pygame.K_RIGHT]:
            time.sleep(0.06)
            if x <= 13:
                judge(now, x + 1, y)
                if now[x + 1][y] in (0, 2, 3) and not lose and not victory:
                    x += 1
                    text1, text2, manImg = False, False, RIGHT_Img
        if key_pressed[pygame.K_UP]:
            time.sleep(0.06)
            if y >= 1:
                judge(now, x, y - 1)
                if now[x][y - 1] in (0, 2, 3) and not lose and not victory:
                    y -= 1
                    text1, text2, manImg = False, False, UP_Img
        if key_pressed[pygame.K_DOWN]:
            time.sleep(0.06)
            if y <= 13:
                judge(now, x, y + 1)
                if now[x][y + 1] in (0, 2, 3) and not lose and not victory:
                    y += 1
                    text1, text2, manImg = False, False, DOWN_Img
        if text2:  # Buy
            if money > 9 and key_pressed[pygame.K_1]:
                hp += 30
                money -= 10
                time.sleep(0.2)
            if money > 9 and key_pressed[pygame.K_2]:
                atk += 1
                money -= 10
                time.sleep(0.2)
            if money > 9 and key_pressed[pygame.K_3]:
                defend += 1
                money -= 10
                time.sleep(0.2)

        if lose or victory or key_pressed[pygame.K_r]:  # restart
            if victory:
                DISPLAYSURF.blit(victory1, rect1)
                pygame.mixer.music.load("aud/002.mid")
                pygame.mixer.music.play()
            if lose:
                pygame.draw.rect(DISPLAYSURF, WHITE, (640, 120, 120, 40))
                hp1 = font2.render("生命：0", True, BLACK, WHITE)
                DISPLAYSURF.blit(hp1, rect6)
                DISPLAYSURF.blit(lose1, rect2)
                pygame.mixer.music.load("aud/001.mid")
                pygame.mixer.music.play()
            pygame.display.update()
            time.sleep(5)
            remap()
            x, y, key, victory, lose, storey, text1, text2 = 7, 14, 0, False, False, 1, False, False
            hp, atk, defend, money, book, manImg = 50, 2, 0, 0, False, DOWN_Img

        if key_pressed[pygame.K_s]:  # save
            if not os.path.isdir("save"):
                os.mkdir("save")
            with open("save/save.bin", "wb") as save:
                pickle.dump(maps, save)
                pickle.dump(x, save)
                pickle.dump(y, save)
                pickle.dump(key, save)
                pickle.dump(storey, save)
                pickle.dump(hp, save)
                pickle.dump(atk, save)
                pickle.dump(defend, save)
                pickle.dump(money, save)
            time.sleep(0.5)
            msg = "存档成功！"
            text1, text2 = True, False

        if key_pressed[pygame.K_l]:  # load
            if os.path.isfile("save/save.bin"):
                with open("save/save.bin", "rb") as load:
                    maps = pickle.load(load)
                    x, y, key, storey = pickle.load(load), pickle.load(load), pickle.load(load), pickle.load(load)
                    hp, atk, defend, money = pickle.load(load), pickle.load(load), pickle.load(load), pickle.load(load)
                time.sleep(0.5)
                msg = "读档成功！"
                victory, lose, text1, text2 = False, False, True, False
                manImg = DOWN_Img

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
