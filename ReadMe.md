# sentiAnnotator140
![image](https://user-images.githubusercontent.com/39694920/155466640-335e2fb8-cb85-440e-805b-d1b21468fad7.png)

#### This can be use as a text labeling tool which has:
+ An input text box for setting your raw dataset as '.csv' file. 
+ 4 kinds of indicators:
+ > A numerical indicator which display predicted sentiment value of specified text(this attain from text blob libray)
+ > A green/red rectangular indicator which determine if there is a positive emotional emoji in the specified text or negative emotional emoji.
+ > Two textual indicators which display what you selected for labels (the left one display numerical label (1-5) and the right one display textual label ("Buy/Sell").
+ 5 buttons to assigan a numerical label (1 to 5) to the text.
+ 2 buttons to assign "Buy/Sell" label to specified text. (It could be helpful if you are labeling financial tweets like)
+ Next and Previous button to switch between tweets

## Usage:

#### 1. Make a ".csv" file (must be in ".csv" format and having three columns as bellow):
- Signal (leave it's value to be None)
- handySentiment (leave it's value to be None)
- tweet (fill this by your dataset tweets)

#### 2. Run "SentiAnnotator.exe"
#### 3. Enter ".csv" file which created in the first step and click "Enter" button
#### 4. Do Some Labeling
#### 5. Finalize your changes on dataset by click on Finish button and exit.
