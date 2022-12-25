import requests
from bs4 import BeautifulSoup

def startSrapping(url):
    content = requests.get(url)
    htmlContent = content.content
    #print(htmlContent)
    soup = BeautifulSoup(htmlContent, 'html.parser')
    #print(soup.prettify)

    title = soup.title
    print("Hello")
    print(title)

def get_capital(country):
    URL = f"https://en.wikipedia.org/wiki/{country}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    infobox = soup.find('table', {'class': 'infobox'})

    capital_row = infobox.find('th', text='Capital')

    if capital_row:
        capital_cell = capital_row.find_next_sibling()
        capital = capital_cell.text
        return capital
    else:
        return None

def get_largest_city(country):
    URL = f"https://en.wikipedia.org/wiki/{country}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    infobox = soup.find('table', {'class': 'infobox'})

    capital_row = infobox.find('th', text='Largest city')

    if capital_row:
        capital_cell = capital_row.find_next_sibling()
        capital = capital_cell.text
        return capital
    else:
        return None

def get_official_languages(country):
    URL = f"https://en.wikipedia.org/wiki/{country}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Find the infobox containing the language information
    infobox = soup.find('table', {'class': 'infobox'})

    # Find the row containing the language information
    language_row = infobox.find('th', text='Official languages')

    print("hello")
    print(language_row)

    # Find the cell containing the language information
    language_cell = language_row.find('td')

    # Find the links to the Wikipedia pages for the official languages
    language_links = language_cell.find_all('a')

    official_languages = []

    # Iterate through the links to extract the language names
    for link in language_links:
        language_name = link.text
        # Strip out unnecessary information
        language_name = language_name.split('(')[0]  # Strip text in parentheses
        language_name = language_name.split('[')[0]  # Strip disambiguation tags
        official_languages.append(language_name)
    return official_languages

def get_area_total(country):
    URL = f"https://en.wikipedia.org/wiki/{country}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    infobox = soup.find('table', {'class': 'infobox'})

    capital_row = infobox.find('th', text='Total')

    if capital_row:
        capital_cell = capital_row.find_next_sibling()
        capital = capital_cell.text
        return capital
    else:
        return None

def get_population(country):
    URL = f"https://en.wikipedia.org/wiki/{country}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    infobox = soup.find('table', {'class': 'infobox'})

    capital_row = infobox.find('th', text='Population')

    if capital_row:
        capital_cell = capital_row.find_next_sibling()
        capital = capital_cell.text
        return capital
    else:
        return None

def get_nominal_gdp(country):
    URL = f"https://en.wikipedia.org/wiki/{country}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    infobox = soup.find('table', {'class': 'infobox'})

    capital_row = infobox.find('th', text='GDP')

    if capital_row:
        capital_cell = capital_row.find_next_sibling()
        capital = capital_cell.text
        return capital
    else:
        return None



# Official languages
# Total
# Population
# GDP

countryName = 'Nepal'

print(get_capital(countryName))
print(get_largest_city(countryName))
print(get_official_languages(countryName))
print(get_area_total(countryName))
print(get_population(countryName))
print(get_nominal_gdp(countryName))

