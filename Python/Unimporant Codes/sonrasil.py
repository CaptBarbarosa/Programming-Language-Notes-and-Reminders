import pgzrun
import random
from math import sin, cos
from pygame import Rect

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Game settings
TITLE = "Roguelike Adventure"
background_music = "background.mp3"
footstep_sound = "footstep.wav"
collision_sound = "collision.wav"
music_enabled = True

# Game objects
hero = Actor("hero_idle", (WIDTH // 2, HEIGHT // 2))
hero.speed = 3
hero.animation_frame = 0
hero.frame_count = 4  # Number of animation frames for hero

enemies = []
for _ in range(3):
    x, y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    enemy = Actor("enemy_idle", (x, y))
    enemy.speed = 2
    enemy.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
    enemies.append(enemy)

# Menu states
menu_active = True

# Button positions
buttons = {
    "start": Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 50),
    "toggle_music": Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50),
    "exit": Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50),
}

# Toggle music
def toggle_music():
    global music_enabled
    music_enabled = not music_enabled
    if music_enabled:
        music.play(background_music)
    else:
        music.stop()

# Draw function
def draw():
    if menu_active:
        screen.clear()
        screen.fill("black")
        screen.draw.text("Roguelike Adventure", center=(WIDTH // 2, 100), fontsize=50, color="white")
        for name, rect in buttons.items():
            screen.draw.filled_rect(rect, "gray")
            screen.draw.text(name.capitalize(), center=rect.center, fontsize=30, color="white")
    else:
        screen.clear()
        screen.fill("green")
        hero.draw()
        for enemy in enemies:
            enemy.draw()

# Update function
def update():
    if menu_active:
        return

    move_hero()
    animate_hero()

    for enemy in enemies:
        move_enemy(enemy)
        check_collision(hero, enemy)

# Handle hero movement
def move_hero():
    if keyboard.left:
        hero.x -= hero.speed
    if keyboard.right:
        hero.x += hero.speed
    if keyboard.up:
        hero.y -= hero.speed
    if keyboard.down:
        hero.y += hero.speed

# Hero animation
def animate_hero():
    hero.animation_frame = (hero.animation_frame + 1) % hero.frame_count
    hero.image = f"hero_walk_{hero.animation_frame}"

# Enemy movement
def move_enemy(enemy):
    dx, dy = enemy.direction
    enemy.x += dx * enemy.speed
    enemy.y += dy * enemy.speed

    if enemy.left < 0 or enemy.right > WIDTH:
        enemy.direction = (-enemy.direction[0], enemy.direction[1])
    if enemy.top < 0 or enemy.bottom > HEIGHT:
        enemy.direction = (enemy.direction[0], -enemy.direction[1])

# Check collision
def check_collision(hero, enemy):
    if hero.colliderect(enemy):
        sounds[collision_sound].play()
        hero.pos = (WIDTH // 2, HEIGHT // 2)  # Reset hero position

# Handle mouse click
def on_mouse_down(pos):
    global menu_active
    for name, rect in buttons.items():
        if rect.collidepoint(pos):
            if name == "start":
                menu_active = False
                if music_enabled:
                    music.play(background_music)
            elif name == "toggle_music":
                toggle_music()
            elif name == "exit":
                exit()

pgzrun.go()
