import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

driver = Chrome()
driver.get('https://www.twitter.com/login')

driver = Chrome()
driver.get('https://www.twitter.com/login')

search_input = driver.find_element_by_xpath('//input[@aria-label="Serch query"]')
search_input.send_keys('#Coronavirus')
search_input.send_keys(Keys.RETURN)

driver.find_element_by_link_text('Latest').click()

cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
cards = cards[7]
# username
card.find_element_by_xpath('.//span').text
# twitter handle
card.find_element_by_xpath('.//span[contains(text(), "@")]')
# postdate
card.find_element_by_xpath('.//time').get_attribute('datetime')
# content of tweet
comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
# reply count
card.find_element_by_xpath('.//div[@data-testid="reply"]').text
# retweet
card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
# likes
card.find_element_by_xpath('.//div[@data-testid="like"').text

def get_tweet_card(card):
	username = card.find_element_by_xpath('.//span').text
	handle = card.find_element_by_xpath('.//span[contains(text(), "@")]')
	try:
		postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
	except NoSuchElementException
		return
	comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
	responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
	text = comment + responding
	reply_count = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
	retweet_count = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
	like_count = card.find_element_by_xpath('.//div[@data-testid="like"').text

	tweet = (username, handle, postdate, text, reply_count, retweet_count, like_count)
	return tweet
  
  tweet_data = []

for card in cards:
	data = get_tweet_data(card)
		if data:
			tweet_data.append(data)
      
 
