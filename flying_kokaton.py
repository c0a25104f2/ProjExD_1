import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)#練習8 背景画像の背景反転
    kouka_img = pg.image.load("fig/3.png") #練習3こうかとんsurfaceの作成
    kouka_img = pg.transform.flip(kouka_img,True,False) #練習4 左右反転
    kouka_rct = kouka_img.get_rect()#練習10 rect作成
    kouka_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        #練習10　矢印キーで動く処理を決めている
        #画像は下方向が＋上方向が-
        n = 0
        m = 0
        kouka_rct.move_ip((n, m))
        if key_lst[pg.K_UP]:
           m = -1
        if key_lst[pg.K_DOWN]:
           m = +1
        if key_lst[pg.K_LEFT]:
           n = -1
        else:
           n = -1
        if key_lst[pg.K_RIGHT]:
           n = +1
        
        
        kouka_rct.move_ip((n, m))
            
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])#練習5画像を移動
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        # screen.blit(kouka_img, [300, 200]) #練習4　こうかとんsurfaceを描画
        screen.blit(kouka_img, kouka_rct)#練習10　rectを画面に貼り付ける
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習6 FPSを変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()