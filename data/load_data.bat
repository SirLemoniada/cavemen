@echo off
for %%f in (*.json) do (
    "mongoimport.exe" --db cavemen --collection tweets --file %%~nf.json
)