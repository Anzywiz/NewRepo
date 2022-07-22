from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = "https://tieba.baidu.com/f?kw=%E5%AE%81%E5%BE%B7%E6%97%B6%E4%BB%A3%E6%96%B0%E8%83%BD%E6%BA%90&ie=utf-8"
driver.get(url)
row = []
rep_nos = []
topics = []
authors = []
for rep_no in driver.find_elements(by=By.XPATH, value='//span[@class="threadlist_rep_num center_text"]'):
    rep_nos.append(rep_no.text)
for topic in driver.find_elements(by=By.XPATH, value='//a[@class="j_th_tit "]'):
    topics.append(topic.text)
for author in driver.find_elements(by=By.XPATH, value='//span[@class="frs-author-name-wrap"]'):
    authors.append(author.text)

file = open('tieba_scrape.csv', 'w', newline='', encoding='UTF8')
writer = csv.writer(file)
writer.writerow(['Number of post', 'Topic title', 'Authors'])
for r, t, a in zip(rep_nos, topics, authors):
    writer.writerow([r, t, a])
file.close()
driver.quit()

print(rep_nos)
print(len(rep_nos))
print(topics)
print(len(topics))
print(authors)
print(len(authors))







