# How to use the "Er Pescator" automatic fishing system | Destiny 2

## Requirements

- Have python 3 installed on your machine (Python3.9 or newer is suggested). You can download it from [here](https://www.python.org/downloads/release/python-3917/).

## Setup

You will need to procure a few packages using the python package manager, so for the unitiated this is how to use it: <br>

Open up a terminal of your liking (since I assume you are on Windows, the CMD is fine, just type `cmd` in the seach bar), then the command to use `pip` is one of the following, most likely the first one will work for you:
- `pip install <package_name>`
- `python -m pip install <package_name>`
- `python3 -m pip install <package_name>`

Now, install via `pip` the following packages:

- **vgamepad** ([this library](https://pypi.org/project/vgamepad/)) <br>
    This will require you to install, also, some drivers, that the library will use to simulate a game-pad, follow the instructions on the wizard that pops on screen as you install the package to do so.
- **keyboard** ([this library](https://pypi.org/project/keyboard/))

Finally, download the code for "Er Pescator" from this github page, or [click this link](nope)!<br>
You will be downloading the python script called `er_pescator.py` that performs the fishing :) .

## Usage

We shall now fish!
- Open the `er_pescator.py` script with right-click and "open with IDLE" (choose the newest version of python if prompted to do so);
- On the window that opens up, just press "F5" to run the script.

Once the script is running, its commands are the following:
- `1`: start the fishing routine
- `0`: stop the fishing routine

Important:
>The script uses the rumble commands sent to the controller as cue to decide when to pick up the fish, as the rumble is slightly random, it might happen that it missfires and starts going idle, in that case just restart the fishing routine by just pressing `1`.