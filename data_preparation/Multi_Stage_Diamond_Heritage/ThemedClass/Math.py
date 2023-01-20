#import path
import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/OneMethodClass/Math")

#-P-IMPORT--------------------------------------------------------------------------------------
from new_by_add import new_by_add
from new_by_div import new_by_div
from new_by_exp import new_by_exp
from new_by_fft import new_by_fft
from new_by_func_on_col import new_by_func_on_col
from new_by_func import new_by_func
from new_by_ifft import new_by_ifft
from new_by_log import new_by_log
from new_by_mult import new_by_mult
from new_by_pow_col import new_by_pow_col
from new_by_pow import new_by_pow
from new_by_sin import new_by_sin
from new_by_sqrt import new_by_sqrt
from new_by_sub import new_by_sub
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class Math(new_by_add, 
           new_by_div, 
           new_by_exp, 
           new_by_fft, 
           new_by_func_on_col, 
           new_by_func, 
           new_by_ifft, 
           new_by_log, 
           new_by_mult, 
           new_by_pow_col, 
           new_by_pow, 
           new_by_sin, 
           new_by_sqrt, 
           new_by_sub):
        
    pass

