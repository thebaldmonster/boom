
#!/bin/bash

# Update system
sudo apt-get update
sudo apt-get install -y python3-pip git

# Install required packages
sudo pip3 install RPi.GPIO
sudo pip3 install adafruit-circuitpython-neopixel
sudo pip3 install pygame
sudo pip3 install board

# Create directories
mkdir -p ~/radio_project/folder{1,2,3}

# Copy main program
cp main.py ~/radio_project/

# Set up autostart
echo "@reboot python3 /home/pi/radio_project/main.py &" | sudo tee -a /etc/crontab

# Set permissions
sudo chmod +x ~/radio_project/main.py

echo "Installation complete! Reboot your Raspberry Pi to start the program."
