
import RPi.GPIO as GPIO
import board
import neopixel
import pygame
import os
import random
from threading import Thread
import time

# GPIO Setup
BUTTON_PINS = [17, 27, 22]  # GPIO pins for buttons
LED_COUNT = 4               # Number of individual LEDs
LED_PIN = board.D18        # GPIO pin for LED data (GPIO18)
LED_COLORS = [(255,0,0), (0,255,0), (0,0,255), (255,255,255)]  # Red, Green, Blue, White

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup buttons as inputs with pull-up resistors
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize NeoPixels
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=0.2, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

# Initialize pygame mixer
pygame.mixer.init()

class RadioPlayer:
    def __init__(self):
        self.current_player = None
        self.is_playing = False
        self.current_folder = None
        
    def play_folder(self, folder_index):
        # Stop current playback if any
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
            
        # Turn off all LEDs
        pixels.fill((0, 0, 0))
            
        # Turn on selected LED with corresponding color
        pixels[folder_index] = LED_COLORS[folder_index]
        pixels.show()
        
        # Get all MP3 files from selected folder
        folder = f'folder{folder_index + 1}'
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        mp3_files = [f for f in os.listdir(folder) if f.endswith('.mp3')]
        
        if mp3_files:
            random.shuffle(mp3_files)
            self.current_folder = folder_index
            self.is_playing = True
            
            for mp3 in mp3_files:
                if not self.is_playing:
                    break
                pygame.mixer.music.load(os.path.join(folder, mp3))
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() and self.is_playing:
                    time.sleep(0.1)

def button_callback(channel):
    button_index = BUTTON_PINS.index(channel)
    if not radio_player.is_playing or radio_player.current_folder != button_index:
        Thread(target=radio_player.play_folder, args=(button_index,)).start()

# Create radio player instance
radio_player = RadioPlayer()

# Add event detection for buttons
for pin in BUTTON_PINS:
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_callback, bouncetime=300)

try:
    print("Radio is ready! Press Ctrl+C to exit.")
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nExiting...")
    pixels.fill((0, 0, 0))
    pixels.show()
    GPIO.cleanup()
