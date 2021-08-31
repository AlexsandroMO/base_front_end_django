import requests
from bs4 import BeautifulSoup
import pandas as pd


def rateall():
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
    }

    links = ('https://www.melhorcambio.com/ipca',
            'https://www.melhorcambio.com/cdi',
            'https://www.melhorcambio.com/taxa-selic',
            'https://www.melhorcambio.com/igpm',)

    #IPCA | CDI | SELIC | IGPM
    def fixed_rate(header, links, rate):

        response_object = requests.get(links[rate], headers=header)
        search_soup = BeautifulSoup(response_object.text, features='html.parser')
        read_elems = search_soup.find_all('td', 'tdvalor')

        list_rate = []
        for i in read_elems:
            conv = i.text.replace(',', '.').replace(' %', '')
            list_rate.append(round(float(conv),2))
            
        return list_rate


    rate_all = []
    for i in range(0, 4):
        rate_all.append(fixed_rate(header, links, i))

    #POUPANÇA
    response_object = requests.get('https://www.idinheiro.com.br/calculadoras/calculadora-rendimento-da-poupanca/', headers=header)
    read_elems = BeautifulSoup(response_object.text, features='html.parser').find_all('input','input__sem_cifrao')
    text = str(read_elems[0]).split(' ')
    poup = 0
    for i in text:
        if i[:5] == 'value':
            poup = round(float(i[7:-3].replace(',','.')),2)

    rate_rate = [ 
                ['IPCA', rate_all[0][2], '(ano)'],
                ['CDI A', (rate_all[1][1]) * 12, '(mes)'],
                ['CDI M', rate_all[1][1], '(mes)'],
                ['CDI D', (rate_all[1][1])/30, '(dia)'],
                ['SELIC', rate_all[2][3], '(ano)'],
                ['IGPM', rate_all[3][2], '(ano)'],
                ['POUPANÇA A', round(poup,2), '(ano)'],
                ['POUPANÇA M', round(poup/12,4), '(mes)'],
                ['POUPANÇA D', round((poup/12)/30,4), '(dia)']
                ]

    rate_data = pd.DataFrame(data=rate_rate, columns=['RATE','VALUE','TERM'])

    #----------------------------------------------
    response_object = requests.get('https://www.poupardinheiro.com.br/financas/734-o-que-e-cdi-valor-hoje', headers=header)
    search_soup = BeautifulSoup(response_object.text, features='html.parser')
    read_title = search_soup.find_all('div','title')
    read_value = search_soup.find_all('div','valor')
    read_variable = search_soup.find_all('div','variacao')

    read_all = []
    for i in range(len(read_title)):
        test_value = read_value[i].text.replace('\n','')
        read_all.append([read_title[i].text, test_value[:test_value.find(',')+3], read_variable[i].text])

    result_coins = []
    for a in read_all[1:5]:
        result_coins.append(a)
        read_all[0][1] = read_all[0][1][:read_all[0][1].find('pts')+3]
        result_coins.append(read_all[0])
    
    for a in read_all[5:13]:
        result_coins.append(a)

    stock_exchange = pd.DataFrame(data=result_coins,columns=['ACTIONS','VALUES','RANGE'])

    return [stock_exchange, rate_data, result_coins]



def result_calc(num_calc, num_rate, num_month):

    rate_all = rateall()

    cdi_year = ((rate_all[1]['VALUE'][2]) * 12)
    cdi_month = ((rate_all[1]['VALUE'][3]) * num_month)

    print('-------- ', rate_all[1]['VALUE'][2])

    #rendimento CDI 100% EM X MESES
    rend_cdi_oh = (cdi_month * num_calc) / 100
    result1 = num_calc + rend_cdi_oh

    #rendimento CDI acima de 100% EM X MESES
    rend_cdi_x = (cdi_month * (num_rate / 100) * num_calc) / 100
    result2 = num_calc + rend_cdi_x

    #rendimento CDI 100% EM 12 MESES
    rend_cdi_oh = (cdi_year * num_calc) / 100
    result3 = num_calc + rend_cdi_oh

    #rendimento CDI acima de 100% EM 12 MESES
    rend_cdi_x = (cdi_year * (num_rate / 100) * num_calc) / 100
    result4 = num_calc + rend_cdi_x

    return [result1, result2, result3, result4]





