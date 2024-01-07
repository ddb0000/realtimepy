import pygame
import threading
import random
import math
import IPython
import subprocess
import logging
from IPython.terminal.embed import InteractiveShellEmbed

logging.basicConfig(filename='game.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
subprocess.Popen(["start", "cmd", "/k", "python", "logger_script.py"], shell=True)

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

offscreen_surface = pygame.Surface((screen_width, screen_height))

class Particle:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randrange(0, screen_width)
        self.y = random.randrange(0, screen_height)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(0.5, 2.0)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.size = 3
        
    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed + gravity

        if self.x <= 0 or self.x >= self.screen_width:
            self.angle = math.pi - self.angle
        if self.y <= 0 or self.y >= self.screen_height:
            self.angle = -self.angle

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def update_screen_size(self, new_width, new_height):
        self.screen_width = new_width
        self.screen_height = new_height

particles = [Particle(screen_width, screen_height) for _ in range(100)]

def start_ipython():
    IPython.embed(using=False, colors='neutral', banner1='', exit_msg='', user_ns=globals())

ipython_thread = threading.Thread(target=start_ipython)
ipython_thread.start()

# Main game loop
gravity = 0.1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.w, event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            offscreen_surface = pygame.Surface((screen_width, screen_height))
            for particle in particles:
                particle.update_screen_size(screen_width, screen_height)
   
    offscreen_surface.fill((0, 0, 0))
    for particle in particles:
        particle.move()
        particle.draw(offscreen_surface)

    screen.blit(offscreen_surface, (0, 0))
    
    logging.info(f'Number of particles: {len(particles)}')

    pygame.display.flip()

    pygame.time.Clock().tick(60)
    
    # Fun
    def change_global_speed(factor):
        for particle in particles:
            particle.speed *= factor
    def randomize_directions():
        for particle in particles:
            particle.angle = random.uniform(0, 2 * math.pi)
    def change_particle_size(new_size):
        for particle in particles:
            particle.size = new_size
    def adjust_gravity(new_gravity):
        global gravity
        gravity = new_gravity
    def toggle_bouncing():
        global bounce
        bounce = not bounce
        for particle in particles:
            particle.bounce = bounce
    def update_particle_colors():
        for particle in particles:
            particle.color = (new_r, new_g, new_b)

pygame.quit()
