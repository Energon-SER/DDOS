import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from matplotlib import style
import plotly.express as px
import plotly.graph_objects as go
#from matplotlib import pylab as plt
import ast
import os


def smo(k, n, lam, mu):
    # k – число каналов, занятых обслуживанием запросов, 
    # n – емкость буфера (16384 по умол, 16384/0.4 сек задержки = 41 Мб/сек = 3.3), 
    # lam – интенсивность входного потока запросов λ, mu – производительность обработки запросов

    # Вычисление коэффициента загрузки ρ
    p = lam / mu 
    rez = f"Коэффициент загрузки ρ = {p:.4f}\n" # результат расчетов 
    # будет представляться в десятичном виде

    # Коэффициент загрузки СМО
    ps = p / k
    rez += f"Коэффициент загрузки СМО ps = {ps:.4f}\n"

    p0 = 1 # Вероятность простоя
    numer = 1 # Счетчик числителя
    denom = 1 # Счетчик знаменателя
    for j in range(1, k): # расчет вероятности простоя при 
        # использовании цикла со счетчиком. С целью упрощения 
        # расчетов и уменьшения их количества числители и знаменатели 
        # дробей накапливаются независимо друг от друга и 
        # формируются на каждой итерации цикла
        numer *= p
        denom *= j
        p0 += numer / denom
    numer *= p * (1 - ps ** (n + 1))
    kfakt = denom * k
    p0 += numer / (kfakt * (1 - ps))
    p0 = 1 / p0
    rez += f"Вероятность простоя p0 = {p0:.4f}\n"

    # Вероятность отказа в обслуживании запроса p_den
    pden = (p ** (k + n)) * p0 / (kfakt * (k ** n))
    rez += f"Вероятность отказа в обслуживании pden = {pden:.4f}\n"

    # Определяем среднее число занятых каналов k_ch
    kch = p * (1 - pden)
    rez += f"Среднее число занятых каналов kch = {kch:.4f}\n"

    # Определяем среднее число заявок в очереди W_req
    Wreq = (p ** (k + 1)) * p0 / (kfakt * k)
    Wreq *= (1 - (ps ** n) * (n + 1 - n * ps)) / ((1 - ps) ** 2)
    rez += f"Среднее число запросов в очеред Wreq = {Wreq:.4f}\n"

    # Определяем среднее время ожидания заявки в очереди T_req
    Treq = Wreq / lam 
    rez += f"Среднее время ожидания запроса в очереди Treq = {Treq:.4f}\n"

     # Определяем среднее число заявок в СМО W_s
    Ws = kch+ Wreq
    rez += f"Cреднее число запросов в СМО Ws = {Ws:.4f}\n"

    # Среднее время пребывания заявки в СМО T_s
    Ts = Treq + (1 - pden) / mu
    rez += f"Определяем среднее время пребывания запроса в СМО Ts = {Ts:.4f}\n"


    # Вероятности пребывания в СМО i запросов ρi вычисляются 
    # по двум различным вариантам расчета – для случая, 
    # когда 1 ≤ i ≤ k, и для k < i ≤ k+n (это делается для расчета всех вариантов, k + 1 дается, 
    # чтобы потом вычислить значения для второго случая и составить 
    # более подроную статистику вероятностей. Например, если k = 4, n = 3, то pi вычисляется 6 раз)
    numer = p0
    denom = 1
    for i in range(1, k + 1): # числители и знаменатели формируются 
        # отдельно по итерациям для случая 1 ≤ i ≤ k
        numer *= p
        denom *= i
        psost = numer / denom
        rez += f"Вероятности пребывания в СМО p{i} = {psost:.4f}\n"

    for i in range(k + 1, k + n): # И для случая k < i ≤ k+n
        numer *= p
        denom *= k
        psost = numer / denom
        rez += f"Вероятности пребывания в СМО p{i} = {psost:.4f}\n"

    if pden <= 0.3:
        rez += '\nВремя до отказа примерно 12-15 мин\n'
        rez += 'Примечание: Заблокировать подозрительные IP\n'
    elif pden >= 0.6:
        rez +='\nВремя до отказа примерно 4-5 мин\n'
        rez +='Примечание: подключить файл подкачки и следовать инструкции по принятию решений\n'
        rez +='Примечание: Внедрить средства защиты от DDoS (DDoS-Guard, Selectel, сеть Петри)\n'
    else:
        rez +='\nВремя до отказа примерно 7-8 мин\n'
        rez +='Примечание: подключить файл подкачки и следовать инструкции по принятию решений\n'

    return rez # Возвращение от функции результата rez


print(smo(4, 3, 200, 17)) # На вход подаются параметры функции smo (4, 3, 150, 17) or (7, 3, 150, 20)


# Графическое представление DDoS

# Импорт данных
#df = pd.read_csv("C:/Users/serge/source/repos/Diplom/Diplom/traffictest.csv")
#df = pd.read_csv("C:/Users/serge/source/repos/Diplom/Diplom/trafficddos.csv")
df = pd.read_csv("C:/Users/serge/source/repos/Diplom/Diplom/traffic_end.csv")

inf = df.info()

val_protocol = df['Protocol'].value_counts()
print ('\n\n Количество найденных протоколов: \n', val_protocol)

# Отрисовка
fig = go.Figure()
fig.add_trace(go.Scatter(x = df['Time'], y = df['Length'], marker=dict(color="#008000"), name='Проходящий трафик'))

fig.update_layout(title='Интенсивность DDoS-атаки',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)
fig.update_xaxes(title='Время сессии (в мин)')
fig.update_yaxes(title='Трафик')
fig.show()





