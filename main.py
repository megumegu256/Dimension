import math
import numpy as np
import pygame as pg

def rot(point,rotation):
  
  rotation_x = math.radians(rotation[0]) * -1
  rotation_y = math.radians(rotation[1])
  rotation_z = math.radians(rotation[2]) * -1
  
  rot_x = np.array([
      [1, 0, 0],
      [0, math.cos(rotation_x), -math.sin(rotation_x)],
      [0, math.sin(rotation_x), math.cos(rotation_x)]
  ])
  rot_y = np.array([
      [math.cos(rotation_y), 0, -math.sin(rotation_y)],
      [0, 1, 0],
      [math.sin(rotation_y), 0, math.cos(rotation_y)]
  ])
  rot_z = np.array([
      [math.cos(rotation_z), -math.sin(rotation_z), 0],
      [math.sin(rotation_z), math.cos(rotation_z), 0],
      [0, 0, 1]
  ])
  
  r = np.array([point[0], point[1], point[2]])
  lr = rot_z @ rot_y @ rot_x @ r

  return lr

def vec(r):
    r = str(r)
    return [int(r[0]),int(r[1]),int(r[2])]
  
#-------------------------------------------------------------------------------
def main():
  
  pg.init() 
  pg.display.set_caption('Dimens.io')
  disp_w, disp_h = 1200, 675 # DisplaySize(WindowSize)
  grid = 100 #200>X>50
  screen = pg.display.set_mode((disp_w,disp_h)) 
  clock  = pg.time.Clock()
  exit_flag = False
  exit_code = '000'
  betf = 0
  aftf = 1
  kbd = ""
  kbdtf = 0
  kbdtg = [-1,-1]
  vx = 0
  vy = 0
  vz = 0

  poses = []
  poses.append([1,1,1])

  rotation = [30,30,30]


  while not exit_flag:

    for event in pg.event.get():
      if event.type == pg.QUIT: # ウィンドウ[X]の押下
        exit_flag = True
        exit_code = '001'
      if event.type == pg.KEYDOWN:  # キーの押下
        if event.key == pg.K_ESCAPE:
          exit_flag = True
          exit_code = "002"

        if event.key == pg.K_SPACE:
          if kbd.isascii():
            if kbdtf == 1 : 
              for i in range(len(poses)):
                if kbdtg == [0,i]:
                  poses[i] = []
                  poses[i] = vec(kbd)

              if kbdtg == [1,0]:
                vx = kbd
              if kbdtg == [1,1]:
                vy = kbd
              if kbdtg == [1,2]:
                vz = kbd
              kbd = ""
              kbdtg = [-1,-1]
              kbdtf = 0
            

        if event.key == pg.K_0:
          if kbdtf == 1:
            kbd += "0"
        elif event.key == pg.K_1:
          if kbdtf == 1:
            kbd += "1"
        elif event.key == pg.K_2:
          if kbdtf == 1:
            kbd += "2"
        elif event.key == pg.K_3:
          if kbdtf == 1:
            kbd += "3"
        elif event.key == pg.K_4:
          if kbdtf == 1:
            kbd += "4"
        elif event.key == pg.K_5:
          if kbdtf == 1:
            kbd += "5"
        elif event.key == pg.K_6:
          if kbdtf == 1:
            kbd += "6"
        elif event.key == pg.K_7:
          if kbdtf == 1:
            kbd += "7"
        elif event.key == pg.K_8:
          if kbdtf == 1:
            kbd += "8"
        elif event.key == pg.K_9:
          if kbdtf == 1:
            kbd += "9"
        elif event.key == pg.K_BACKSPACE:
          if kbdtf == 1 and kbd !="":
            kbd = ""

        
      if event.type == pg.MOUSEBUTTONDOWN:
        # 左
        if event.button == 1:
          if disp_w-116 <= event.pos[0] <= disp_w-116+20 and 40 <= event.pos[1] <= 40+20:
            if grid>=100 : grid -=50
          if disp_w-79 <= event.pos[0] <= disp_w-79+20 and 40 <= event.pos[1] <= 40+20:
            if grid<=150 : grid +=50

          if disp_w-90 <= event.pos[0] <= disp_w-90+20 and 120 <= event.pos[1] <= 120+20:
            if betf == 0 : betf = 1
          if disp_w-90 <= event.pos[0] <= disp_w-90+20 and 160 <= event.pos[1] <= 160+20:
            if aftf == 0 : aftf = 1
          if disp_w-70 <= event.pos[0] <= disp_w-70+20 and 120 <= event.pos[1] <= 120+20:
            if betf == 1 : betf = 0
          if disp_w-70 <= event.pos[0] <= disp_w-70+20 and 160 <= event.pos[1] <= 160+20:
            if aftf == 1 : aftf = 0
          

          for i in range(len(poses)):
            if 0 <= event.pos[0] <= 300 and 40*i <= event.pos[1] <= 40*i+20:
              kbdtf = 1
              kbdtg = [0,i]

          if disp_w-200 <= event.pos[0] <= disp_w-200+20 and 400 <= event.pos[1] <= 400+20:
            kbdtf = 1
            kbdtg = [1,0]
          if disp_w-150 <= event.pos[0] <= disp_w-150+20 and 400 <= event.pos[1] <= 400+20:
            kbdtf = 1
            kbdtg = [1,1]
          if disp_w-100 <= event.pos[0] <= disp_w-100+20 and 400 <= event.pos[1] <= 400+20:
            kbdtf = 1
            kbdtg = [1,2]

    screen.fill(pg.Color("#ffffff"))




    Grid_L = pg.Color(0,150,150)
    Grid_S = pg.Color(0,175,175)
    

    font1 = pg.font.SysFont("", int(3*grid/10))
    font2 = pg.font.SysFont("UDデジタル教科書体", 50)
    font3 = pg.font.SysFont("UDデジタル教科書体", 30)
    font4 = pg.font.SysFont("UDデジタル教科書体", 60)

    #グリッド
    pg.draw.line(screen, Grid_L, (disp_w/2,0), (disp_w/2,disp_h), 2)
    pg.draw.line(screen, Grid_L, (0,disp_h/2), (disp_w,disp_h/2), 2)
    

    #原点
    screen.blit(font1.render("0", True, (0,0,0)), (disp_w//2-15, disp_h//2+10))
    #x軸
    for w in range(disp_w//grid//2+1):
      if w != 0:
        pg.draw.line(screen, Grid_S, (w*grid+disp_w//2,0), (w*grid+disp_w//2,disp_h), 1)
        screen.blit(font1.render(f"{int(w)}", True, (0,0,0)), (w*grid-grid/20+disp_w//2, disp_h/2+grid/10))
        pg.draw.line(screen, Grid_S, ((-w*grid+disp_w//2),0), (-w*grid+disp_w//2,disp_h), 1)
        screen.blit(font1.render(f"{int(-w)}", True, (0,0,0)), (-w*grid-grid/20+disp_w//2, disp_h/2+grid/10))
    #y軸
    for h in range(disp_h//grid//2+1):
      #pg.draw.line(screen, Grid_S, (0,h*grid), (disp_w,h*grid), 1)
      if h != 0:
        pg.draw.line(screen, Grid_S, (0,h*grid+disp_h//2), (disp_w,h*grid+disp_h//2), 1)
        screen.blit(font1.render(f"{int(-h)}", True, (0,0,0)), (disp_w/2+grid/10,h*grid-grid/10+disp_h//2))
        pg.draw.line(screen, Grid_S, ((0,-h*grid+disp_h//2)), (disp_w,-h*grid+disp_h//2), 1)
        screen.blit(font1.render(f"{int(h)}", True, (0,0,0)), (disp_w/2+grid/10,-h*grid-grid/10+disp_h//2))

    #点
    for i in range(len(poses)):
      if betf == 1: 
        pg.draw.circle(screen,"green",(poses[i][0]*grid+disp_w/2,disp_h/2-poses[i][1]*grid),5)
        screen.blit(font1.render(f"{i}", True, (0,0,0)), (poses[i][0]*grid+disp_w/2+4,disp_h/2-poses[i][1]*grid-4))
      if aftf == 1:
        pg.draw.circle(screen,"blue",(rot(poses[i],rotation)[0]*grid+disp_w/2,disp_h/2-rot(poses[i],rotation)[1]*grid),5)
        screen.blit(font1.render(f"{i}", True, (0,0,0)), (rot(poses[i],rotation)[0]*grid+disp_w/2+4,disp_h/2-rot(poses[i],rotation)[1]*grid-4))

    #GUI
    pg.draw.rect(screen,"gray",(0,0,250,disp_h))

    #点リスト
    for j in range(len(poses)):
      screen.blit(font3.render(f"{j} -> pos:({poses[j][0]},{poses[j][1]},{poses[j][2]}){poses}", True, (0,0,0)), (10, 40*j+20))


    pg.draw.rect(screen,"gray",(disp_w-250,0,250,disp_h))
    #拡大率
    pg.draw.rect(screen,"green",(disp_w-116, 40,20,20))
    pg.draw.rect(screen,"green",(disp_w-79, 40,20,20))
    screen.blit(font2.render("Zoom:<  >", True, (0,0,0)), (disp_w-220, 30))
    
    #Before,Afterのクリック
    if betf == 0:
      pg.draw.rect(screen,"yellow",(disp_w-90, 120,20,20))
    elif betf == 1:
      pg.draw.rect(screen,"red",(disp_w-70, 120,20,20))
    screen.blit(font2.render("Before: ", True, (0,0,0)), (disp_w-220, 110))


    if aftf == 0:
      pg.draw.rect(screen,"yellow",(disp_w-90, 160,20,20))
    elif aftf == 1:
      pg.draw.rect(screen,"red",(disp_w-70, 160,20,20))
    screen.blit(font2.render("After   : ", True, (0,0,0)), (disp_w-220, 150))

    #回転

    #vx
    screen.blit(font2.render(f"{vx}", True, (0,0,0)), (disp_w-200, 360))
    pg.draw.rect(screen,"green",(disp_w-200,400,20,20))
    #vy
    screen.blit(font2.render(f"{vy}", True, (0,0,0)), (disp_w-150, 360))
    pg.draw.rect(screen,"green",(disp_w-150,400,20,20))
    #vz
    screen.blit(font2.render(f"{vz}", True, (0,0,0)), (disp_w-100, 360))
    pg.draw.rect(screen,"green",(disp_w-100,400,20,20))


    #入力欄
    pg.draw.rect(screen,"#bbccee",(disp_w/2-150,disp_h*5//6,300,50))
    screen.blit(font4.render(f"/{kbd}", True, (0,0,0)), (disp_w/2-150,disp_h*5//6))

    # 画面出力の更新と同期
    pg.display.update()
    clock.tick(30) # 最高速度を 30フレーム/秒 に制限

  # ゲームループ [ここまで]
  pg.quit()
  return exit_code

if __name__ == "__main__":
  code = main()
  print(f'プログラムを「コード{code}」で終了しました。')