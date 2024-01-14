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

  poses = []
  poses.append([[1,1,1],"green"])

  rotation = [45,45,45]


  while not exit_flag:

    for event in pg.event.get():
      if event.type == pg.QUIT: # ウィンドウ[X]の押下
        exit_flag = True
        exit_code = '001'
      if event.type == pg.KEYDOWN:  # キーの押下
        if event.key == pg.K_ESCAPE:
          exit_flag = True
          exit_code = "002"
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
          print('left:', event.pos)

    screen.fill(pg.Color("#ffffff"))




    Grid_L = pg.Color(0,150,150)
    Grid_S = pg.Color(0,175,175)
    

    font1 = pg.font.SysFont("", int(3*grid/10))
    font2 = pg.font.SysFont("UDデジタル教科書体", 50)
    font3 = pg.font.SysFont("UDデジタル教科書体", 25)

    #グリッド
    pg.draw.line(screen, Grid_L, (disp_w/2,0), (disp_w/2,disp_h), 2)
    pg.draw.line(screen, Grid_L, (0,disp_h/2), (disp_w,disp_h/2), 2)
    
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
        pg.draw.circle(screen,"blue",(poses[i][0][0]*grid+disp_w/2,disp_h/2-poses[i][0][1]*grid),5)
        screen.blit(font1.render(f"{i}", True, (0,0,0)), (poses[i][0][0]*grid+disp_w/2+4,disp_h/2-poses[i][0][1]*grid-4))
      if aftf == 1:
        pg.draw.circle(screen,poses[i][1],(rot(poses[i][0],rotation)[0]*grid+disp_w/2,disp_h/2-rot(poses[i][0],rotation)[1]*grid),5)
        screen.blit(font1.render(f"{i}", True, (0,0,0)), (rot(poses[i][0],rotation)[0]*grid+disp_w/2+4,disp_h/2-rot(poses[i][0],rotation)[1]*grid-4))

    #GUI
    pg.draw.rect(screen,"gray",(0,0,250,disp_h))

    for j in range(len(poses)):
      screen.blit(font3.render(f"{j} -> pos:({poses[j][0][0]},{poses[j][0][1]},{poses[j][0][2]}), color:{poses[j][1]}", True, (0,0,0)), (10, 40*j+20))


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
    




    # 画面出力の更新と同期
    pg.display.update()
    clock.tick(30) # 最高速度を 30フレーム/秒 に制限

  # ゲームループ [ここまで]
  pg.quit()
  return exit_code

if __name__ == "__main__":
  code = main()
  print(f'プログラムを「コード{code}」で終了しました。')