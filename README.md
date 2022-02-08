# Python_Webbot
Selenium web bot to automate Flight Searching

## Imports
    pip install selenium
    pip install pyinstaller
    

## Executiion
1. Install Pip if not installed.
2. Install all the import dependencies
3. Find Chrome Version by clicking '...' -> Help -> About Chrome
4. Download chromewebdriver for that associated version
5. Extract the zip into working directory
6. Open into a codeeditor you like
7. Generate an exe using the below script
8. Copy the chromewebdriver wherever the application would be run from
8. Enjoy!

## Executable Script Generation
pyinstaller.exe --onefile --windowed app.py 

## Disable Console
Go to C:\ProgramData\Anaconda3\Lib\site-packages\selenium\webdriver\common\service.py
OR
C:\Python38\Lib\site-packages\selenium\webdriver\common\service.py
and add from win32process import CREATE_NO_WINDOW at line 26
and add creationflags=CREATE_NO_WINDOW at line 76 OR creationflags=134217728 (a hacky way)

## Enable Console
Go to C:\ProgramData\Anaconda3\Lib\site-packages\selenium\webdriver\common\service.py
and remove from win32process import CREATE_NO_WINDOW
and remove creationflags=CREATE_NO_WINDOW

## Remember to Update ChromeDriver for the chrome version you are using