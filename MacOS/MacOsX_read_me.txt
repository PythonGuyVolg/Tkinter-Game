How to compile THEGAME.py on Mac os X:
1. Download all files from GitHub(.zip)
2. Unarchive .zip
3. Put unzipped folder into /Applications on your Mac
4. *Download py2app, threading, playsound and python 3.7.6 or later*(if you have not downloaded them before)
5 open Terminal( Terminal.app )
6 put this commands into Terminal:
  py2applet --make-setup ....../Applications/......./THEGAME.py
   /// CONSOLE: Wrote setup.py
   rm -rf build dist
   python setup.py py2app -A 
   /// CONSOLE: ...... DONE!
    ""If the program work correctly you should be make this command: python setup.py py2app. (without -A) to pack all python files in one .app file""
 7  Run program: $ ./dist/MyApplication.app/Contents/MacOS/MyApplication ( in Terminal ) OR find your app on your mac with spotlight( or finder).
 8. If you do not see the image, try to click on running .app file in Dock. 
 
 9. Enjoy!!!!!! 
 
 If you have problems with this instruction, please go to the https://py2app.readthedocs.io/en/latest/tutorial.html#clean-up-your-build-directories
 or send me email: egorkacahnov1998@gmail.com 
 Egor Kachanov, April 8th
