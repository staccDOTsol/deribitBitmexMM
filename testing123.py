import time
from blackscholes import black_scholes
import time
from datetime import datetime
#   >>> black_scholes(7598.45, 7000, 0.09587902546296297, 0.679, 0.03, 0.0, -1)
#   >>> black_scholes(7598.45, 9000, 0.09587902546296297, 0.675, 0.03, 0.0, 1)
from deribit_api    import RestClient
KEY     = 'pUcNWyjC'
SECRET  = 'iQaAEpwYEOnS-aJm7vlusoDDwYry00thwywe1mwDfZU'
client = RestClient( KEY, SECRET, 'https://test.deribit.com' )
import math
from utils          import ( get_logger, lag, print_dict, print_dict_of_dicts, sort_by_key,
                             ticksize_ceil, ticksize_floor, ticksize_round )
while True:
    spot = 7184.99
    diff = 1/12
    ivc = 0.602
    ivp = 0.604
    p = 7220.4900
    c = 7220.4900
    p1 = black_scholes(spot, 7220.4900, diff, ivp, 0.03, 0.0, -1) 
    c1 = black_scholes(spot, 7220.4900, diff, ivc, 0.03, 0.0, 1) 
    
    c2 = black_scholes(spot * 1.075, p, diff, ivp, 0.03, 0.0, -1) 
    p2 = black_scholes(spot * 1.075, c, diff, ivc, 0.03, 0.0, 1) 
    c3 = black_scholes(spot * (1-0.075), p, diff, ivp, 0.03, 0.0, -1) 
    p3 = black_scholes(spot * (1-0.075), c, diff, ivc, 0.03, 0.0, 1) 
    cost1 =(c1 + p1)
    cost2 = (c2 + p2)
    cost3 = (c3 + p3)
    profit=(cost2-cost1)+(cost3-cost1)
    print(profit)