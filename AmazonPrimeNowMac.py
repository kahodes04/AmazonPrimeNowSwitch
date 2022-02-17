import datetime
import time
import bs4
import os
import requests
import webbrowser

with requests.session() as c:
    print("APNSS. vers 1.0.2")
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
            
            text = gray + "\n" + neon
            title = "AmazonPrimeNow Switch AVAILABLE"
            sound = "/System/Library/Sounds/Purr.aiff"
            os.system(""" afplay "{}" """.format(sound))
            os.system(""" afplay "{}" """.format(sound))
            os.system(""" afplay "{}" """.format(sound))
            os.system("""
              osascript -e 'display notification "{}" with title "{}" sound name "{}"'
              """.format(text, title,sound))


        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print(st + "\n" + neon + "\n" + gray + "\n")
        time.sleep(int(sleeptime))

