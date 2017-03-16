import datetime
import time
import bs4
import requests
import winsound
with requests.session() as c:

    sleeppart = True
    zippart = True

    while(sleeppart):
        sleeptime = input("Enter the sleep time after every search in seconds: ")
        if (sleeptime < 20):
            print("The minimum sleep time is 20 seconds.")
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
                break
            neon = "Neon - No Stock"
        for item in filtered:
            if (item.text.strip() == "Nintendo Switch with Gray Joy-Con"):
                gray = "Gray - IN STOCK!"
                break
            gray = "Gray - No Stock"

        if (neon == "Neon - IN STOCK!" or gray == "Gray - IN STOCK!"):
            winsound.Beep(800, 250)
            winsound.Beep(800, 250)
            winsound.Beep(800, 250)

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print(st + "\n" + neon + "\n" + gray + "\n")
        time.sleep(int(sleeptime))