import requests         # for html requests
import bs4              # handle HTML
import collections      # includes named tuples


# define type
WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')


def main():
    # print header
    print_header()

    # get ZIP from user
    z_code = input('What ZIP code do you want the weather for? ')

    # get HTML  from web www.wunderground.com
    html = get_html_from_web(z_code)

    # parse HTML (using beautiful soup)
    report = get_weather_from_html(html)

    print('The weather in {} is {} and the temperature is {} {}'.format(
        report.loc,
        report.cond,
        report.temp,
        report.scale
    ))

    # display the forecast
    strleng = 0
    strleng = len(z_code)


def print_header():
    print('------------------------')
    print('      WEATHER APP')
    print('------------------------')
    print()


def get_html_from_web(zipCode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipCode)
    response = requests.get(url)
    # print(response.status_code)  # should be 200
    # print(response.text[0:250])  # slice - get 0 to 250th char
    return response.text


def get_weather_from_html(html):
    # #### FOR REFERENCE #### the html will have these elements
    # cityCss = 'div#location h1'
    # weatherConditionCss = 'div#curCond span.wx-value'
    # weatherTempCss = '#curTemp span.wx-data span.wx-value'
    # weatherScaleCss = '#curTemp span.wx-data span.wx-unit'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    # print(condition, temp, scale, loc)
    # return a tuple...
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def find_city_and_state(location: str):
    parts = location.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
