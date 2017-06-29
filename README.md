# YouTube Bubble Analyzer

## Presentation
This is a a script to store YouTube "autoplay" playlist into a csv file. 
The goal is to know how the "autoplay" algorithm makes the user discover music.
Our hypotheses we want to confirm or infirm are:
- (i) If the user plays a song, the algorithm will always play similar songs (same artist, same genre...);
- (ii) If the user plays a song, the algorithm will tend to bring her to always the same songs related to the genre and artist of the first song;
- (iii) If the user plays a song, the algorithm will tend to bring her to always the same maintream song, no matter what is the initial song;
- (iv) The algorithm is not sensitive to users preferences, history, demographic characteristics, etc.

To do that, we created a Python (3.6) script that simulate an user, open a browser (Firefox) and record the following data for each new song played on YouTube :
- Title of the video
- Number of views
- URL
- Video ID
- Recording time

The output of the script is a csv file which looks like [that](https://github.com/jeremiepoiroux/RecoYouTube/blob/master/RecoYouTube_csv_example.png).

Currently, we are leading the beta-experimentation to test the script, to debug it.

## Goals
### Short-term goal
Our short term goal is to run the script on different computers to confirm or infirm the fourth hypothesis : 
> "(iv) The algorithm is not sensitive to users preferences, history, demographic characteristics, etc."

### Mid-term goals
You can follow the Kanban of the project [here](https://github.com/jeremiepoiroux/RecoYouTube/projects/1).

## Run the script
To run the script on your computer, you need to follow these steps:
1. Open the terminal
2. Check if Python 3.x is installed: type "python", it shoul return ">>>". If not, you can download it [here](https://www.python.org/downloads/) but I recommand using [Anaconda](https://www.continuum.io/downloads)
3. You can quit python by doing ctrl+d. 
4. Check if pip is effectively installed: type "pip" in the terminal. If not, here is the [doc](https://pip.pypa.io/en/stable/installing/).
5. Make sure you have already [set up](https://splinter.readthedocs.io/en/latest/contribute/setting-up-your-development-environment.html) your development environment
5. Install [Splinter](https://splinter.readthedocs.io/en/latest/#) using pip3: type "pip3 install splinter". It should also install selenium
7. Download the latest geckodriver [here](https://github.com/mozilla/geckodriver/releases), extract the file from the archive and rename it to "geckodriver" (with no "2" at the end if there is one).
8. Go to the folder with the terminal: assuming you have simply open the terminal, you are in the home folder. If the geckodriver is in the Download folder, type cd /Download.
9. Now your command line should be "xxx@xxxx : ~/Download". Move the geckodriver to a system folder: mv geckodriver /usr/local/bin
10. Make it executable: chmod +x /usr/local/bin/geckodriver
11. Make sure you have the last version (53 at least) of Firefox: type "firefox -V" on the terminal to check. It can be pretty triky to get it for Debian because you have to put the old version away. [Here](http://libre-software.net/how-to-install-firefox-on-ubuntu-linux-mint/) is a good tutorial
12. Download this folder from GitHub
13. Move to this folder with the terminal: "cd xxx/xxx/RecoYouTube"
14. Launch the script: type "python3 yt_scraper.py"
15. Go to the YouTube video from which you want to start the script and copy/paste the URL to the prompt in the terminal
16. Name your csv file in the prompt, for example "starting-adele-hello" (without the "" and the .csv)
17. If there is no error(s), the script should open Firefox, head to the video and start storing the data to the csv file. Note: it only store one line per song.
18. You can navigate through YouTube, listen to other songs, etc. The script will only store informations for videos. PLEASE NOTE: When you are not on a video page (e.g. search page), the terminal will report you an « Index out of range » error. No worries, it will continue his job as soon as you are on a video page.
19. To stop the script, simply do ctrl+c
