# YouTube Bubble Analyzer

## Presentation
This is a a script to store YouTube "autoplay" playlist into a csv file. 
The goal is to know how the "autoplay" algorithm makes the user discover music.
Our hypotheses we want to confirm or infirm are :
- (i) If the user plays a song, the algorithm will always play similar songs (same artist, same genre...);
- (ii) If the user plays a song, the algorithm will tend to bring her to always the same songs related to the genre and artist of the first song;
- (iii) If the user plays a song, the algorithm will tend to bring her to always the same maintream song, no matter what is the initial song.
- (iv) The algorithm is not sensitive to users preferences, history, demographic characteristis, etc.

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
> "(iv) The algorithm is not sensitive to users preferences, history, demographic characteristis, etc."

### Long-term goals
Coming soon.

## Run the script
To run the script on your computer, you need to follow these steps:
1. Open the terminal
2. Check if Python is installed: type "python", it shoul return ">>>". If not, you can download it [here](https://www.python.org/downloads/) but I recommand using [Anaconda](https://www.continuum.io/downloads)
3. You can quit python by doing ctrl+d. 
4. Check if pip is effectively installed: type "pip" in the terminal. If not, here is the [doc](https://pip.pypa.io/en/stable/installing/).
5. Install [Splinter](https://splinter.readthedocs.io/en/latest/#) using pip: type "pip install splinter"
