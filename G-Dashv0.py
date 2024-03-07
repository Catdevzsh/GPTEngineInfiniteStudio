import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Geometry Dash")
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

player_size = 20
player_color = red

obstacle_width = 50
obstacle_height = 20
obstacle_color = black

class Player:
    def __init__(self):
        self.x = 50
        self.y = screen_height // 2 - player_size // 2
        self.y_vel = 0
        self.is_jumping = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.y_vel = -10
            self.is_jumping = True

        self.y += self.y_vel
        self.y_vel += 0.5  # Gravity

        if self.y + player_size >= screen_height:
            self.y = screen_height - player_size
            self.y_vel = 0
            self.is_jumping = False

    def draw(self):
        pygame.draw.rect(screen, player_color, (self.x, self.y, player_size, player_size))

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        self.x -= 5  # Move obstacles to the left

    def draw(self):
        pygame.draw.rect(screen, obstacle_color, (self.x, self.y, obstacle_width, obstacle_height))

player = Player()
obstacles = []
obstacle_spawn_timer = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    player.update()
    player.draw()

    obstacle_spawn_timer += 1
    if obstacle_spawn_timer >= 100:
        obstacles.append(Obstacle(screen_width, screen_height - obstacle_height))
        obstacle_spawn_timer = 0

    for obstacle in obstacles:
        obstacle.update()
        obstacle.draw()

        if player.x + player_size >= obstacle.x and player.x <= obstacle.x + obstacle_width:
            if player.y + player_size >= obstacle.y:
                print("Game Over!")
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
