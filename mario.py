import pygame
import sys
import os
import math

# --- 1. Game Initialization and Constants ---
# Initialize Pygame modules
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Platformer Demo (Mario Style)")

# Game clock for managing frame rate
CLOCK = pygame.time.Clock()
FPS = 60

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
BROWN = (139, 69, 19)
GREEN = (34, 139, 34)

# --- Physics Constants ---
GRAVITY = 0.5
JUMP_STRENGTH = -12
PLAYER_SPEED = 5
TILE_SIZE = 50

# --- Helper Function for Simple Surface ---
def get_surface(color, size):
    """Creates a basic solid color square surface."""
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf

# --- 2. Player Class ---

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Create a simple player sprite (a red square)
        self.image = get_surface((255, 0, 0), (30, 50)) 
        self.rect = self.image.get_rect(topleft=(x, y))
        
        # Movement and physics variables
        self.direction = pygame.math.Vector2(0, 0)
        self.on_ground = False

    def get_input(self):
        """Handles keyboard input for movement and jumping."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = PLAYER_SPEED
        elif keys[pygame.K_LEFT]:
            self.direction.x = -PLAYER_SPEED
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def apply_gravity(self):
        """Applies vertical acceleration (gravity)."""
        self.direction.y += GRAVITY
        self.rect.y += self.direction.y

    def jump(self):
        """Sets upward velocity for jumping."""
        self.direction.y = JUMP_STRENGTH
        self.on_ground = False
        
    def update(self):
        """Called every frame to update player state."""
        self.get_input()

# --- 3. Tile/Platform Class ---

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y, color):
        super().__init__()
        self.image = get_surface(color, (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
        
# --- 4. Level Setup ---

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0 # For horizontal scrolling

    def setup_level(self, layout):
        """Creates sprites from the level map."""
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if cell == 'X':
                    # Ground tile
                    tile = Tile(TILE_SIZE, x, y, BROWN)
                    self.tiles.add(tile)
                elif cell == 'P':
                    # Player spawn point
                    player_sprite = Player(x, y)
                    self.player.add(player_sprite)
                    
    def scroll_x(self):
        """Handles simple camera/world scrolling."""
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        # Scroll the world if the player is near the edge
        if player_x < SCREEN_WIDTH / 4 and direction_x < 0:
            self.world_shift = PLAYER_SPEED
            player.direction.x = 0
        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH / 4) and direction_x > 0:
            self.world_shift = -PLAYER_SPEED
            player.direction.x = 0
        else:
            self.world_shift = 0

    def horizontal_movement_collision(self):
        """Checks for and resolves horizontal collisions."""
        player = self.player.sprite
        player.rect.x += player.direction.x
        
        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    # Moving left, hit a wall on the right
                    player.rect.left = tile.rect.right
                elif player.direction.x > 0:
                    # Moving right, hit a wall on the left
                    player.rect.right = tile.rect.left

    def vertical_movement_collision(self):
        """Checks for and resolves vertical collisions (gravity/jumping)."""
        player = self.player.sprite
        player.apply_gravity() # Move player down by gravity

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    # Falling down, land on top of the tile
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    # Jumping up, hit the bottom of the tile
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0

        # Reset on_ground if player is not colliding vertically
        if player.direction.y != 0:
             player.on_ground = False


    def run(self):
        """Draws and updates all elements of the level."""
        
        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # Scrolling logic
        self.scroll_x()

        # Player
        self.player.update()
        
        # Collision
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        
        self.player.draw(self.display_surface)

# --- 5. Game Loop and Level Map ---

# Level map: 'X' is a tile, 'P' is the player spawn point
# This creates a ground floor and a small platform
LEVEL_MAP = [
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '                            ',
    '     X X                    ',
    '  X XXXXX                   ',
    ' P XXXXXXXX                 ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
]

level = Level(LEVEL_MAP, SCREEN)

def game_loop():
    """The main game loop."""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Drawing ---
        SCREEN.fill(SKY_BLUE) # Clear screen with sky color
        
        # Run the level update and drawing
        level.run()

        # --- Update ---
        pygame.display.flip() # Update the full screen
        CLOCK.tick(FPS) # Limit frame rate

    pygame.quit()
    sys.exit()

# --- Execution ---
if __name__ == '__main__':
    game_loop()