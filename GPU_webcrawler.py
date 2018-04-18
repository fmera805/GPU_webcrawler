import requests
from bs4 import BeautifulSoup

print("Nvidia Webcrawler")
def trade_spider(max_pages):
    page=1
    while page <= max_pages:
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_sop=1&_nkw=1080+gtx&_pgn='+ str(page)

        # 1080  https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_sop=1&_nkw=1080+gtx&_pgn=
        # 1080 ti  https://www.ebay.com/sch/i.html?_sop=1&_from=R40&_sacat=0&_nkw=1080+ti+gtx&_pgn=
        # 1060 6gb https://www.ebay.com/sch/i.html?_sop=1&_from=R40&_sacat=0&_nkw=1060+6gb&_pgn=
        # 1070 https://www.ebay.com/sch/i.html?_sop=1&_from=R40&_sacat=0&_nkw=1070&_pgn=
        # 1070 ti https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_sop=1&_nkw=1070+ti&_pgn=
        # rx 580 https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_sop=1&_nkw=rx+580&_pgn=

        source_code=requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'vip'}):
            href = link.get('href')
            title = link.string
            print('')
            print(150 * '-')
            print('')
            get_Item_Title(href)
            print(href)
            get_Item_Price(href)
            get_BidPrice(href)
            get_Time_Left(href)
            get_single_item_data(href)
            get_Item_Condition(href)
        page +=1

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

def get_BidPrice(item_BidPrice):
    source_code = requests.get(item_BidPrice)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_BidPrice in soup.findAll('span', {'id': 'prcIsum_bidPrice'}):
        print('Current Bid:')
        print(item_BidPrice.string)

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

trade_spider(10)