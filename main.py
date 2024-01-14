import math
import numpy as np
import pygame as pg



poses = []
poses.append([[1,1,1],"green"])

rotation = [30,0,0]


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


  while not exit_flag:

    for event in pg.event.get():
      if event.type == pg.QUIT: # ウィンドウ[X]の押下
        exit_flag = True
        exit_code = '001'
      if event.type == pg.KEYDOWN:  # キーの押下
        if event.key == pg.K_ESCAPE:
          exit_flag = True
          exit_code = "002"

    screen.fill(pg.Color("#ffffff"))



    Blue = pg.Color(0,50,200)
    Red = pg.Color(200,50,200)
    Black = pg.Color(0,0,0)
    Grid_L = pg.Color(0,150,150)
    Grid_S = pg.Color(0,175,175)
    

    font1 = pg.font.SysFont("", int(3*grid/10))
    font2 = pg.font.SysFont("UDデジタル教科書体", 50)

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
      pg.draw.circle(screen,"blue",(poses[i][0][0]*grid+disp_w/2,disp_h/2-poses[i][0][1]*grid),5)
      pg.draw.circle(screen,poses[i][1],(rot(poses[i][0],rotation)[0]*grid+disp_w/2,disp_h/2-rot(poses[i][0],rotation)[1]*grid),5)

    #GUI
    pg.draw.rect(screen,"gray",(0,0,250,disp_h))

    pg.draw.rect(screen,"gray",(disp_w-250,0,250,disp_h))
    screen.blit(font2.render("Zoom:", True, (0,0,0)), (disp_w-220, 30))




    # 画面出力の更新と同期
    pg.display.update()
    clock.tick(30) # 最高速度を 30フレーム/秒 に制限

  # ゲームループ [ここまで]
  pg.quit()
  return exit_code

if __name__ == "__main__":
  code = main()
  print(f'プログラムを「コード{code}」で終了しました。')