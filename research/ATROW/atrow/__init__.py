import atexit

from bs4 import BeautifulSoup
from scapy.all import *
from selenium import webdriver

driver = webdriver.Firefox()
atexit.register(driver.quit)

# a. File compression techniques for image optimization.
# b. Browser caching.
# c. Reduced number of redirects.
# d. Reduced usage of non-blocking JavaScript.
# e. Images of variable sizes depending on the device being used by the customer

def trace_route(url):
	'''
	This is a tracert implementation for finding the list of visible routes.
	'''
	target = [primary_url]
	result, unans = traceroute(target, maxttl = 32)
	print(result)
	print(unans)

def analyze_dom(dom_str):
	'''
	This is the DOM Analysis component. This will be worked upon later on.
	'''
	soup = BeautifulSoup(dom_str)
	anchors = soup.find_all(a)
	metas = soup.findall(metas)
	print(anchros, metas)

def preliminary_load(url):
	'''
	This is to get the first load statistics.
	'''
	stats = {}
	driver.get(url)
	# driver.manage().window().minimize()
	navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
	responseStart = driver.execute_script("return window.performance.timing.responseStart")
	domComplete = driver.execute_script("return window.performance.timing.domComplete")
	stats['backend_load_time'] = responseStart - navigationStart
	stats['frontend_performance'] = domComplete - responseStart
	return driver.page_source, stats

def run():
	primary_url = 'https://extra.com/'
	main_dom, stats = preliminary_load(primary_url)
	metas, links = analyze_dom(main_dom)
	# print(main_dom)
	cdns = set([link for link in links if 'cdn' in link])
	trace_route(primary_url)
	analyze_ui(primary_url)
