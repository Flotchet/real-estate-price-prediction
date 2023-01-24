import PySimpleGUI as sg
import os 

#make a menu with key 
def create_menu(title, buttons):
    return [[sg.Text(title)], [sg.Button(button, key=f'{button}_key') for button in buttons]]

        
#make layout 
layout = [
            [sg.Text('Welcome! Click on any button to execute some part of the project.')],
            create_menu('Scrapihg part', ['Full scraper', 'URL scraper', 'HTML scraper', 'Data extractor + csv']),
            create_menu('Data preparation part', ['Data preparation for visualization','Data preparation for regression']),
            create_menu('Data visualisation part', ['Data visualisation']),
            create_menu('Machine learning part', ['Model']),
            create_menu('deploiment part', []),
            [sg.Text('rest')],
            [sg.Button('Run all', key = 'run all')],
            [sg.Button('Exit' , key = 'Exit')]
        ]
# Create the window
window = sg.Window('Immoweb project', layout, element_justification='center')

# Event loop
while True:

    event, values = window.read()

    if event in (None, 'Exit'):
        break
    elif event == 'Full scraper_key':
        print('Full scraper')
        #run data_aquisition.py in command 
        os.system('python3 data_acquisition/data_aquisition.py')

    elif event == 'URL scraper_key':
        print('URL scraper')
        #run Immoweb_URL__scraper.py
        os.system('python3 data_acquisition/a_Immoweb_URL__scraper/Immoweb_URL__scraper.py')

    elif event == 'HTML scraper_key':
        print('HTML scraper')

    elif event == 'Data extractor + csv_key':
        print('Data extractor + csv')

    elif event == 'run all':
        print('run all')

window.close()