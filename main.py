import pygame
import random
import sys
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Mushroom Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Levels configuration
levels = {
    "Easy": {"speed": 2, "time": 60},
    "Medium": {"speed": 4, "time": 45},
    "Hard": {"speed": 6, "time": 30},
}

# Function to display the menu
def show_menu():
    selected_level = None
    while True:
        screen.fill(WHITE)

        # Title
        title_text = font.render("Select Game Level", True, BLACK)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        # Level buttons
        y_offset = 200
        level_rects = {}
        for level, config in levels.items():
            level_rect = pygame.Rect(WIDTH // 2 - 100, y_offset, 200, 50)
            pygame.draw.rect(screen, GRAY, level_rect)
            level_text = small_font.render(level, True, BLACK)
            screen.blit(level_text, (level_rect.x + level_rect.width // 2 - level_text.get_width() // 2, level_rect.y + 10))
            level_rects[level] = level_rect
            y_offset += 100

        # Check for mouse click
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for level, rect in level_rects.items():
                    if rect.collidepoint(event.pos):
                        selected_level = level
                        break

        if selected_level:
            break

        # Update display
        pygame.display.flip()

    return selected_level


def show_game_over(hearts):
    screen.fill(WHITE)
    end_message = "You Win!" if hearts > 0 else "Game Over!"
    end_text = font.render(end_message, True, BLACK)
    screen.blit(end_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))

    # Restart button
    restart_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
    pygame.draw.rect(screen, GRAY, restart_button_rect)
    restart_text = small_font.render("Restart", True, BLACK)
    screen.blit(restart_text, (restart_button_rect.x + restart_button_rect.width // 2 - restart_text.get_width() // 2, restart_button_rect.y + 10))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart_button_rect.collidepoint(event.pos):
                    return True
        pygame.time.wait(100)

def play_game(level_config):
    player_pos = [WIDTH // 2, HEIGHT // 2]
    player_speed = 5
    pacman_img = pygame.image.load("sprites/pacman.png")
    pacman_img = pygame.transform.scale(pacman_img, (50, 50))
    pacman = pacman_img
    hearts = 5
    start_time = pygame.time.get_ticks()
    game_duration = level_config["time"]

    # Mushrooms
    red_mushroom_img = pygame.image.load("sprites/red-mushroom.png")
    pink_mushroom_img = pygame.image.load("sprites/pink-mushroom.png")
    blue_mushroom_img = pygame.image.load("sprites/blue-mushroom.png")
    mushrooms = [
        {"image": pygame.transform.scale(red_mushroom_img, (30, 30)), "type": "red", "pos": [random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30)], "speed": [level_config["speed"], level_config["speed"]]},
        {"image": pygame.transform.scale(pink_mushroom_img, (30, 30)), "type": "pink", "pos": [random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30)], "speed": [0, 0]},
        {"image": pygame.transform.scale(blue_mushroom_img, (30, 30)), "type": "blue", "pos": [random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30)], "speed": [0, 0]},
    ]

    # Clock for controlling frame rate
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Check for game end conditions
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        if elapsed_time > game_duration or hearts <= 0:
            running = False
            continue

        # Get keys for movement
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            player_pos[0] -= player_speed
            pacman = pygame.transform.rotate(pacman_img, 180)
        if keys[K_RIGHT]:
            player_pos[0] += player_speed
            pacman = pygame.transform.rotate(pacman_img, 0)
        if keys[K_UP]:
            player_pos[1] -= player_speed
            pacman = pygame.transform.rotate(pacman_img, 90)
        if keys[K_DOWN]:
            player_pos[1] += player_speed
            pacman = pygame.transform.rotate(pacman_img, 270)

        # Boundary check for player
        player_pos[0] = max(0, min(player_pos[0], WIDTH - 50))
        player_pos[1] = max(0, min(player_pos[1], HEIGHT - 50))

        # Draw player
        screen.blit(pacman, player_pos)

        # Draw mushrooms and handle interactions
        for mushroom in mushrooms:
            mushroom_rect = pygame.Rect(*mushroom["pos"], 30, 30)
            pacman_rect = pygame.Rect(*player_pos, 50, 50)

            # Draw mushroom
            screen.blit(mushroom["image"], mushroom["pos"])

            # Move red mushroom
            if mushroom["type"] == "red":
                mushroom["pos"][0] += mushroom["speed"][0]
                mushroom["pos"][1] += mushroom["speed"][1]

                # Bounce on borders
                if mushroom["pos"][0] <= 0 or mushroom["pos"][0] >= WIDTH - 30:
                    mushroom["speed"][0] = -mushroom["speed"][0]
                if mushroom["pos"][1] <= 0 or mushroom["pos"][1] >= HEIGHT - 30:
                    mushroom["speed"][1] = -mushroom["speed"][1]

            # Check collision
            if pacman_rect.colliderect(mushroom_rect):
                if mushroom["type"] == "red":
                    hearts -= 1
                elif mushroom["type"] == "pink":
                    hearts -= 0.5
                elif mushroom["type"] == "blue":
                    hearts += 1

                # Relocate mushroom after collision
                mushroom["pos"] = [random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30)]

        # Draw hearts
        for i in range(int(hearts)):
            pygame.draw.circle(screen, BLUE, (20 + i * 25, 20), 10)

        # Display timer
        time_left = max(0, game_duration - int(elapsed_time))
        timer_text = small_font.render(f"Time: {time_left}s", True, BLACK)
        screen.blit(timer_text, (WIDTH - 150, 10))

        # Update display
        pygame.display.flip()
        clock.tick(30)

    # Show game over screen and check for restart
    if show_game_over(hearts):
        play_game(level_config)

# Run the menu and start the game
selected_level = show_menu()
play_game(levels[selected_level])
pygame.quit()
