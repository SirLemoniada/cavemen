# cavemen - DBL Challange
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

## Cleaning the data
1. Install MongoDB Exntension for VSCode 
2. Connectect to MongoDB thorugh the Exntension
3. Run calling_functions.py
4. Run duplicates.mongodb