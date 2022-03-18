from filecmp import cmp
from itertools import count
import pdb
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# df = pd.read_csv('/Users/qruzz/Dev/scrape_hdfc/src/ind_nifty500list.csv', index_col=0)
# company_symbol = df['Symbol']
# for symbol in company_symbol:
#     url = ("https://www.screener.in/company/%s" %symbol)
url = "https://www.screener.in/company/3MINDIA/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

company_name = driver.find_elements(by=By.XPATH, value="//main[@class='container']/div/div/div[@class='flex-row flex-wrap flex-align-center flex-grow']/h1") if True else " "
marcket_cap = driver.find_elements(by=By.XPATH, value="//ul[@id='top-ratios']/li[@class='flex flex-space-between'][1]/span[@class='nowrap value']") if True else " "
current_price = driver.find_elements(by=By.XPATH, value="//ul[@id='top-ratios']/li[@class='flex flex-space-between'][2]/span[@class='nowrap value']") if True else " "
high_low = driver.find_elements(by=By.XPATH, value="//ul[@id='top-ratios']/li[@class='flex flex-space-between'][3]/span[@class='nowrap value']") if True else " "
stock_pe = driver.find_elements(by=By.XPATH, value="//ul[@id='top-ratios']/li[@class='flex flex-space-between'][4]/span[@class='nowrap value']") if True else " "
book_value = driver.find_elements(by=By.XPATH, value="//ul[@id='top-ratios']/li[@class='flex flex-space-between'][5]/span[@class='nowrap value']") if True else " "
dividend_yield = driver.find_elements(by=By.XPATH, value="//ul[@id='top-ratios']/li[@class='flex flex-space-between'][6]/span[@class='nowrap value']") if True else " "
roce = driver.find_elements(by=By.XPATH, value="//ul[@id='top-ratios']/li[@class='flex flex-space-between'][7]/span[@class='nowrap value']") if True else " "
roe = driver.find_elements(by=By.XPATH, value="//ul[@id='top-ratios']/li[@class='flex flex-space-between'][8]/span[@class='nowrap value']") if True else " "
face_value = driver.find_elements(by=By.XPATH, value="//ul[@id='top-ratios']/li[@class='flex flex-space-between'][9]/span[@class='nowrap value']") if True else " "

    

# print("Company name : %s" %company_name[0].text)
result = []

company_data = {'Company Name':company_name[0].text,
                    'Marcket Cap':marcket_cap[0].text,
                    'Current Price':current_price[0].text,
                    'High/Low':high_low[0].text,
                    'Stock P/E':stock_pe[0].text,
                    'Book Value':book_value[0].text,
                    'Dividend Yield':dividend_yield[0].text,
                    'Roce':roce[0].text,
                    'Roe':roe[0].text,
                    'Face Value':face_value[0].text,
                    }

result.append(company_data)
df = pd.DataFrame(result)
print(company_name[0].text)
print(df)

peer_compoarision_result = []
peer_row = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr")
for k in range(2, len(peer_row)+1):
    name = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr[%s]/td[2]/a" %k) if True else " "
    cmp_rs = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr[%s]/td[3]" %k) if True else " "
    pe = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr[%s]/td[4]" %k) if True else " "
    mar_cap_rs_cr = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr[%s]/td[5]" %k) if True else " "
    div_yld = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr[%s]/td[6]" %k) if True else " "
    np_qtr_rs_cr = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr[%s]/td[7]" %k) if True else " "
    qtr_profit_var = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr[%s]/td[8]" %k) if True else " "
    sales_qtr_rs_cr = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr[%s]/td[9]" %k) if True else " "
    qtr_sales_var = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr[%s]/td[10]" %k) if True else " "
    roce_1  = driver.find_elements(by=By.XPATH, value="//div[@id='peers-table-placeholder']/div[3]/table/tbody/tr[%s]/td[11]" %k) if True else " "

    
    peer_comaparision = {'Name':name[0].text,
                            'CMP Rs':cmp_rs[0].text,
                            'P/E':pe[0].text,
                            'Mar Cap Rs.Cr.':mar_cap_rs_cr[0].text,
                            'Div Yld':div_yld[0].text,
                            'NP Qtr Rs.Cr.':np_qtr_rs_cr[0].text,
                            'Qtr Profit Var':qtr_profit_var[0].text,
                            'Sales Qtr Rs.Cr.':sales_qtr_rs_cr[0].text,
                            'Qtr Sales Var':qtr_sales_var[0].text,
                            'ROCE':roce_1[0].text,
                            }
    peer_compoarision_result.append(peer_comaparision)

df_peer = pd.DataFrame(peer_compoarision_result)
print("Peer Comparision")
print(df_peer) 

def fetch_results(header, row_length, row_values):
    data_dict = {}
    heading = driver.find_elements(by=By.XPATH, value=header) if True else    []
    for i in range(len(heading)):
        header_index = i+1
        p = []
        get_length = driver.find_elements(by=By.XPATH, value=row_length)
        for t in range(1, len(get_length)+1):
            qu = driver.find_elements(by=By.XPATH, value=row_values %(t ,header_index)) if True else []
            for m in range(len(qu)):
                p.append(qu[m].text)
        data_dict.update({heading[i].text: p})
    data1 = pd.DataFrame(data=data_dict)
    print(data1)


def fetch_quarterly_results():
    header = "//section[@id='quarters']/div[2]/table/thead/tr/th"
    row_length = "//section[@id='quarters']/div[2]/table/tbody/tr"
    row_values = "//section[@id='quarters']/div[2]/table/tbody/tr[%s]/td[%s]"
    fetch_results(header, row_length, row_values)

def fetch_profit_and_loss():
    header = "//section[@id='profit-loss']/div[2]/table/thead/tr/th"
    row_length = "//section[@id='profit-loss']/div[2]/table/tbody/tr"
    row_values = "//section[@id='profit-loss']/div[2]/table/tbody/tr[%s]/td[%s]"
    fetch_results(header, row_length, row_values)

def fetch_balance_sheet():
    header = "//section[@id='balance-sheet']/div[2]/table/thead/tr/th"
    row_length = "//section[@id='balance-sheet']/div[2]/table/tbody/tr"
    row_values = "//section[@id='balance-sheet']/div[2]/table/tbody/tr[%s]/td[%s]"
    fetch_results(header, row_length, row_values)


def fetch_cash_flows():
    header = "//section[@id='cash-flow']/div[2]/table/thead/tr/th"
    row_length = "//section[@id='cash-flow']/div[2]/table/tbody/tr"
    row_values = "//section[@id='cash-flow']/div[2]/table/tbody/tr[%s]/td[%s]"
    fetch_results(header, row_length, row_values)


def fetch_ratios():
    header = "//section[@id='ratios']/div[2]/table/thead/tr/th"
    row_length = "//section[@id='ratios']/div[2]/table/tbody/tr"
    row_values = "//section[@id='ratios']/div[2]/table/tbody/tr[%s]/td[%s]"
    fetch_results(header, row_length, row_values)


def fetch_share_holdings():
    header = "//section[@id='shareholding']/div[2]/table/thead/tr/th"
    row_length = "//section[@id='shareholding']/div[2]/table/tbody/tr"
    row_values = "//section[@id='shareholding']/div[2]/table/tbody/tr[%s]/td[%s]"
    fetch_results(header, row_length, row_values)


fetch_quarterly_results()
fetch_profit_and_loss()
fetch_balance_sheet()
fetch_cash_flows()
fetch_ratios()
fetch_share_holdings()