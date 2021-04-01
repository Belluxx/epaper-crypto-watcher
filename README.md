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
5) \[Optional\] Install tmux and use the command `tmux`
6) Run the script with `sudo python3 cryptowatcher.py`
## Libraries included
I used the official libraries from Waveshare. You can find them here: https://github.com/waveshare/e-Paper
