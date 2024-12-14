
# Raspberry Pi LED Music Player

A Python-based music player that controls WS2812B LEDs (4x 5050 RGB LEDs) and plays MP3 files using buttons on a Raspberry Pi 3.

## Hardware Requirements
- Raspberry Pi 3
- 4x WS2812B 5050 RGB LEDs
- 3x Push buttons
- 5V Power supply

## Wiring
- Connect LED data line to GPIO18 (Pin 12)
- Connect buttons to GPIO17, GPIO27, and GPIO22
- Connect LED ground to Pi GND
- Connect LED VCC to 5V power supply

## Installation
```bash
git clone https://github.com/thebaldmonster/boom
cd boom
chmod +x install.sh
./install.sh
```

## Usage
1. Place MP3 files in folder1, folder2, or folder3
2. Press buttons to play music from respective folders
3. LEDs will indicate which folder is playing
