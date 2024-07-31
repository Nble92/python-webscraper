import news_List
import scraper
import db
import json
import time

def generate_id():
    id = 1
    while True:
        yield id
        id += 1

id_generator = generate_id()
next_id = next(id_generator)

def __init__():
    print("Starting Scraper")

    # scrprABC11 = scraper.abc11Scraper("https://web.archive.org/web/20240109124918/https://abc11.com/community/schoolclosings/")
    # scrprWRAL = scraper.wralScraper("https://web.archive.org/web/20220103135345/https://www.wral.com/weather/closings/")
    # scrprWXII = scraper.wxii12Scraper("https://web.archive.org/web/20240109031849/https://www.wxii12.com/weather/closings")

    scrprABC11 = scraper.abc11Scraper("https://abc11.com/community/schoolclosings/")
    scrprWRAL = scraper.wralScraper("https://www.wral.com/weather/closings/")
    scrprWXII = scraper.wxii12Scraper("https://www.wxii12.com/weather/closings")


    siteList = [
    scrprABC11,
    scrprWRAL,
    scrprWXII
    ]
    districtData = {}

    print("Now Scraping " + "the sites" + "!")
    for site in siteList:
        
        statusDict = site.runScraper()
        if statusDict:
            print(statusDict)
            print("\n")
# adding to dictionary
            districtData.update(statusDict)

    data_to_insert = [(org, status) for org, status in districtData.items()]   

    try:
        query = "INSERT INTO closures (Organization,Status) VALUES (%s,%s);"
        db.cursor.executemany(query, data_to_insert)
        db.conn.commit()
        print("Success!")
    except Exception as e:
        db.conn.rollback()
        print(f"Error storing data: {e}")
        
    db.close_connection()

__init__()  # Corrected E305


# Ensure there's a newline here at the end of the file
