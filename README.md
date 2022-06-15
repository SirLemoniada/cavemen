# Pre-process
## Loading the data
1. Make sure MongoDB is running
2. Create `data` folder and put all JSON files inside
3. create script based on `load_data_example`

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
sh ./load_data
```

## Steps for cleaning data, doing sentiment analysis, and grouping conversations  
1. Install MongoDB Exntension for VSCode 
2. Connectect to MongoDB thorugh the Exntension
3. Go to Code_for_cleaning file
4. Run Calling_functions.py
5. Run Cleaning.mongodb
6. Go to Code_for_sentiment file
7. Run Sa_textbob.py
8. Go to Code_for_conversations file
9. Run Calling_functions.py