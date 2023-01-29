from flask import Flask, render_template, request, Markup
app = Flask(__name__, template_folder='templates', static_folder='templates/assets')

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

    # Get the data from the form

    #category
    immo = request.form['category']
    #zipcode
    zipcode = request.form['zipcode']
    #number of room
    room = request.form['number of room']
    #living area
    surface = request.form['living Area']

    
    value = 0
    
    #check if the data are correct
    result = check(immo, zipcode, room, surface)

    if result != "":
        return render_template('index.html', result=Markup(result))

    zipcode = int(zipcode)  
    room = int(room)
    surface = float(surface)

    #other usefull form field
    garden = request.form['Total Area of gardens']
    try:
        garden = float(garden)
    except:
        garden = 0

    terrace = request.form['Total Area of terraces']
    try:
        terrace = float(terrace)
    except:
        terrace = 0

    furnished = request.form["Furnished"]
    if furnished == "on":
        furnished = True
    else:
        furnished = False

    Equiped = request.form["Equiped kitchen"]
    if Equiped == "on":
        Equiped = True
    else:
        Equiped = False

    



    #load the model
    #model = pickle.load(open('model.pkl', 'rb'))

    #prepare the data

    #predict the value
    #value = model.predict([[zipcode, room, surface]])

    return render_template('index.html', result=f"Your {immo} has a value of approximatly {value} euros")

if __name__ == '__main__':
    app.run(debug=False)