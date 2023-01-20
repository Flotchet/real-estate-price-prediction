#import path
import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/OneMethodClass/OQOF")

#-P-IMPORT--------------------------------------------------------------------------------------
from append_data import append_data
from apply import apply
from concatenate_data import concatenate_data
from dropna import dropna
from new_colomn_by_separation import new_colomn_by_separation
from reset_all import reset_all
from reset import reset
from switch import switch
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class QualityOfLife(append_data,
           apply,
           concatenate_data,
           dropna,
           new_colomn_by_separation,
           reset_all,
           reset,
           switch):
     
    pass