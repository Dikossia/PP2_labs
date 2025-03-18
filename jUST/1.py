import pygame
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Define screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player 🎵")

# Define font
font = pygame.font.SysFont("Verdana", 20)

# Music folder (Change the path to your own)
MUSIC_FOLDER = "C:\\Users\\Huawei\\Desktop\\PP2_labs\\lab_7\\Music"

# Load all MP3 files from the music folder
songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]

# Check if there are any songs
if not songs:
    raise FileNotFoundError("No MP3 files found in the 'Music' folder!")

# Track index
current_song = 0
is_playing = False  # Initially, music is not playing

def play_song():
    """Play the current song."""
    global is_playing
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_song]))
    pygame.mixer.music.play()
    is_playing = True

def stop_song():
    """Stop the current song."""
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False

def next_song():
    """Play the next song."""
    global current_song
    current_song = (current_song + 1) % len(songs)
    play_song()

def prev_song():
    """Play the previous song."""
    global current_song
    current_song = (current_song - 1) % len(songs)
    play_song()

def display_text(text, y_offset):
    """Display text on the screen."""
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 100 + y_offset))

# Start the first song
play_song()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Display currently playing song
    display_text(f"Playing: {songs[current_song]}", 0)
    display_text("P: Play  |  Space: Pause/Unpause  |  S: Stop", 40)
    display_text("N: Next  |  B: Previous  |  Esc: Exit", 70)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                play_song()
            elif event.key == pygame.K_SPACE:  # Pause/Unpause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True
            elif event.key == pygame.K_s:  # Stop
                stop_song()
            elif event.key == pygame.K_n:  # Next song
                next_song()
            elif event.key == pygame.K_b:  # Previous song
                prev_song()
            elif event.key == pygame.K_ESCAPE:  # Exit
                running = False

    pygame.display.update()

# Quit pygame
pygame.quit()
