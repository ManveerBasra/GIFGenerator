# GIFGenerator
Developed during GCI 2016. <br>
This repository creates a GIF file with subtitles from a video and subtitle file.

## Setup Instructions
### Install python3

If python3 is not installed <br>
Run this in a command window:
```
sudo apt-get install python3
```
### Install pip
If pip3 is not installed <br>
Run this in a command window:
```
sudo apt-get install python3-setuptools
sudo easy_install3 pip
sudo mv /usr/local/bin/pip /usr/local/bin/pip-3
```
### Install pysubs2
Run this in a command window:
```
sudo pip3 install pysubs2
```
### Install MoviePy
Run this in a command window:
```
pip install moviepy
```
If you have neither setuptools nor ez_setup installed the command above will fail.<br>
If this is the case run this:
```
pip install ez_setup
```

## Usage Instructions
Open a command window in directory containing `gif_generate.py`
Run this command:
```
python gif_generate.py [-h] [--display-text= DISPLAY_TEXT]
                       [--sub-number= SUB_NUMBER] [--gif= GIF]
                       [--resize= RESIZE] [--fps= FPS] [--font= FONT]
                       [--font-size= FONT_SIZE] [--font-color= FONT_COLOR]
                       [--stroke-width= STROKE_WIDTH]
                       [--stroke-color= STROKE_COLOR] [--capital= CAPITAL]
                       video subtitles
```
Or run this command for more information:
```
python gif_generate.py [-h]
```
