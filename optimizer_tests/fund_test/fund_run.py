####################
# fund test
####################


########################################
# import all necessary libraries

import rqdatac
from rqdatac import *
rqdatac.init("ricequant", "8ricequant8")
import datetime as dt
import itertools
import matplotlib.pyplot as plt


########################################
# !!!! You need to have github structure to run all the code without modificaiton.
########################################
# import all related functions

import optimizer_tests.fund_test.ptfopt1
import optimizer_tests.fund_test.get_fund_suite
import optimizer_tests.fund_test.get_optimizer
import optimizer_tests.fund_test.get_optimizer_indicators
import optimizer_tests.fund_test.get_efficient_plots



# generate fund_test_suite
fund_test_suite = get_fund_test_suite('2014-01-01')


# test_fund_opt is to wrap get_optimizer to run all suite
def test_fund_opt(fund_test_suite, bc = 0):
    """
    :param fund_test_suite (dic)
    :param bc (int): an indicator about bounds and constraints. 0 means nothing;
                                                               1 means have bounds, no constraints;
                                                               2 means no bounds, have constraints;
                                                               3 means have both
    :return:
    """
    a = {}
    for k in fund_test_suite.keys():
        a[k] = get_optimizer(fund_test_suite[k],  start_date = '2014-01-01',end_date= '2017-05-31',
                             asset_type='fund', method='all', fields ='all', name = k,bc = bc)

    return a


# run

bigboss = test_fund_opt(fund_test_suite)
bigboss_b_nc = test_fund_opt(fund_test_suite, 1)
bigboss_nb_c = test_fund_opt(fund_test_suite, 2)
bigboss_b_c = test_fund_opt(fund_test_suite, 3)



# to get efficient plots, run get_efficient_plot.py
get_efficient_plots(fund_test_suite, bigboss)
get_efficient_plots(fund_test_suite, bigboss_b_nc)
get_efficient_plots(fund_test_suite, bigboss_nb_c)
get_efficient_plots(fund_test_suite, bigboss_b_c)