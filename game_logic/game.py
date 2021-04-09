import pygame
from consts import RED, GREEN

class Player():
    def __init__(self, x, y, name, width=100, height=100, color=RED):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.name = name
        self.update_rect()
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update_rect()

    def update_rect(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def set_color(self, c):
        self.color = c



class Game:
    def __init__(self, id):
        self.players = {}
        self.id_count = 0
        self.id = id

    def add_player(self, current_player: int):
        self.players[current_player] = Player(50, 50, str(current_player))

    def get_player(self, player_id: int) -> Player:
        return self.players[player_id]

    def action(self, player_id: int, data: Player):
        self.players[player_id] = data
