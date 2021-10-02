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
5. Extract the zip into C:\Program Files (x86)
6. Open into a codeeditor you like and enjoy!

## Executable Script Generation
pyinstaller.exe --onefile --windowed app.py 

## Renable Console
Go to C:\ProgramData\Anaconda3\Lib\site-packages\selenium\webdriver\common\service.py
and remove from win32process import CREATE_NO_WINDOW
and remove creationflags=CREATE_NO_WINDOW
