import pygame

# Initialize Pygame
pygame.init()
npc = pygame.load.
# Set up the window
window = pygame.display.set_mode((400, 300))

# Create a font for the NPC's dialogue
font = pygame.font.SysFont('Arial', 24)

# Set the NPC's dialogue
dialogue = "Hello! I'm an NPC. How are you today?"

# Create a text surface with the NPC's dialogue
text = font.render(dialogue, True, (0, 0, 0))

# Set the location at which the text should be drawn on the screen
text_rect = text.get_rect(center=(200, 150))

# Create a clock to control the speed at which the text is displayed
clock = pygame.time.Clock()

# Main game loop
while True:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # Clear the screen
  window.fill((255, 255, 255))

  # Draw the NPC's dialogue on the screen
  window.blit(text, text_rect)

  # Update the display
  pygame.display.update()

  # Control the speed at which the text is displayed
  clock.tick(2000)