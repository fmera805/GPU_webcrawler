import requests
import os
from bs4 import BeautifulSoup
from Tkinter import *

def log_writer(x):
    with open('Logbook.txt','a') as log_file:
        log_file.write('\n')
        log_file.write(x)
        log_file.write('\n')
        log_file.close()

def nvidia1080TI():
    page=1
    log_writer(80 * '*')
    log_writer("1080TI Log")
    log_writer(80 * '*')
    print("Scanning for 1080 TI")

    while page <= 1:
        url = 'https://www.ebay.com/sch/i.html?_sop=1&_from=R40&_sacat=0&_nkw=1080+ti+gtx&_pgn='+ str(page)

        source_code=requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'vip'}):
            href = link.get('href')
            title = link.string
            print('')
            print(150 * '-')
            log_writer(80 * '-')
            log_writer(href)
            print('')
            get_Item_Title(href)
            print(href)
            get_Item_Price(href)
            get_BidPrice(href)
            get_Time_Left(href)
            get_single_item_data(href)
            get_Item_Condition(href)

        page +=1

def nvidia1080():
    page=1
    log_writer(80 * '*')
    log_writer("1080 Log")
    log_writer(80 * '*')
    print("Scanning for 1080")
    while page <= 1:
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_sop=1&_nkw=1080+gtx&_pgn='+ str(page)

        source_code=requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'vip'}):
            href = link.get('href')
            title = link.string
            print('')
            print(150 * '-')
            log_writer(80 * '-')
            log_writer(href)
            print('')
            get_Item_Title(href)
            print(href)
            get_Item_Price(href)
            get_BidPrice(href)
            get_Time_Left(href)
            get_single_item_data(href)
            get_Item_Condition(href)
        page +=1
    return

def nvidia1070TI():
    page=1
    log_writer(80 * '*')
    log_writer("1070TI Log")
    log_writer(80 * '*')
    print("Scanning for 1070 TI")
    while page <= 1:
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_sop=1&_nkw=1070+ti&_pgn='+ str(page)

        source_code=requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'vip'}):
            href = link.get('href')
            title = link.string
            print('')
            print(150 * '-')
            log_writer(80 * '-')
            log_writer(href)
            print('')
            get_Item_Title(href)
            print(href)
            get_Item_Price(href)
            get_BidPrice(href)
            get_Time_Left(href)
            get_single_item_data(href)
            get_Item_Condition(href)
        page +=1

def nvidia1070():
    page = 1
    log_writer(80 * '*')
    log_writer("1070 Log")
    log_writer(80 * '*')
    print("Scanning for 1070")
    while page <= 1:
        url = 'https://www.ebay.com/sch/i.html?_sop=1&_from=R40&_sacat=0&_nkw=1070&_pgn=' + str(page)

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'vip'}):
            href = link.get('href')
            title = link.string
            print('')
            print(150 * '-')
            log_writer(80 * '-')
            log_writer(href)
            print('')
            get_Item_Title(href)
            print(href)
            get_Item_Price(href)
            get_BidPrice(href)
            get_Time_Left(href)
            get_single_item_data(href)
            get_Item_Condition(href)
        page += 1

def nvidia1060_6GB():
    page = 1
    log_writer(80 * '*')
    log_writer("1060 6GB Log")
    log_writer(80 * '*')
    print("Scanning for 1060 6GB")
    while page <= 1:
        url = '1060 6gb https://www.ebay.com/sch/i.html?_sop=1&_from=R40&_sacat=0&_nkw=1060+6gb&_pgn=' + str(page)

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'vip'}):
            href = link.get('href')
            title = link.string
            print('')
            print(150 * '-')
            log_writer(80 * '-')
            log_writer(href)
            print('')
            get_Item_Title(href)
            print(href)
            get_Item_Price(href)
            get_BidPrice(href)
            get_Time_Left(href)
            get_single_item_data(href)
            get_Item_Condition(href)
        page += 1

def amdRX580():
    page = 1
    log_writer(80 * '*')
    log_writer("RX580 Log")
    log_writer(80 * '*')
    print("Scanning for RX580")
    while page <= 1:
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_sop=1&_nkw=rx+580&_pgn=' + str(page)

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'vip'}):
            href = link.get('href')
            title = link.string
            print('')
            print(150 * '-')
            log_writer(80 * '-')
            log_writer(href)
            print('')
            get_Item_Title(href)
            print(href)
            get_Item_Price(href)
            get_BidPrice(href)
            get_Time_Left(href)
            get_single_item_data(href)
            get_Item_Condition(href)
        page += 1


def get_Item_Title(Item_Title):
    source_code = requests.get(Item_Title)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for Item_Title in soup.findAll('span', {'class': 'u-dspn'}):
        print(Item_Title.string)

def get_Item_Price(Item_Price):
    source_code = requests.get(Item_Price)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for Item_Price in soup.findAll('span', {'id': 'prcIsum'}):
        print('Buy It Now:')
        print(Item_Price.string)
        log_writer('Buy it now:')
        log_writer(str(Item_Price))

def get_BidPrice(item_BidPrice):
    source_code = requests.get(item_BidPrice)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for item_BidPrice in soup.findAll('span', {'id': 'prcIsum_bidPrice'}):
        print('Current Bid:')
        print(item_BidPrice.string)
        log_writer('Current bid:')
        log_writer(str(item_BidPrice))

def get_single_item_data(item_location):
    source_code = requests.get(item_location)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for item_location in soup.findAll('span', {'itemprop': 'availableAtOrFrom'}):
        print('Item Location:')
        print(item_location.string)


def get_Time_Left(item_Time):
    source_code = requests.get(item_Time)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for item_Time in soup.findAll('span', {'class': 'endedDate'}):
        print('End Time:')
        print(item_Time.string)

def get_Item_Condition(Item_condition):
    source_code = requests.get(Item_condition)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for Item_condition in soup.findAll('div', {'id': 'vi-itm-cond'}):
        print('Item Condition:')
        print(Item_condition.string)



main = Tk()
Label(main, text = "Please select a GPU:").grid(row=0, column=0, sticky=W, pady=4)
Button(main, text='1080TI', command=nvidia1080TI).grid(row=0, column=1, sticky=W, pady=4)
Button(main, text='1080', command=nvidia1080).grid(row=0, column=2, sticky=W, pady=4)
Button(main, text='1070TI', command=nvidia1070TI).grid(row=0, column=3, sticky=W, pady=4)
Button(main, text='1070', command=nvidia1070).grid(row=0, column=4, sticky=W, pady=4)
Button(main, text='1060 6GB', command=nvidia1060_6GB).grid(row=0, column=5, sticky=W, pady=4)
Button(main, text='RX580', command=amdRX580).grid(row=0, column=6, sticky=W, pady=4)

main.title('Spider GPU')

mainloop()