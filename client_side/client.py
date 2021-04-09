import pygame

from consts import RED, GREEN
from network.network import Network
import pickle

pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def redrawWindow(win, game, player_id):
    win.fill((128, 128, 128))
    for p_id in game.players:
        if p_id == player_id:
            p = game.get_player(p_id)
            p.set_color(GREEN)
        else:
            p = game.get_player(p_id)
            p.set_color(RED)
        game.get_player(p_id).draw(win)

        for btn in btns:
            btn.draw(win)

    pygame.display.update()


btns = [Button("Rock", 50, 500, (0, 0, 0)), Button("Scissors", 250, 500, (255, 0, 0)),
        Button("Paper", 450, 500, (0, 255, 0))]


def main():
    run = True

    clock = pygame.time.Clock()
    n = Network()

    while run:
        clock.tick(60)
        try:
            game_state = n.send("get")
            game, player_id = game_state
        except:
            run = False
            print("Couldn't get game")
            break

        if game:
            redrawWindow(win, game, player_id)
            pygame.display.update()
            pygame.time.delay(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player = game.get_player(player_id)
        player.move()

        n.send(player)


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255, 0, 0))
        win.blit(text, (100, 200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True:
    menu_screen()
