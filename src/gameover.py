from settings import *
from button import Button

class GameOver:
    def __init__(self, menu_frames, switch_stage, font):
        self.display_surface = pygame.display.set_mode((WINDOWN_WIDTH, WINDOWN_HEIGHT))
        self.switch_stage = switch_stage
        self.setup(menu_frames, font)
        
    def setup(self, menu_frames, font):
        self.new_game_button = Button(WINDOWN_WIDTH / 2 - 90, 300, menu_frames['new_game'], 0.3)
        self.option_button = Button(WINDOWN_WIDTH / 2 - 90, 400, menu_frames['options'], 0.3)
        self.exit = Button(WINDOWN_WIDTH / 2 - 90, 500, menu_frames['exit'], 0.3)
        self.background = menu_frames['background']
        self.gameover = font.render("Game over", True, (0, 0, 0))
        self.gameoverRect = self.gameover.get_rect()
        self.gameoverRect.center = (WINDOWN_WIDTH / 2, 200)
            
    def input(self):
        if self.new_game_button.check_pressed():
            self.switch_stage('level')
        if self.exit.check_pressed():
            self.switch_stage('exit')
        
    def run(self, dt):
        self.display_surface.blit(self.background, (2, 0))
        self.display_surface.blit(self.gameover, self.gameoverRect)
        self.new_game_button.draw(self.display_surface)
        self.option_button.draw(self.display_surface)
        self.exit.draw(self.display_surface)
        self.input()