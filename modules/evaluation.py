import numpy as np
from constants import *
from config import *
import sys

def evaluate(stake_names, stake_data, df_):
    """ This methods evaluates the simulation with the stake measurements
        stake_name  ::  """

    if eval_method == 'rmse':
        stat = rmse(stake_names, stake_data, df_)
    else:
        stat = None
       
    return stat


def rmse(stake_names, stake_data, df_):
    rmse = ((stake_data[stake_names].subtract(df_['mb'],axis=0))**2).mean()**.5
    return rmse
