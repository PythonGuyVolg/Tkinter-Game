How to compile THEGAME.py on Mac os X:
1. Download all files from GitHub(.zip)
2. Unarchive .zip
3. Put unzipped folder into /Applications on your Mac (folder name - Tkinter-Game-master)
4. *Download py2app, threading, playsound (packages( you can use pip)) and python 3.7.6 or later*(if you have not downloaded them before)
5 open Terminal( Terminal.app )
6 put this commands into Terminal:
   cd /Applications/Tkinter-Game-master
   (setup.py have been already created by me, make sure this file locate in Tkinter-Game unzipped folder( doesnt move this file))
   rm -rf build dist
   python setup.py py2app -A  ( or python3 setup.py py2app -A if you use 2 versions of python)
   /// CONSOLE: ...... DONE!
    ""If the program work correctly you should be make this command: python setup.py py2app. (without -A) to pack all python files in one .app file""
 7  Run program: $ ./dist/THEGAME.app/Contents/MacOS/THEGAME ( in Terminal ) OR find your app on your mac with spotlight( or finder).
 8. If you do not see the image, try to click on running .app file in Dock. 
 
 9. Enjoy!!!!!! 
 
 If you have problems with this instruction, please go to the https://py2app.readthedocs.io/en/latest/tutorial.html#clean-up-your-build-directories
 or send me email: egorkacahnov1998@gmail.com 
 Egor Kachanov, April 8th
