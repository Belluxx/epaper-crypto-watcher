# ePaper crypto watcher
Python example on how to show real time prices of cryptocurrencies and stocks using a Raspberry Pi and an ePaper Display.\
If this project was useful to you, please leave a ⭐ :)
## Hardware needed
- Raspberry Pi
- Waveshare ePaper Display
## Setup
### Setup the hardware
1) Connect the ePaper Display to the Raspberry
2) Enable the SPI interface: `sudo raspi-config` --> Interface Options --> SPI --> yes
### Download and tweak the code
3) Clone/Download the repository
4) In `cryptowatcher.py` replace `epd2in7` with your display's model ("2in7" means 2.7 inches, adjust for the size of your display)
5) Adjust the coordinates in the code to match display's size
### Install dependecies
6) Install libopenjp2-7 with the command `sudo apt install libopenjp2-7`
7) Install libtiff5 with the command `sudo apt install libtiff5`
8) Install pip for python3 with the command `sudo apt install python3-pip`
9) Install the package spidev using `sudo pip3 install spidev`
10) Install the package RPi.GPIO using `sudo pip3 install RPi.GPIO`
11) Install the package PIL using `sudo pip3 install Pillow`
### Run the code!
12) \[Optional\] Install tmux and use the command `tmux`
13) Run the script with `sudo python3 cryptowatcher.py`
## Libraries included
I used the official libraries from Waveshare. You can find them here: https://github.com/waveshare/e-Paper
