#import numpy
import numpy as np
#import pandas
import pandas as pd
#import matplotlib
import matplotlib.pyplot as plt

#read the csv file
df = pd.read_csv('/home/flotchet/Becode/LIE-Thomas-2-main/content/0.projects/2.immo_eliza/Machine_learning/_139857770514512_DataFrameExtended.csv')

#split data with the To sell column
df_sell = df[df['To sell'] == True]
df_not_sell = df[df['To sell'] == False]

#create list that conatains data by zipcode
list_sell = []
list_not_sell = []

#mean_price
mean_price_to_sell = df_sell['Price'].mean()
mean_price_not_to_sell = df_not_sell['Price'].mean()

#compute the range by zipcode
for i in range(1000, 9999):
    try:
        list_sell.append(df_sell[df_sell['zipcode'] == i])
        list_not_sell.append(df_not_sell[df_not_sell['zipcode'] == i])
    except:
        pass

#drop the zipcode
for i in range(len(list_sell)):
    list_sell[i] = list_sell[i].drop(columns=['zipcode'])
    list_not_sell[i] = list_not_sell[i].drop(columns=['zipcode'])

#just keep duplicates
for i in range(len(list_sell)):
    list_sell[i] = list_sell[i][list_sell[i].duplicated()]
    list_not_sell[i] = list_not_sell[i][list_not_sell[i].duplicated()]

#drop the duplicates
for i in range(len(list_sell)):
    list_sell[i] = list_sell[i].drop_duplicates()

for i in range(len(list_not_sell)):
    list_not_sell[i] = list_not_sell[i].drop_duplicates()

#only keep the price
for i in range(len(list_sell)):
    list_sell[i] = list_sell[i]['Price']

for i in range(len(list_not_sell)):
    list_not_sell[i] = list_not_sell[i]['Price']

print(list_sell)

#compute the max and the min by zipcode
for i in range(len(list_sell)):
    list_sell[i] = list_sell[i].max() - list_sell[i].min()

for i in range(len(list_not_sell)):
    list_not_sell[i] = list_not_sell[i].max() - list_not_sell[i].min()

#remove NaN
list_sell = [x for x in list_sell if str(x) != 'nan']
list_not_sell = [x for x in list_not_sell if str(x) != 'nan']

#compute the mean difference
mean_difference_sell = np.mean(list_sell)*len(list_sell)/len(df_sell['Price'])
mean_difference_not_sell = np.mean(list_not_sell)*len(list_not_sell)/len(df_not_sell['Price'])

#print them
print(f"The average max difference of selling price for 2 simalar propreties (if there is no duplicate the difference is 0) {mean_difference_sell}")
print(f"The average max difference of renting price for 2 simalar propreties (if there is no duplicate the difference is 0) {mean_difference_not_sell}")

#compute the percentage of duplicate
#compute duplicate without price


ps=(len(df_sell['Price']) - len(list_sell))/len(df_sell['Price'])
pr=(len(df_not_sell['Price']) - len(list_not_sell))/len(df_not_sell['Price'])

#number of duplicate
print(f"The number of duplicate for selling propreties is {ps}")
print(f"The number of duplicate for renting propreties is {pr}")

#average uncertainty of the price
print(f"The average estimated uncertainty of the selling price is {np.mean(list_sell)*(1-ps)}")
print(f"The average estimated uncertainty of the renting price is {np.mean(list_not_sell)*(1-pr)}")

#plot the data by zipcode in a barh
plt.figure(figsize=(20, 20))
plt.barh(range(len(list_sell)), list_sell, color='red')
plt.show()

#plot the data by zipcode in a barh
plt.figure(figsize=(20, 20))
plt.barh(range(len(list_not_sell)), list_not_sell, color='blue')
plt.show()