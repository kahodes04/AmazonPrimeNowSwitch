# Amazon Prime Now Stock Scraper (APNSS)
This is a fairly simple script that will check the stock of the Amazon Prime Now website and return the ammount of units they have of a certain item. In this case it looks for both Nintendo Switch models and returns values for each one.
## Installation
Download the executable APNSS.exe and place it in a directory of your liking. You do not have to worry about the other files on GitHub. After doing that, the program is ready to be run, there is no extracting or installations to be made.
## Usage
Double click on the executable to start. It will ask you how long you want to wait after getting the stock information. Please, do not use very low numbers since it creates many requests to the website which could be harmful. It is recommended to use 5 seconds at a minimum. On every iteration, the program will print onto the console whether there is stock or not along with a timestamp. If there is stock of either system, three beeps will played followed by a Windows Notification [that looks like this](http://i.imgur.com/YcgPodv.png). The notification will keep showing up if there is stock the next time the program checks for it.
## Updates
### 1.0.2
The Amazon Prime Now website with the corresponding item will be opened upon stock detection. It will trigger a variable that will be turned off as soon as there is no stock left. When stock comes back in the website will be opened again. This is to deal with tabs opening every time the program checks and finds stock.
### 1.0.1
Notifications for Windows are added. The script icon is not displayed yet due to conflicts with the python freezer so the default one is used instead.
## Credits
Thanks to [wontocc](https://gist.github.com/wontoncc) for his help with the WindowsBalloonTip class.
