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
    This will require you to install, also, some drivers, that the library will use to simulate a game-pad, follow the instructions on the wizard that pops on screen as you install the package to do so.<br>
    `pip install vgamepad`
- **keyboard** ([this library](https://pypi.org/project/keyboard/))<br>
    `pip install keyboard`

Finally, download the code for "Er Pescator" from this github page, [click this link](https://github.com/EMJzero/Er-Pescator/blob/master/er_pescator.py) and press the download icon on the top right side of the text area!<br>
Alternatively, if you have `git` ready to use, you can directly clone this repository.<br>
Anyway, you will be downloading the python script called `er_pescator.py` that performs the fishing :) .

Note that, before using the script, you need to restart Destiny 2 (if it was running since before the package installation process), as it needs to recognize the drivers for the simulated controller, and it does so on startup.

One last thing, make sure to have the controller **rumble enabled** in Destiny 2.

## Usage

We shall now fish!
- Open the `er_pescator.py` script with right-click and "open with IDLE" or "edit with IDLE" (choose the newest version of python if prompted to do so). This shall open a new window with the script's code, ignore it for now.
- In Destiny 2, reach a pond and get close to it until you see the prompt to start fishing.
- On the IDLE window we previously opened up, press "F5" to run the script.
- Now move to Destiny 2 and press `9`.
- Finally, you can even do other stuff with your computer now, Destiny 2 does not need to be in the foreground!

Once the script is running, its commands are the following:
- `9`: start the fishing routine
- `0`: stop the fishing routine

### **Important**
The script uses the rumble commands sent to the controller as cue to decide when to pick up the fish, as the rumble is slightly random, it might happen that it missfires and starts going idle, in that case just restart the fishing routine by pressing `9`.<br><br>
If you are curious and want to tune the behavior of the script, you can enable the logging of rumble values by changing line 6 into:<br>
`log_rumble_values = True`<br>
And then you can play around with the **lower bounds** of the two values on line 18. The values range from 0 to 255, so leave the upper bounds untouched. I found the (200, 220) pair of lower bounds to be pretty reliable, bue feel free to try others!
