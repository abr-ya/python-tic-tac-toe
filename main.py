import pygame as pg
import sys

WIN_SIZE = 600
CELL_SIZE = WIN_SIZE // 3
INF = float('inf')

class TicTacToe:
  def __init__(self, game):
    self.game = game
    self.field_image = self.get_scaled_image(path='img/field.png', res=[WIN_SIZE] * 2)
    self.O_image = self.get_scaled_image(path='img/o.png', res=[CELL_SIZE] * 2)
    self.X_image = self.get_scaled_image(path='img/x.png', res=[CELL_SIZE] * 2)

  def draw(self):
    self.game.screen.blit(self.field_image, (0, 0))
    # self.draw_objects()
    # self.draw_winner()

  @staticmethod
  def get_scaled_image(path, res):
    img = pg.image.load(path)
    return pg.transform.smoothscale(img, res)

  def run(self):
    self.draw()

class Game:
  def __init__(self):
    pg.init()
    self.screen = pg.display.set_mode([WIN_SIZE] * 2)
    self.clock = pg.time.Clock()
    self.tic_tac_toe = TicTacToe(self)

  def new_game(self):
    pass

  def check_events(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()

  def run(self):
    while True: # чтобы не захлопывалось окно!
      self.tic_tac_toe.run() # экземпляр игры
      self.check_events() # события
      pg.display.update() # обновления экрана
      self.clock.tick(60) # framerate


if __name__ == '__main__':
  game = Game()
  game.run()