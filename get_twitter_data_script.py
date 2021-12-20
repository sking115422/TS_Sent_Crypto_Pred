

import twint as t
from datetime import date
from datetime import datetime as dt
import os
from os.path import exists

#To make twint run inside juypter notebook
import nest_asyncio 

nest_asyncio.apply()


today = date.today()
today = str(today)
print("Today's date:", today)

now = dt.now()

hour = now.strftime("%H_%M_%S")
hour = str(hour)
print(hour)

path = "./data/twitter/" + today

if exists(path) == False:
    os.mkdir(path)

    path_btc = "./data/twitter/" + today + "/BTC"
    path_eth = "./data/twitter/" + today + "/ETH"
    path_xrp = "./data/twitter/" + today + "/XRP"
    path_gen = "./data/twitter/" + today + "/gen"

    if exists(path_btc) == False:
        os.mkdir(path_btc)
        
    if exists(path_eth) == False:
        os.mkdir(path_eth)
        
    if exists(path_xrp) == False:
        os.mkdir(path_xrp)
        
    if exists(path_gen) == False:
        os.mkdir(path_gen)


##BTC Tweets Gatherer

# Search List
s_list = ['#BTC', '#bitcoin']

for dat_thang in s_list:

    # Configure
    c = t.Config()
    c.Search = dat_thang
    c.Limit = "1500"
    c.Lang = "en"
    c.Store_json = True
    c.Output = "./data/twitter/" + today + "/BTC/" + dat_thang + "-" + hour + ".json"

    # Run
    t.run.Search(c)


##ETH Tweets Gatherer

# Search List
s_list = ['#ETH', '#ethereum']

for dat_thang in s_list:

    # Configure
    c = t.Config()
    c.Search = dat_thang
    c.Limit = "1500"
    c.Lang = "en"
    c.Store_json = True
    c.Output = "./data/twitter/" + today + "/ETH/" + dat_thang + "-" + hour + ".json"

    # Run
    t.run.Search(c)
    

##XRP Tweets Gatherer

# Search List
s_list = ['#XRP', '#ripple']

for dat_thang in s_list:

    # Configure
    c = t.Config()
    c.Search = dat_thang
    c.Limit = "1500"
    c.Lang = "en"
    c.Store_json = True
    c.Output = "./data/twitter/" + today + "/XRP/" + dat_thang + "-" + hour + ".json"

    # Run
    t.run.Search(c)
    

##General Crypto Info Gatherer

# Search List
s_list = ['#crypto', '#cryptocurrency', '#cryptoworld', '#cryptotrading', '#cryptocurrencies', '#cryptonews']

for dat_thang in s_list:

    # Configure
    c = t.Config()
    c.Search = dat_thang
    c.Limit = "500"
    c.Lang = "en"
    c.Store_json = True
    c.Output = "./data/twitter/" + today + "/gen/" + dat_thang + "-" + hour + ".json"

    # Run
    t.run.Search(c)


