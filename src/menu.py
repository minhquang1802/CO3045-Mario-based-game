from settings import *
from button import Button

class Menu:
    def __init__(self, menu_frames, switch_stage):
        self.display_surface = pygame.display.set_mode((WINDOWN_WIDTH, WINDOWN_HEIGHT))
        self.switch_stage = switch_stage
        self.setup(menu_frames)
        
    def setup(self, menu_frames):
        self.new_game_button = Button(WINDOWN_WIDTH / 2 - 150, 125, menu_frames['new_game'], 0.5)
        self.option_button = Button(WINDOWN_WIDTH / 2 - 150, 325, menu_frames['options'], 0.5)
        self.exit = Button(WINDOWN_WIDTH / 2 - 150, 525, menu_frames['exit'], 0.5)
        self.background = menu_frames['background']
            
    def input(self):
        if self.new_game_button.check_pressed():
            self.switch_stage('level')
        if self.exit.check_pressed():
            self.switch_stage('exit')
        
    def run(self, dt):
        self.display_surface.blit(self.background, (2, 0))
        self.new_game_button.draw(self.display_surface)
        self.option_button.draw(self.display_surface)
        self.exit.draw(self.display_surface)
        self.input()