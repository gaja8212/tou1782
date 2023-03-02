import telepot
from bs4 import BeautifulSoup
import urllib.request
import ccxt
import threading
import json
import requests

token = '6290346834:AAHEfFXBl4AO8Rwawew6gS6gdQuHwEg7NkA'
mc = '6024674971'
bot = telepot.Bot(token)


def UPBN_final():
    '''#환율
    url_usd = "https://finance.naver.com/marketindex/"
    res_usd = urllib.request.urlopen(url_usd).read()
    soup_usd = BeautifulSoup(res_usd, "html.parser")
    usd = soup_usd.find('select', id='select_to',class_="selectbox-source")
    currency ={}
    for opt in usd.find_all('option'):
        currency[opt.text[-3:]]=float(opt['value'])

    exchange = currency['USD']'''

    binance =ccxt.binance()
    upbit =ccxt.upbit()

    #업비트 수수료
    UPlist1 = {'HIVE' : 0.01, 'SHIB' : 710000, 'ZRX' : 6.6, 'STPT': 32.4, 'WAVES' : 0.001}
    UPlist2 = {'MANA' : 1.9, 'ATOM' : 0.01, 'STMX': 358.1, 'PUNDIX' : 2.8}
    UPlist3 = {'MBL' : 172, 'STEEM' : 0.01, 'DOT' : 0.1, 'DOGE': 12, 'MATIC' : 2.7}
    UPlist4 = {'ETC' : 0.01, 'OMG' : 0.9, 'QTUM' : 0.1, 'ICX': 0.01}
    UPlist5 = {'ETH' : 0.01, '1INCH' : 3.1, 'PLA' : 4, 'LSK': 0.1, 'ADA' : 0.5}
    UPlist6 = {'XTZ' : 0.1, 'POWR' : 8.9, 'JST' : 30, 'ALGO': 0.1, 'XEM' : 4}
    UPlist7 = {'ZIL' : 0.5, 'ANKR' : 60.1, 'STX' : 3, 'ARDR': 2, 'BCH' : 0.001} 
    UPlist8 = {'WAXP' : 0, 'THETA' : 0.5, 'AVAX' : 0.01, 'SAND': 2, 'MTL' : 1.9}
    UPlist9 = {'XEC' : 1000, 'HIFI' : 3.5, 'MTL' : 1.9, 'POLYX' : 0.4}
    UPlist10 = {'VET' : 32.6, 'ENJ' : 3.6, 'T': 93.6, 'ONG' : 1, 'BTC' : 0.0009}
    UPlist11 = {'STRAX' : 0.2, 'IOTA' : 0, 'TRX': 1, 'TFUEL' : 2, 'EOS' : 0}
    UPlist12 = {'XRP' : 1, 'XLM' : 0.01, 'LINK': 0.3, 'CELO' : 0.8, 'ELF' : 4.3}
    UPlist13 = {'NEAR' : 0.2, 'AXS' : 0.1, 'APT' : 0.01, 'FLOW' : 0.03}
    UPlist14 = {'SNT':183.8, 'AERGO':23.7, 'KNC':2.3, 'NEO':0.1, 'BAT':5.2, 'AAVE':0.1, 'SXP':0.2, 'HBAR':0.01, 'CHZ':18.2, 'STORJ':3.8, 'CVC':16.5, 'GLM':8.4, 'ARK':0.1, 'QKC':0.01, 'IQ':0, 'LOOM':56.7, 'GAS':0.5}

    #'KAVA' : 0.4, 'GMT': 0.5, 'SOL': 0.01, 'SC' : 0.1
    
    #바이낸스 수수료
    BNlist1 = {'HIVE' : 0.01, 'SHIB' : 277919, 'ZRX' : 15, 'STPT': 87}
    BNlist2 = {'MANA' : 5.29, 'ATOM' : 0.004, 'STMX': 609, 'PUNDIX' : 7.76}
    BNlist3 = {'MBL' : 3.27, 'STEEM' : 0.01, 'DOT' : 0.08, 'DOGE': 4, 'MATIC' : 9.72}
    BNlist4 = {'ETC' : 0.008, 'OMG' : 2.33, 'QTUM' : 0.01, 'ICX': 0.02}
    BNlist5 = {'ETH' : 0.0012, '1INCH' : 6.83, 'PLA' : 8, 'LSK': 0.1, 'ADA' : 0.8}
    BNlist6 = {'XTZ' : 0.1, 'POWR' : 18, 'JST' : 50, 'ALGO': 0.008, 'XEM' : 4}
    BNlist7 = {'ZIL' : 0.2, 'ANKR' : 137, 'STX' : 1.5, 'ARDR': 2, 'BCH' : 0.00064} 
    BNlist8 = {'WAXP' : 2, 'THETA' : 0.12, 'AVAX' : 0.008, 'SAND': 5.31, 'MTL' : 6.46}
    BNlist9 = {'XEC' : 1000, 'HIFI' : 7.67, 'MTL' : 3.23, 'POLYX' : 5}
    BNlist10 = {'VET' : 20, 'ENJ' : 8.49, 'T': 90, 'ONG' : 0.037, 'BTC' : 0.0002}
    BNlist11 = {'STRAX' : 0.1, 'IOTA' : 0.5, 'TRX': 1, 'TFUEL' : 2.3, 'EOS' : 0.08}
    BNlist12 = {'XRP' : 0.2, 'XLM' : 0.02, 'LINK': 0.56, 'CELO' : 0.001, 'ELF' : 1}
    BNlist13 = {'NEAR' : 0.01, 'AXS' : 0.36, 'APT' : 0.01, 'FLOW' : 0.008}

    #'KAVA' : 0.01, 'GMT': 0.36, 'SOL': 0.008, 'WAVES' : 0.0016, 'SC' : 0.1

    #업비트에서 바이낸스
    UPBNDic = {}

    UPlistA = {**UPlist1, **UPlist2, **UPlist3, **UPlist4}
    UPlistB = {**UPlist5,**UPlist6, **UPlist7, **UPlist8, **UPlist9}
    UPlistC = {**UPlist10, **UPlist11, **UPlist12, **UPlist13, **UPlist14}

    UPlistABC = {**UPlistA, **UPlistB, **UPlistC}

    for symbol, fee in UPlistA.items():
        BN_aCOIN = binance.fetch_ticker(symbol + "/USDT")
        UP_aCOIN = upbit.fetch_ticker(symbol+'/KRW')
        UP_aCOIN_Fee = fee
        UPBNDic[symbol] = (100000*0.9995/UP_aCOIN['last']-UP_aCOIN_Fee)*0.999*BN_aCOIN['bid']

    UPBNDic0 = {v:k for k,v in UPBNDic.items()}
    UPBNDic1 = list(UPBNDic.values())
    UPBNDic2 = sorted(UPBNDic1)
    
    #바이낸스에서 업비트
    BNUPDic = {}
    BNlistA = {**BNlist1, **BNlist2, **BNlist3, **BNlist4}
    BNlistB = {**BNlist5, **BNlist6, **BNlist7, **BNlist8, **BNlist9}
    BNlistC = {**BNlist10, **BNlist11, **BNlist12, **BNlist13}

    BNlistABC = {**BNlistA,**BNlistB,**BNlistC}

    for symbol, fee in BNlistABC.items():
        BN_bCOIN = binance.fetch_ticker(symbol + "/USDT")
        UP_bCOIN = upbit.fetch_ticker(symbol+"/KRW")
        UP_bCOIN_Fee = fee
        BNUPDic[symbol] = (100*0.999/BN_bCOIN['ask']-fee)*(0.9995)*UP_bCOIN['last']

    BNBUSDlist={'SNT':142, 'AERGO':30, 'KNC':4, 'NEO':0, 'BAT':14, 'AAVE':0.05, 'SXP':13, 'HBAR':0.8, 'CHZ':28, 'STORJ':10, 'CVC':35, 'GLM':16, 'ARK':0.2, 'QKC':371, 'IQ':50, 'LOOM':77, 'GAS':0.05}

    for symbol, fee in BNBUSDlist.items():
        BN_bCOIN = binance.fetch_ticker(symbol + "/BUSD")
        UP_bCOIN = upbit.fetch_ticker(symbol+"/KRW")
        UP_bCOIN_Fee = fee
        BNUPDic[symbol] = (100*0.999/BN_bCOIN['ask']-fee)*(0.9995)*UP_bCOIN['last']

    BNUPDic0 = {v:k for k,v in BNUPDic.items()}
    BNUPDic1 = list(BNUPDic.values())
    BNUPDic2 = sorted(BNUPDic1)
    
    UPCOIN = "업비트 > 바이낸스\n"+str(UPBNDic0.get(UPBNDic2[-1]))+" 100000원 > "+str(round(UPBNDic2[-1]))+'달러'
    BNCOIN = "바이낸스 > 업비트\n"+str(BNUPDic0.get(BNUPDic2[-1]))+" 100달러 > "+str(round(BNUPDic2[-1]))+'원'

    bot.sendMessage(mc, UPCOIN+'\n'+BNCOIN)
    print('end')

    threading.Timer(60, UPBN_final).start()

UPBN_final()