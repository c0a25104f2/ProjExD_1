import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kouka_img = pg.image.load("fig/3.png") #練習3こうかとんsurfaceの作成
    kouka_img = pg.transform.flip(kouka_img,True,False) #練習4 左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr
        screen.blit(bg_img, [-x, 0])#練習5画像を移動
        screen.blit(kouka_img, [300, 200]) #練習4　こうかとんsurfaceを描画
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習6 FPSを変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()