# ePaper crypto watcher
Python example on how to show real time prices of cryptocurrencies and stocks using a Raspberry Pi and an ePaper Display
## Hardware needed
- Raspberry Pi
- Waveshare ePaper Display
- `tmux` package (for background execution, optional)
## Setup
1) Connect the ePaper Display to the Raspberry
2) Clone/Download the repository
3) In `cryptowatcher.py` replace `epd2in7` with your display's model ("2in7" means 2.7 inches, adjust for the size of your display)
4) Adjust the coordinates in the code to match display's size
5) Install libopenjp2-7 with the command `sudo apt install libopenjp2-7`
6) Install libtiff5 with the command `sudo apt install libtiff5`
7) Install pip for python3 with the command `sudo apt install python3-pip`
8) Install the package `spidev` using `sudo pip3 install spidev`
9) Install the package `RPi.GPIO` using `sudo pip3 install RPi.GPIO`
10) Install the package `PIL` using `sudo pip3 install Pillow`
11) \[Optional\] Install tmux and use the command `tmux`
12) Run the script with `sudo python3 cryptowatcher.py`
## Libraries included
I used the official libraries from Waveshare. You can find them here: https://github.com/waveshare/e-Paper
