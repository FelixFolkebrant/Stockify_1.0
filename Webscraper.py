import csv
import selenium
from time import sleep as s
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def all_stocks(stocks=100, mode=1):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.set_window_position(-10000,0)
    modes = {"market-cap-large":1, "market-cap-small":2, "top-gainers":3, "biggest-losers":4, "growth":5, "dividend-yield-high":6}
    mode = list(modes.keys())[list(modes.values()).index(mode)]
    tickers = []
    for page in range(1, int(stocks/24)):
        print("Loading page")
        driver.get(f'https://simplywall.st/stocks/se/{mode}?page={page}')
        try:
            elem = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/section/div[1]/div[1]/section/div/table/tbody/tr[20]/td[2]/a/b')) #This is a dummy element
            )
        finally:
            for stock in range(1,25):
                try:
                    tickers.append(str(driver.find_element_by_xpath(f'/html/body/div/div/div[2]/section/div[1]/div[1]/section/div/table/tbody/tr[{stock}]/td[2]/a/b').text).replace(" ", "-"))
                    os.system("cls")
                    print(f"{stock+((page-1)*24)}/{(int(stocks/24)-1)*24}")
                except: 
                    pass
    driver.quit()
    with open("potential_stocks.csv","w",newline="") as f:
        cw = csv.writer(f)
        for x in tickers:
            cw.writerow([x])
    print(f"{len(tickers)} tickers have been loaded to potential_stocks.csv")
def industry_stocks(industry, stocks=100, mode=1):
    driver = webdriver.Chrome('chromedriver.exe')
    # driver.set_window_position(-10000,0)
    modes = {"market-cap-large":1, "market-cap-small":2, "top-gainers":3, "biggest-losers":4, "growth":5, "dividend-yield-high":6}
    industries = {"automobiles":1, "banks":2, "":3, "capital-goods":4, "commercial-services":5, "consumer-durables":6,"consumer-retailing":7,"consumer-services":8,"diversified-financials":9,"energy":10,"food-beverage-tobacco":11,"healthcare":12,"household":13, "materials":14, "media":15,"pharmaceuticals-biotech":17,"real-estate":18,"retail":19,"semiconductors":20,"software":21,"tech":22,"telecom":23,"transportation":24,"utilities":25}
    mode = list(modes.keys())[list(modes.values()).index(mode)]
    industry = list(industries.keys())[list(industries.values()).index(mode)]
    print(mode, industry)
    tickers = []
    for page in range(1, int(stocks/24)):
        print("Loading page")
        driver.get(f'https://simplywall.st/stocks/se/{industry}/{mode}?page={page}')
        try:
            elem = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/section/div[1]/div[1]/section/div/table/tbody/tr[20]/td[2]/a/b')) #This is a dummy element
            )
        finally:
            for stock in range(1,25):
                try:
                    tickers.append(str(driver.find_element_by_xpath(f'/html/body/div/div/div[2]/section/div[1]/div[1]/section/div/table/tbody/tr[{stock}]/td[2]/a/b').text).replace(" ", "-"))
                    print(driver.find_element_by_xpath(f'//*[@id="root"]/div/div[2]/section/div[1]/div[1]/section/div/table/tbody/tr[{stock}]/td[11]/a/span').text)
                    os.system("cls")
                    print(f"{stock+((page-1)*24)}/{(int(stocks/24)-1)*24}")
                except: 
                    pass
    driver.quit()
    with open("potential_stocks.csv","w",newline="") as f:
        cw = csv.writer(f)
        for x in tickers:
            cw.writerow([x])
    print(f"{len(tickers)} tickers have been loaded to potential_stocks.csv")
industry_stocks(1)
