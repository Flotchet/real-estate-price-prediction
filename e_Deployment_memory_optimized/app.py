from flask import Flask, render_template, request, Markup
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
import pickle
import os
import pandas as pd
import datetime

app = Flask(__name__, template_folder='templates', static_folder='templates/assets')

def prepare_zipcode(df : pd.DataFrame) -> dict[int:float]:
    #create zipcode conversion table
    zipcode = {}

    #dropnan from prices
    df2 = df.dropna(subset=['Price'])
    #dropnan from zipcode
    df2 = df2.dropna(subset=['zipcode'])

    for z in list(df2['zipcode'].unique()):
        zipcode[z] = df2[df2['zipcode'] == z]['Price'].median()
        
    return zipcode

def prepare_type(df : pd.DataFrame) -> dict[str:float]:
    #create type conversion table
    types = {}

    #dropnan from prices
    df2 = df.dropna(subset=['Price'])
    #dropnan from type
    df2 = df2.dropna(subset=['type'])

    for i in df["type"].unique():
        types[i] = df[df['type'] == i]['Price'].mean()

    return types

def prepare_tax(df : pd.DataFrame) -> dict[int:float]:
    #create zipcode conversion table
    zipcode = {}

    #dropnan from tax
    df2 = df.dropna(subset=['Taxe'])
    #dropnan from zipcode
    df2 = df2.dropna(subset=['zipcode'])

    for z in list(df2['zipcode'].unique()):
        zipcode[z] = df2[df2['zipcode'] == z]['Taxe'].mean()

    return zipcode

def get_name(zipcode : int) -> str:

    if zipcode < 1300:
        return 'BruxellesCapitale'
    elif zipcode < 1500:
        return 'ProvinceduBrabantwallon'
    elif zipcode < 2000:
        return 'ProvinceduBrabantflamand'
    elif zipcode < 3000:
        return 'ProvincedAnvers'
    elif zipcode < 3500:
        return 'ProvinceduBrabantflamand2'
    elif zipcode < 4000:
        return 'ProvincedeLimbourg'
    elif zipcode < 5000:
        return 'ProvincedeLiege'
    elif zipcode < 6000:
        return 'ProvincedeNamur'
    elif zipcode < 6600:
        return 'ProvinceduHainaut1'
    elif zipcode < 7000:
        return 'ProvincedeLuxembourg'
    elif zipcode < 8000:
        return 'ProvinceduHainaut2'
    elif zipcode < 9000:
        return 'ProvincedeFlandreOccidentale'
    elif zipcode < 10000:
        return 'ProvincedeFlandreOrientale'
    else:
        return ""

def models_loader() -> dict[str : any]:
    #get the all the file name in the model folder 
    models = {} 
    for file in os.listdir('models'):
        if file.endswith(".pickle"):
            name = file[:-7]
            models[name] = pickle.load(open(f'models/{file}', 'rb'))

    return models

def check(immo : str, zipcode : str, room : str, surface : str) -> str:
    result = ""
    if immo == "":
        result += "<br> Please choose a category <br/>"

    if zipcode == "":
        result += "<br> Please enter a zipcode <br/>"
    else:
        zipcode = int(zipcode)
        if zipcode < 1000 or zipcode > 9999:
            result += "<br> Please enter a plausible zipcode <br/>"

    if room == "":
        result += "<br> Please enter a number of room <br/>"

    else:
        room = int(room)
        if room < 1 or room > 100:
             result += "<br> Please enter a plausible number of room <br/>"


    if surface == "":
        result += "<br> Please enter a living area <br/>"

    else:
        surface = float(surface)
        if surface < 5 or surface > 1000:
            result += "<br> Please enter a plausible living area <br/>"

    return result

@app.route('/')
def form():
    return render_template('index.html', result="")

@app.route('/', methods=['POST'])
def result():


    #category
    immo = request.form['category']
    #zipcode
    zipcode = request.form['zipcode']
    #number of room
    room = request.form['number of room']
    #living area
    surface = request.form['living Area']


    value : float = 0

    #check if the data are correct
    result : str = check(immo, zipcode, room, surface)

    if result != "":
        return render_template('index.html', result=Markup(result))

    zipcode = int(zipcode)  

    room = int(room)

    surface = float(surface)

    #other usefull form field
    garden : str = request.form['Total Area of gardens']
    try:
        garden = float(garden)
    except:
        garden = 0

    terrace = request.form['Total Area of terraces']
    try:
        terrace = float(terrace)
    except:
        terrace = 0

    
    try:
        furnished = request.form['Furnished']
        if furnished == "on":
            furnished = True
        else:
            furnished = False
    except:
        furnished = False


    try:
        Equiped = request.form['Equiped kitchen']
        if Equiped == "on":
            Equiped = True
        else:
            Equiped = False
    except:
        Equiped = False




    name = get_name(zipcode)
    try:
        current_mdl = models[name]
    except:
        return render_template('index.html', result=f"Sorry we don't have a model for {name}")

    if zipcode not in zipcode_converter.keys():
        return render_template('index.html', result=f"Sorry the zipcode: {zipcode} doesn't exist")
    zipcode_v = zipcode_converter[zipcode]

    if immo not in type_converter.keys():
        return render_template('index.html', result=f"Sorry the type: {immo} doesn't exist")
    immo_v = type_converter[immo]

    if zipcode not in tax_converter:
        return render_template('index.html', result=f"Sorry the zipcode: {zipcode} doesn't refer to a city tax")
    tax = tax_converter[zipcode]


    #make a dict of the data
    data = {
            'Number of rooms': room, 
            'Living Area': surface, 
            'Fully equipped kitchen': Equiped, 
            'Furnished': furnished, 
            'Area of the terrace': terrace,
            'Area of the garden': garden, 
            'zipcode': zipcode_v,    
            'type': immo_v, 
            'Taxe': tax
           }

    #transform the dict in a data frame
    data = pd.DataFrame(data, index=[0])

    value = current_mdl.predict(data)*surface
    value = round(value[0])

    #save to log
    with open('log.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} : {immo} {zipcode} {room} {surface} {garden} {terrace} {furnished} {Equiped} {value}\n")

    return render_template('index.html', result=f"Your {immo} has a value of approximatly {value} euros. (The selected model is XGboost{name})")


    

#connect to the db
#db = SQLAlchemy(app)


#serve(app, host="0.0.0.0", port=8080)
#load the csv in a data frame
df : pd.DataFrame = pd.read_csv('data_for_regression.csv')

zipcode_converter : dict[int:float] = prepare_zipcode(df)
tax_converter : dict[int:float] = prepare_tax(df)
type_converter : dict[str:float] = prepare_type(df)

models : dict[str:any] = models_loader()

for model in models.keys():
    print(f"model {model} loaded")

app.run(debug=False)