import requests
import time
from NewsDAO import NewsDAO
from bs4 import BeautifulSoup

# Using the DAO


# def check_school_closure(url):  # Corrected E302
   
   
#     dao = NewsDAO()
#     closure_list = []


#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         response.raise_for_status()  # Raises an HTTPError for unsuccessful status codes
#         school_list = soup.find('ul', class_='school-closings-list')
#         for school in school_list.find_all('li', class_='school-closing'):
#         # Extract the school name
#             school_name = school.find('span', class_='school-closing-name').get_text().strip()

#         # Extract the school status
#             school_status = school.find('span', class_='school-closing-text').get_text().strip()
#             closure_list.append(school_name + " : " + school_status)
#             print(school_name + " : " + school_status)
#         return closure_list
#     except requests.exceptions.HTTPError as err:
#         print(err)
#         print("Initial request failed. Retrying in 10 seconds")
#         time.sleep(30)  # Pauses for 10 seconds
#         return check_school_closure(url)  # Recursively retry fetching data

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         dao.set_data(url + " BAD!!", "badData", "nothing")
#         return closure_list     



    # try:
    #     response = requests.get(url)
    #     response.raise_for_status()  # Raises an HTTPError for unsuccessful status codes

    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     title = soup.find('title').get_text()  # Corrected W291
    #     status = "open"

    #     print(response.status_code)
    #     dao.set_data(url, title.strip(), status)
    #     return dao

    # except requests.exceptions.HTTPError as err:
    #     print(err)
    #     print("Initial request failed. Retrying in 10 seconds")
    #     time.sleep(30)  # Pauses for 10 seconds
    #     return check_school_closure(url)  # Recursively retry fetching data

    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     dao.set_data(url + " BAD!!", "badData", "nothing")
    #     return dao

# Returns DAO
# Ensure there's a newline here at the end of the file

# Using the DAO
   
   
dao = NewsDAO()
closure_list = []


class BaseScraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.content
        except requests.exceptions.HTTPError as err:
            print(err)
            print("Request failed. Retrying in 10 seconds...")
            time.sleep(10)
            return self.fetch_data()  # Simple retry logic
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def parse_data(self, content):
        # Base method for parsing, to be overridden in subclass
        pass

    def runScraper(self):
        content = self.fetch_data()
        if content:
            return self.parse_data(content)
        return None


class abc11Scraper(BaseScraper):
    def parse_data(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        school_list = soup.find('ul', class_='school-closings-list')
        closure_list = {}
        try:
            for school in school_list.find_all('li', class_='school-closing'):
                school_name = school.find('span', class_='school-closing-name').get_text().strip()
                school_status = school.find('span', class_='school-closing-text').get_text().strip()
                closure_list.setdefault(school_name, school_status)
            
            return closure_list
        except Exception as e:
            print("no data. moving on")
            return []

class wralScraper(BaseScraper):
    def parse_data(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        school_list = soup.find('tbody')
        closure_list = {}
        try:    
            for school in school_list.find_all('tr'):
                school_name = school.find('td', {'data-title': 'Organization'}).get_text().strip()
                school_status = school.find('td', {'data-title': 'Status'}).get_text().strip()
                closure_list.setdefault(school_name, school_status)
        except Exception as e:
            print("no data. moving on")
            return []
        
        # for org in closure_list:
        #     print(f"{org[0]}: {org[1]}")
        # return closure_list
        
class wxii12Scraper(BaseScraper):
    
    def parse_data(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        school_list = soup.find('div', class_='weather-closings-data')
        closure_list = {}
        try:
            for school in school_list.find_all('div', class_='weather-closings-data-item'):
                school_name = school.find('h2', class_='weather-closings-data-name').get_text().strip()
                school_status = school.find('div', class_='weather-closings-data-status').get_text().strip()
                closure_list.setdefault(school_name, school_status)
        except Exception as e:
            print("no data. moving on")
            return []
        # for org in closure_list:
        #     print(f"{org[0]}: {org[1]}")

        return closure_list

# Example usage:
# scraper = abc11Scraper("https://example.com/school-closures")
# closures = scraper.run()
# print(closures)