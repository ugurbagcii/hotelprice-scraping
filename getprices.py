from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime
from datetime import date, timedelta

print("------------------------------------------------------------------------------------------------")
specificDate = input("Would you like to enter a specific date? for YES (1), for NO (2): ")
print("------------------------------------------------------------------------------------------------")

if specificDate == "1":
    cInDay      = input("Check/in Day: ")
    print("------------------------------------------------------------------------------------------------")
    cInMonth    = input("Check/in Month: ")
    print("------------------------------------------------------------------------------------------------")
    cInYear     = input("Check/in Year: ")
    print("------------------------------------------------------------------------------------------------")
    cOutDay     = input("Check/Out Day: ")
    print("------------------------------------------------------------------------------------------------")
    cOutMonth   = input("Check/Out Month: ")
    print("------------------------------------------------------------------------------------------------")
    cOutYear    = input("Check/Out Year: ")
    print("------------------------------------------------------------------------------------------------")
    print("--- This may take several minutes ---")
    print("------------------------------------------------------------------------------------------------")

    browser = webdriver.Chrome()

    """ HOLIDAY INN LARA """
    browser.get("https://tr.hotels.com/ho489303296/?pa=1&q-check-out=" + cOutYear + "-" + cOutMonth + "-" + cOutDay + "&tab=description&q-room-0-adults=2&YGF=2&q-check-in=" + cInYear + "-" + cInMonth + "-" + cInDay + "&MGT=1&WOE=3&WOD=2&ZSX=0&SYE=3&q-room-0-children=0")
    html = browser.page_source
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    price  = soup.find("span", {"class": "current-price"})
    if price is None:
        name = "Holiday Inn Antalya - Lara"
        price = "***"
    else:
        name   = soup.find("h1").text
        price  = soup.find("span", {"class": "current-price"}).text
    hotel1 = name
    price1 = str(price)

    """ DOUBLE TREE BY HILTON ANTALYA CITY CENTRE """
    browser.get("https://tr.hotels.com/ho1146923296/?pa=1&q-check-out=" + cOutYear + "-" + cOutMonth + "-" + cOutDay + "&tab=description&q-room-0-adults=2&YGF=2&q-check-in=" + cInYear + "-" + cInMonth + "-" + cInDay + "&MGT=1&WOE=3&WOD=2&ZSX=0&SYE=3&q-room-0-children=0")
    html = browser.page_source
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    price  = soup.find("span", {"class": "current-price"})
    if price is None:
        name = "DoubleTree By Hilton Antalya City Centre"
        price = "***"
    else:
        name   = soup.find("h1").text
        price  = soup.find("span", {"class": "current-price"}).text
    hotel2 = name
    price2 = str(price)

    """ CROWNE PLAZA HOTEL ANTALYA """
    browser.get("https://tr.hotels.com/ho335845/?pa=1&q-check-out=" + cOutYear + "-" + cOutMonth + "-" + cOutDay + "&tab=description&q-room-0-adults=2&YGF=2&q-check-in=" + cInYear + "-" + cInMonth + "-" + cInDay + "&MGT=1&WOE=3&WOD=2&ZSX=0&SYE=3&q-room-0-children=0")
    html = browser.page_source
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    price  = soup.find("span", {"class": "current-price"})
    if price is None:
        name = "Crowne Plaza Hotel Antalya"
        price = "***"
    else:
        name   = soup.find("h1").text
        price  = soup.find("span", {"class": "current-price"}).text
    hotel3 = name
    price3 = str(price)

    """ CLUB HOTEL SERA """
    browser.get("https://tr.hotels.com/ho227807/?pa=1&q-check-out=" + cOutYear + "-" + cOutMonth + "-" + cOutDay + "&tab=description&q-room-0-adults=2&YGF=2&q-check-in=" + cInYear + "-" + cInMonth + "-" + cInDay + "&MGT=1&WOE=3&WOD=2&ZSX=0&SYE=3&q-room-0-children=0")
    html = browser.page_source
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    price  = soup.find("span", {"class": "current-price"})
    if price is None:
        name = "Club Hotel Sera - All Inclusive"
        price = "***"
    else:
        name   = soup.find("h1").text
        price  = soup.find("span", {"class": "current-price"}).text
    hotel4 = name
    price4 = str(price)

    """ RIXOS DOWNTOWN HOTEL ANTALYA """
    browser.get("https://tr.hotels.com/ho142993/?pa=1&q-check-out=" + cOutYear + "-" + cOutMonth + "-" + cOutDay + "&tab=description&q-room-0-adults=2&YGF=2&q-check-in=" + cInYear + "-" + cInMonth + "-" + cInDay + "&MGT=1&WOE=3&WOD=2&ZSX=0&SYE=3&q-room-0-children=0")
    html = browser.page_source
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    price  = soup.find("span", {"class": "current-price"})
    if price is None:
        name = "Rixos Downtown Antalya"
        price = "***"
    else:
        name   = soup.find("h1").text
        price  = soup.find("span", {"class": "current-price"}).text
    hotel5 = name
    price5 = str(price)

    f = open("index.html", "w")
    f.write("""
    <!DOCTYPE html>
    <html lang="tr-TR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles.css">
        <link href="https://fonts.googleapis.com/css2?family=Jost&display=swap" rel="stylesheet">
        <title>HOTEL PRICES</title>
    </head>
    <body>

        <h1>HOTELS.COM</h1>
        <table id="table">
            <tr>
                <th>Check/In: """ + cInDay + """/""" + cInMonth + """/""" + cInYear + """ --- Check/Out: """ + cOutDay + """/""" + cOutMonth + """/""" + cOutYear + """</th>
                <th>Fiyat</th>
            </tr>
            <tr>
                <td>"""+hotel1+"""</td>
                <td>"""+price1+"""</td>
            </tr>
            <tr>
                <td>"""+hotel2+"""</td>
                <td>"""+price2+"""</td>
            </tr>
            <tr>
                <td>"""+hotel3+"""</td>
                <td>"""+price3+"""</td>
            </tr>
            <tr>
                <td>"""+hotel4+"""</td>
                <td>"""+price4+"""</td>
            </tr>
            <tr>
                <td>"""+hotel5+"""</td>
                <td>"""+price5+"""</td>
            </tr>
        </table>
        
        <script>
            const cells = document.getElementById("table").getElementsByTagName("td");
            for (let i = 0; i < cells.length; i++) {
                if (cells[i].innerHTML == "***") {
                    cells[i].style.backgroundColor = "#ff3f34";
                }
            }
        </script>

    </body>
    </html>
    """)
    f.close()
    
elif specificDate == "2":

    print("--- This may take 6-8 minutes ---")
    print("------------------------------------------------------------------------------------------------")

    browser = webdriver.Chrome()

    hotel1 = ["name"]
    hotel2 = ["name"]
    hotel3 = ["name"]
    hotel4 = ["name"]
    hotel5 = ["name"]

    i = 0
    while i < 14:

        today = date.today() + datetime.timedelta(days = i)
        cInDay = str(today.day)
        cInMonth = str(today.month)
        cInYear = str(today.year)
        
        tomorrow = date.today() + datetime.timedelta(days = i + 1)
        cOutDay = str(tomorrow.day)
        cOutMonth = str(tomorrow.month)
        cOutYear = str(tomorrow.year)

        """ HOLIDAY INN LARA """
        browser.get("https://tr.hotels.com/ho489303296/?pa=1&q-check-out=" + cOutYear + "-" + cOutMonth + "-" + cOutDay + "&tab=description&q-room-0-adults=2&YGF=2&q-check-in=" + cInYear + "-" + cInMonth + "-" + cInDay + "&MGT=1&WOE=3&WOD=2&ZSX=0&SYE=3&q-room-0-children=0")
        html = browser.page_source
        time.sleep(2)
        soup = BeautifulSoup(html, 'html.parser')
        price  = soup.find("span", {"class": "current-price"})
        if price is None:
            name = "Holiday Inn Antalya - Lara"
            price = "***"
        else:
            name   = soup.find("h1").text
            price  = soup.find("span", {"class": "current-price"}).text
        hotel1[0] = name
        hotel1.append(str(price))

        i += 1
    
    i = 0
    while i < 14:

        today = date.today() + datetime.timedelta(days = i)
        cInDay = str(today.day)
        cInMonth = str(today.month)
        cInYear = str(today.year)
        
        tomorrow = date.today() + datetime.timedelta(days = i + 1)
        cOutDay = str(tomorrow.day)
        cOutMonth = str(tomorrow.month)
        cOutYear = str(tomorrow.year)

        """ DOUBLE TREE BY HILTON ANTALYA CITY CENTRE """
        browser.get("https://tr.hotels.com/ho1146923296/?pa=1&q-check-out=" + cOutYear + "-" + cOutMonth + "-" + cOutDay + "&tab=description&q-room-0-adults=2&YGF=2&q-check-in=" + cInYear + "-" + cInMonth + "-" + cInDay + "&MGT=1&WOE=3&WOD=2&ZSX=0&SYE=3&q-room-0-children=0")
        html = browser.page_source
        time.sleep(2)
        soup = BeautifulSoup(html, 'html.parser')
        price  = soup.find("span", {"class": "current-price"})
        if price is None:
            name = "DoubleTree By Hilton Antalya City Centre"
            price = "***"
        else:
            name   = soup.find("h1").text
            price  = soup.find("span", {"class": "current-price"}).text
        hotel2[0] = name
        hotel2.append(str(price))

        i += 1

    i = 0
    while i < 14:

        today = date.today() + datetime.timedelta(days = i)
        cInDay = str(today.day)
        cInMonth = str(today.month)
        cInYear = str(today.year)
        
        tomorrow = date.today() + datetime.timedelta(days = i + 1)
        cOutDay = str(tomorrow.day)
        cOutMonth = str(tomorrow.month)
        cOutYear = str(tomorrow.year)

        """ CROWNE PLAZA HOTEL ANTALYA """
        browser.get("https://tr.hotels.com/ho335845/?pa=1&q-check-out=" + cOutYear + "-" + cOutMonth + "-" + cOutDay + "&tab=description&q-room-0-adults=2&YGF=2&q-check-in=" + cInYear + "-" + cInMonth + "-" + cInDay + "&MGT=1&WOE=3&WOD=2&ZSX=0&SYE=3&q-room-0-children=0")
        html = browser.page_source
        time.sleep(2)
        soup = BeautifulSoup(html, 'html.parser')
        price  = soup.find("span", {"class": "current-price"})
        if price is None:
            name = "Crowne Plaza Hotel Antalya"
            price = "***"
        else:
            name   = soup.find("h1").text
            price  = soup.find("span", {"class": "current-price"}).text
        hotel3[0] = name
        hotel3.append(str(price))

        i += 1

    i = 0
    while i < 14:

        today = date.today() + datetime.timedelta(days = i)
        cInDay = str(today.day)
        cInMonth = str(today.month)
        cInYear = str(today.year)
        
        tomorrow = date.today() + datetime.timedelta(days = i + 1)
        cOutDay = str(tomorrow.day)
        cOutMonth = str(tomorrow.month)
        cOutYear = str(tomorrow.year)

        """ CLUB HOTEL SERA """
        browser.get("https://tr.hotels.com/ho227807/?pa=1&q-check-out=" + cOutYear + "-" + cOutMonth + "-" + cOutDay + "&tab=description&q-room-0-adults=2&YGF=2&q-check-in=" + cInYear + "-" + cInMonth + "-" + cInDay + "&MGT=1&WOE=3&WOD=2&ZSX=0&SYE=3&q-room-0-children=0")
        html = browser.page_source
        time.sleep(2)
        soup = BeautifulSoup(html, 'html.parser')
        price  = soup.find("span", {"class": "current-price"})
        if price is None:
            name = "Club Hotel Sera - All Inclusive"
            price = "***"
        else:
            name   = soup.find("h1").text
            price  = soup.find("span", {"class": "current-price"}).text
        hotel4[0] = name
        hotel4.append(str(price))

        i += 1

    i = 0
    while i < 14:

        today = date.today() + datetime.timedelta(days = i)
        cInDay = str(today.day)
        cInMonth = str(today.month)
        cInYear = str(today.year)
        
        tomorrow = date.today() + datetime.timedelta(days = i + 1)
        cOutDay = str(tomorrow.day)
        cOutMonth = str(tomorrow.month)
        cOutYear = str(tomorrow.year)

        """ RIXOS DOWNTOWN HOTEL ANTALYA """
        browser.get("https://tr.hotels.com/ho142993/?pa=1&q-check-out=" + cOutYear + "-" + cOutMonth + "-" + cOutDay + "&tab=description&q-room-0-adults=2&YGF=2&q-check-in=" + cInYear + "-" + cInMonth + "-" + cInDay + "&MGT=1&WOE=3&WOD=2&ZSX=0&SYE=3&q-room-0-children=0")
        html = browser.page_source
        time.sleep(2)
        soup = BeautifulSoup(html, 'html.parser')
        price  = soup.find("span", {"class": "current-price"})
        if price is None:
            name = "Rixos Downtown Antalya"
            price = "***"
        else:
            name   = soup.find("h1").text
            price  = soup.find("span", {"class": "current-price"}).text
        hotel5[0] = name
        hotel5.append(str(price))

        i += 1

    today1 = date.today() + datetime.timedelta(days = 0)
    if today1.day < 10:
        day1 = "0" + str(today1.day)
    else:
        day1 = str(today1.day)
    if today1.month < 10:
        month1 = "0" + str(today1.month)
    else:
        month1 = str(today1.month)

    today2 = date.today() + datetime.timedelta(days = 1)
    if today2.day < 10:
        day2 = "0" + str(today2.day)
    else:
        day2 = str(today2.day)
    if today2.month < 10:
        month2 = "0" + str(today2.month)
    else:
        month2 = str(today2.month)

    today3 = date.today() + datetime.timedelta(days = 2)
    if today3.day < 10:
        day3 = "0" + str(today3.day)
    else:
        day3 = str(today3.day)
    if today3.month < 10:
        month3 = "0" + str(today3.month)
    else:
        month3 = str(today3.month)

    today4 = date.today() + datetime.timedelta(days = 3)
    if today4.day < 10:
        day4 = "0" + str(today4.day)
    else:
        day4 = str(today4.day)
    if today4.month < 10:
        month4 = "0" + str(today4.month)
    else:
        month4 = str(today4.month)

    today5 = date.today() + datetime.timedelta(days = 4)
    if today5.day < 10:
        day5 = "0" + str(today5.day)
    else:
        day5 = str(today5.day)
    if today5.month < 10:
        month5 = "0" + str(today5.month)
    else:
        month5 = str(today5.month)

    today6 = date.today() + datetime.timedelta(days = 5)
    if today6.day < 10:
        day6 = "0" + str(today6.day)
    else:
        day6 = str(today6.day)
    if today6.month < 10:
        month6 = "0" + str(today6.month)
    else:
        month6 = str(today6.month)

    today7 = date.today() + datetime.timedelta(days = 6)
    if today7.day < 10:
        day7 = "0" + str(today7.day)
    else:
        day7 = str(today7.day)
    if today7.month < 10:
        month7 = "0" + str(today7.month)
    else:
        month7 = str(today7.month)

    today8 = date.today() + datetime.timedelta(days = 7)
    if today8.day < 10:
        day8 = "0" + str(today8.day)
    else:
        day8 = str(today8.day)
    if today8.month < 10:
        month8 = "0" + str(today8.month)
    else:
        month8 = str(today8.month)
    
    today9 = date.today() + datetime.timedelta(days = 8)
    if today9.day < 10:
        day9 = "0" + str(today9.day)
    else:
        day9 = str(today9.day)
    if today9.month < 10:
        month9 = "0" + str(today9.month)
    else:
        month9 = str(today9.month)
    
    today10 = date.today() + datetime.timedelta(days = 9)
    if today10.day < 10:
        day10 = "0" + str(today10.day)
    else:
        day10 = str(today10.day)
    if today10.month < 10:
        month10 = "0" + str(today10.month)
    else:
        month10 = str(today10.month)
    
    today11 = date.today() + datetime.timedelta(days = 10)
    if today11.day < 10:
        day11 = "0" + str(today11.day)
    else:
        day11 = str(today11.day)
    if today11.month < 10:
        month11 = "0" + str(today11.month)
    else:
        month11 = str(today11.month)
    
    today12 = date.today() + datetime.timedelta(days = 11)
    if today12.day < 10:
        day12 = "0" + str(today12.day)
    else:
        day12 = str(today12.day)
    if today12.month < 10:
        month12 = "0" + str(today12.month)
    else:
        month12 = str(today12.month)
    
    today13 = date.today() + datetime.timedelta(days = 12)
    if today13.day < 10:
        day13 = "0" + str(today13.day)
    else:
        day13 = str(today13.day)
    if today13.month < 10:
        month13 = "0" + str(today13.month)
    else:
        month13 = str(today13.month)
    
    today14 = date.today() + datetime.timedelta(days = 13)
    if today14.day < 10:
        day14 = "0" + str(today14.day)
    else:
        day14 = str(today14.day)
    if today14.month < 10:
        month14 = "0" + str(today14.month)
    else:
        month14 = str(today14.month)

    f = open("index.html", "w")
    f.write("""
    <!DOCTYPE html>
    <html lang="tr-TR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles.css">
        <link href="https://fonts.googleapis.com/css2?family=Jost&display=swap" rel="stylesheet">
        <title>HOTEL PRICES</title>
    </head>
    <body>

        <h1>HOTELS.COM</h1>
        <table id="table">
            <tr>
                <th>OTEL ADI</th>
                <th>""" + day1 + """/""" + month1 + """</th>
                <th>""" + day2 + """/""" + month2 + """</th>
                <th>""" + day3 + """/""" + month3 + """</th>
                <th>""" + day4 + """/""" + month4 + """</th>
                <th>""" + day5 + """/""" + month5 + """</th>
                <th>""" + day6 + """/""" + month6 + """</th>
                <th>""" + day7 + """/""" + month7 + """</th>
                <th>""" + day8 + """/""" + month8 + """</th>
                <th>""" + day9 + """/""" + month9 + """</th>
                <th>""" + day10 + """/""" + month10 + """</th>
                <th>""" + day11 + """/""" + month11 + """</th>
                <th>""" + day12 + """/""" + month12 + """</th>
                <th>""" + day13 + """/""" + month13 + """</th>
                <th>""" + day14 + """/""" + month14 + """</th>
            </tr>
            <tr>
                <td>"""+hotel1[0]+"""</td>
                <td>"""+hotel1[1]+"""</td>
                <td>"""+hotel1[2]+"""</td>
                <td>"""+hotel1[3]+"""</td>
                <td>"""+hotel1[4]+"""</td>
                <td>"""+hotel1[5]+"""</td>
                <td>"""+hotel1[6]+"""</td>
                <td>"""+hotel1[7]+"""</td>
                <td>"""+hotel1[8]+"""</td>
                <td>"""+hotel1[9]+"""</td>
                <td>"""+hotel1[10]+"""</td>
                <td>"""+hotel1[11]+"""</td>
                <td>"""+hotel1[12]+"""</td>
                <td>"""+hotel1[13]+"""</td>
                <td>"""+hotel1[14]+"""</td>
            </tr>
            <tr>
                <td>"""+hotel2[0]+"""</td>
                <td>"""+hotel2[1]+"""</td>
                <td>"""+hotel2[2]+"""</td>
                <td>"""+hotel2[3]+"""</td>
                <td>"""+hotel2[4]+"""</td>
                <td>"""+hotel2[5]+"""</td>
                <td>"""+hotel2[6]+"""</td>
                <td>"""+hotel2[7]+"""</td>
                <td>"""+hotel2[8]+"""</td>
                <td>"""+hotel2[9]+"""</td>
                <td>"""+hotel2[10]+"""</td>
                <td>"""+hotel2[11]+"""</td>
                <td>"""+hotel2[12]+"""</td>
                <td>"""+hotel2[13]+"""</td>
                <td>"""+hotel2[14]+"""</td>
            </tr>
            <tr>
                <td>"""+hotel3[0]+"""</td>
                <td>"""+hotel3[1]+"""</td>
                <td>"""+hotel3[2]+"""</td>
                <td>"""+hotel3[3]+"""</td>
                <td>"""+hotel3[4]+"""</td>
                <td>"""+hotel3[5]+"""</td>
                <td>"""+hotel3[6]+"""</td>
                <td>"""+hotel3[7]+"""</td>
                <td>"""+hotel3[8]+"""</td>
                <td>"""+hotel3[9]+"""</td>
                <td>"""+hotel3[10]+"""</td>
                <td>"""+hotel3[11]+"""</td>
                <td>"""+hotel3[12]+"""</td>
                <td>"""+hotel3[13]+"""</td>
                <td>"""+hotel3[14]+"""</td>
            </tr>
            <tr>
                <td>"""+hotel4[0]+"""</td>
                <td>"""+hotel4[1]+"""</td>
                <td>"""+hotel4[2]+"""</td>
                <td>"""+hotel4[3]+"""</td>
                <td>"""+hotel4[4]+"""</td>
                <td>"""+hotel4[5]+"""</td>
                <td>"""+hotel4[6]+"""</td>
                <td>"""+hotel4[7]+"""</td>
                <td>"""+hotel4[8]+"""</td>
                <td>"""+hotel4[9]+"""</td>
                <td>"""+hotel4[10]+"""</td>
                <td>"""+hotel4[11]+"""</td>
                <td>"""+hotel4[12]+"""</td>
                <td>"""+hotel4[13]+"""</td>
                <td>"""+hotel4[14]+"""</td>
            </tr>
            <tr>
                <td>"""+hotel5[0]+"""</td>
                <td>"""+hotel5[1]+"""</td>
                <td>"""+hotel5[2]+"""</td>
                <td>"""+hotel5[3]+"""</td>
                <td>"""+hotel5[4]+"""</td>
                <td>"""+hotel5[5]+"""</td>
                <td>"""+hotel5[6]+"""</td>
                <td>"""+hotel5[7]+"""</td>
                <td>"""+hotel5[8]+"""</td>
                <td>"""+hotel5[9]+"""</td>
                <td>"""+hotel5[10]+"""</td>
                <td>"""+hotel5[11]+"""</td>
                <td>"""+hotel5[12]+"""</td>
                <td>"""+hotel5[13]+"""</td>
                <td>"""+hotel5[14]+"""</td>
            </tr>
        </table>

        <script>
            const cells = document.getElementById("table").getElementsByTagName("td");
            for (let i = 0; i < cells.length; i++) {
                if (cells[i].innerHTML == "***") {
                    cells[i].style.backgroundColor = "#ff3f34";
                }
            }
        </script>

    </body>
    </html>
    """)
    f.close()

else:
    print("------------------------------------------------------------------------------------------------")
    print("Please enter 1 or 2..")
    print("------------------------------------------------------------------------------------------------")
    specificDate = input("Would you like to enter a specific date? for YES (1), for NO (2): ")
    if specificDate != "1" or specificDate != "2":
        specificDate = "1"

browser.get("C:/Users/USER/Desktop/index.html")