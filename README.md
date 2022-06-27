# Working Environmnet Setup
## Setting up MongoDB

1. Install `MongoDB Compass` - https://www.mongodb.com/try/download/compass.
2. Install `MongoDB Extension` on Visual Studio Code.
3. Install `MongoDB Community server` - https://www.mongodb.com/try/download/community
4. Install `MongoDB Tools` - https://www.mongodb.com/try/download/database-tools
5. Connect to MongoDB via VSCode extension using this code - `mongodb://localhost:27017`

## Installing all packages (via Terminal)

1. Install `Pymongo` - https://pypi.org/project/pymongo/
2. Install `Matplotlib` - https://matplotlib.org/stable/users/installing/index.html
3. Install `Numpy` - https://numpy.org/install/
4. Install `Pandas` - https://pandas.pydata.org/docs/getting_started/install.html
5. Install `TextBlob` - https://textblob.readthedocs.io/en/dev/install.html
6. Install `Regex` - https://blog.finxter.com/how-to-install-regex-in-python/

## Loading the data
1. Make sure MongoDB is running.
2. Create `data` folder and put all JSON files inside.
3. Create script based on your operating system. Exaples are in `load_data_example`.

### Linux
Create `load_data` file alongside the `load_data_example`\
Run from `/cavemen`: 
```sh
chmod +x load_data
sh ./load_data
```
### Windows
Create `load_data.bat` file in `data` folder\
Run from `\cavemen\data`
```sh
load_data.bat
```
### MacOS
Create `load_data.bat` file in `data` folder\
Run from `/cavemen/data`
```sh
sh ./load_data.bat
```

# Working With Data
## Data Cleaning

1. Make sure MongoDB Compass is up and connected to the database.
2. Make sure MongoDB extension on VSCode is up and connected to the database. 
3. Go to `Code_for_cleaning` folder and run `Calling_functions.py`
4. Go to `Code_for_cleaning` folder and run `cleaning.mongodb`

## Plots Sprint 1

1. Go to `Code_for_plots` folder and uncomment functions that you want to run `Sprint_1.py`

## Sentiment Analysis

1. Go to `Code_for_sentiment_analysis` folder and run `sa_textblob.py`

## Creating Conversations

1. Go to `Code_for_conversations` folder and run `Calling_functions.py`

## Data Augmentation

1. Go to `Code_for_augmentation` folder and run `Augmentation.py`

## Plots Sprint 2 and 3

1. Go to `Code_for_plots` folder and ucomment the function you want to run `Sprint_2_and_3.py`

## Running Demo 

1. Create `Plots_for_demo` folder and create `Extra_1.png`, `Extra_2.png` , `Extra_3.png`, and `Sentiment_change.png` files
2. Run `Running_demo.py`