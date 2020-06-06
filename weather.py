import requests, bs4
import re
def weather_get(city):
	def appe(days):
		for i in days:
			weathers.append({
				"day": i.find('p', class_ = "weather__content_tab-day").get_text(strip = True),
				"date": i.find('p', class_ = "weather__content_tab-date day_red").get_text(strip = True) +' '+ i.find('p', class_ = "weather__content_tab-month").get_text(strip = True),
				"sky": i.find('label', class_ = "show-tooltip").get_text(strip = True),
				"t": i.find('div', class_ = "weather__content_tab-temperature").get_text(strip = True).replace('мин.', '').replace('макс.', ' ').split()
			})
	s=requests.get('https://sinoptik.com.ru/погода-'+city.lower())
	b=bs4.BeautifulSoup(s.text, "html.parser")
	if s.status_code != 200:
		return 'Error'
	first_days = b.findAll('div', class_ = "weather__content_tab current")
	sec_and_third_days = b.findAll('div', class_ = "weather__content_tab dateFree")
	other_days = b.findAll('div', class_ = "weather__content_tab")
	weathers = []
	appe(first_days)
	appe(sec_and_third_days)
	appe(other_days)
	return(weathers)
	bs4.BeautifulSoup