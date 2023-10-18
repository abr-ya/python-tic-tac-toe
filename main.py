import pygame as pg
import sys

WIN_SIZE = 600
CELL_SIZE = WIN_SIZE // 3
INF = float('inf')
vec2 = pg.math.Vector2
CELL_CENTER = vec2(CELL_SIZE / 2)

class TicTacToe:
  def __init__(self, game):
    self.game = game
    self.field_image = self.get_scaled_image(path='img/field.png', res=[WIN_SIZE] * 2)
    self.O_image = self.get_scaled_image(path='img/o.png', res=[CELL_SIZE] * 2)
    self.X_image = self.get_scaled_image(path='img/x.png', res=[CELL_SIZE] * 2)

    self.game_array = [[INF, INF, INF],
                      [INF, INF, INF],
                      [INF, INF, INF]]
    self.player = 1 # стартовый/текущий игрок

    self.winner = None
    self.game_steps = 0

  def  draw_signs(self):
    for y, row in enumerate(self.game_array):
      for x, sign in enumerate(row):
        if sign != INF:
          self.game.screen.blit((self.X_image, self.O_image)[sign], vec2(x, y) * CELL_SIZE)

  def draw(self):
    self.game.screen.blit(self.field_image, (0, 0))
    self. draw_signs()
    # self.draw_winner()

  @staticmethod
  def get_scaled_image(path, res):
    img = pg.image.load(path)
    return pg.transform.smoothscale(img, res)
  
  # делаем ход!)
  def run_game_process(self):
    current_cell = vec2(pg.mouse.get_pos()) // CELL_SIZE
    col, row = map(int, current_cell)
    left_click = pg.mouse.get_pressed()[0]

    if left_click and self.game_array[row][col] == INF and not self.winner:
      self.game_array[row][col] = self.player
      self.player = not self.player

  def print_caption(self):
    pg.display.set_caption(f'Player "{("X", "O")[self.player]}" turn!')

  def run(self):
    self.print_caption()
    self.draw()
    self.run_game_process()

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