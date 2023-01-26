import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

if __name__ == "__main__":
    # Read data
    data = pd.read_csv("data_visualization/processed_data.csv")

    #separate the data by the value of the column "To sell" True or False
    data_to_sell = data[data["To sell"] == True]
    data_to_rent = data[data["To sell"] == False]

    #plot the histplot for each data set
    plt.title("Price To sell")
    sns.histplot(data_to_sell, x="Price", kde=True)
    plt.show()

    plt.title("Price To rent")
    sns.histplot(data_to_rent, x="Price", kde=True)
    plt.show()
    
    plt.title("Price by square meter To sell")
    sns.histplot(data_to_sell, x="Price by M**2", kde=True)
    plt.show()

    plt.title("Price by square meter To rent")
    sns.histplot(data_to_rent, x="Price by M**2", kde=True)
    plt.show()

    plt.title("Price by square meter comparating to to the size of population")
    plt.scatter(data_to_rent["Price by M**2"],data_to_rent["Total"])
    plt.show()

    plt.title("Price by square meter comparating to to the size of population")
    plt.scatter(data_to_sell["Price by M**2"],data_to_sell["Total"])
    plt.show()

    #Average price per square meter by postcode
    avg_data_to_sell = data_to_sell.groupby("Name").mean()
    avg_data_to_rent = data_to_rent.groupby("Name").mean()

    #find the 10 cities with the most expensive
    avg_data_to_sell = avg_data_to_sell.sort_values(by="Price by M**2", ascending=False)
    avg_data_to_rent = avg_data_to_rent.sort_values(by="Price by M**2", ascending=False)

    #plot the 10 cities with the most expensive
    plt.title("10 cities with the most expensive price by square meter")
    x = avg_data_to_sell.index[:10] 
    y = avg_data_to_sell["Price by M**2"][:10]
    plt.barh(x, y)
 
    for index, value in enumerate(y):
        plt.text(value, index, str("%.2f" % value))

    plt.show()

    #plot the relation between A-Taxe and Price
    plt.title("Relation between A-Taxe and Price")
    plt.scatter(data_to_sell["A-Taxe"],data_to_sell["Price by M**2"])
    plt.show()

    #plot the relation between A-taxe and average Price by taxes with groupby
    med_data_to_sell = data_to_sell.groupby("A-Taxe").median()

    #fit a curve to med_data_to_sell.index and to 
    # and med_data_to_sell["Price by M**2"] to find the relation between A-Taxe and Price
    #z = np.polyfit(med_data_to_sell.index,med_data_to_sell["Price by M**2"], 3)
    #p = np.poly1d(z)
    #plt.plot(med_data_to_sell.index,p(med_data_to_sell.index),"r--")

    z = np.polyfit(med_data_to_sell.index,med_data_to_sell["Price by M**2"], 2)
    p = np.poly1d(z)
    plt.plot(med_data_to_sell.index,p(med_data_to_sell.index),"g")

    plt.title("Relation between municipal A-Taxes and median Prices by square meter", )

    plt.scatter(med_data_to_sell.index,med_data_to_sell["Price by M**2"])

    #add a legend
    plt.legend(["Tendency","Municipal A-taxes - Median prices by square meter from dataset"])
    #add axes name
    plt.xlabel("""1 - municipal taxe
percent
(%)""")
    plt.ylabel("""Price by square meter 
euros by square meter
(€/m²)""")
    
    plt.show()

    #do the same but with a regplot
    plt.title("Relation between municipal wealth and median prices by square meter", )

    sns.regplot(x=med_data_to_sell.index, y=med_data_to_sell["Price by M**2"], order=1, scatter_kws={'color':'r', 's':9})

    plt.xlabel("""1 - municipal taxe
percent
(%)""")
    plt.ylabel("""Price by square meters
euros by square meter
(€/m²)""")
    plt.show()

    #plot the relation between price and type in a bar plot
    plt.title("Relation between median price by square meter and the type of goods")


    y = data_to_sell.groupby("type").median()
    y = y.sort_values(by="Price by M**2", ascending=False)["Price by M**2"]
    x = y.index

    #labels
    plt.ylabel("Type of goods")
    plt.xlabel("Price by square meter in euros")

    plt.barh(x,y)

    for index, value in enumerate(y):
        plt.text(value, index, str("%.2f" % value))

    plt.show()

    #make two boxplot with two dataframe
    plt.title("Boxplot of the price by square meter")
    sns.boxplot(x="To sell", y="Price by M**2", data=data)
    plt.show()