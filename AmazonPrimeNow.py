import datetime
from win32api import *
from win32gui import *
import sys, os
import win32con
import time
import bs4
import requests
import winsound
import webbrowser

class WindowsBalloonTip:
    def __init__(self):
        message_map = {
                win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        self.hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        self.classAtom = RegisterClass(wc)

    def ShowWindow(self,title, msg):
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow( self.classAtom, "Taskbar", style, \
                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                0, 0, self.hinst, None)
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join( sys.path[0], "balloontip.ico" ))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
           hicon = LoadImage(self.hinst, iconPathName, \
                    win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
          hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, \
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER+20,\
                        hicon, "Balloon  tooltip",msg,200,title))
        # self.show_balloon(title, msg)
        DestroyWindow(self.hwnd)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0) # Terminate the app.

with requests.session() as c:
    w = WindowsBalloonTip()
    openbrowserneon = False;
    openbrowsergray = False;

    sleeppart = True
    zippart = True
    while(sleeppart):
        sleeptime = input("Enter the sleep time after every search in seconds: ")
        if int(sleeptime) < 1:
            print("The minimum sleep time is 1 second.")
        else: sleeppart = False

    while(zippart):
        zip = input("Enter the zipcode of your choice: ")
        if (len(str(zip)) != 5):
            print("The zip code has to be at least 5 digits.")
        else: zippart = False

    print("Searching in zip code: "+ str(zip) + '\n')
    neon = "Neon - No Stock"
    gray = "Gray - No Stock"
    url = "https://primenow.amazon.com/"
    c.get(url)
    login_data = dict(newPostalCode = zip);
    c.post(url, data=login_data, headers = {'User-agent': 'Mozilla/5.0'})
    while(True):
        page = c.get("https://primenow.amazon.com/search?k=nintendo+switch&p_95=&merchantId=&ref_=pn_gw_nav_ALL", headers = {'User-agent': 'Mozilla/5.0'})
        soup = bs4.BeautifulSoup(page.text, 'lxml')
        filtered = soup.findAll("p", {"class": "asin__details__title"})
        for item in filtered:
            if(item.text.strip() == "Nintendo Switch with Neon Blue and Neon Red Joy-Con"):
                neon = "Neon - IN STOCK!"
                if openbrowserneon == False:
                    webbrowser.open("https://primenow.amazon.com/dp/B01MUAGZ49", new=0, autoraise=True);
                    openbrowserneon = True
                break
            openbrowserneon = False
            neon = "Neon - No Stock"
        for item in filtered:
            if (item.text.strip() == "Nintendo Switch with Gray Joy-Con"):
                gray = "Gray - IN STOCK!"
                if openbrowsergray == False:
                    webbrowser.open("https://primenow.amazon.com/gp/product/B01LTHP2ZK", new=0, autoraise=True);
                    openbrowsergray = True
                break
            openbrowsergray = False
            gray = "Gray - No Stock"
        if (neon == "Neon - IN STOCK!" or gray == "Gray - IN STOCK!"):
            winsound.Beep(800, 250)
            winsound.Beep(800, 250)
            winsound.Beep(800, 250)
            w.ShowWindow("Amazon Prime Now", neon + '\n' + gray);


        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print(st + "\n" + neon + "\n" + gray + "\n")
        time.sleep(int(sleeptime))

