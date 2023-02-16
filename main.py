import PySimpleGUI as sg
from itertools import cycle
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
            create_menu('Deployment part', []),
            [sg.Text('rest')],
            [sg.Button('Run all', key = 'run all')],
            [sg.Button('Exit' , key = 'Exit')],
            [sg.Button('Install needed packages', key = "install")]
        ]



keys = {
        'Full scraper_key': 'python3 a_data_acquisition/data_aquisition.py',
        'URL scraper_key': 'python3 a_data_acquisition/a_Immoweb_URL__scraper/Immoweb_URL__scraper.py',
        'HTML scraper_key': 'python3 a_data_acquisition/b_Immoweb_HTML_scraper/Immoweb_HTML_scraper.py',
        'Data extractor + csv_key': """
        python3 a_data_acquisition/c_Immoweb_data_extractor/Immoweb_data_extractor.py
        python3 a_data_acquisition/d_Immoweb_raw_csv_maker/Immoweb_raw_csv_maker.py
        """,

        'Data preparation for visualization_key': 'python3 b_data_preparation/data_preparation_for_visualization.py',
        'Data preparation for regression_key': 'python3 b_data_preparation/data_preparation_for_regression.py',

        'Data visualisation_key': 'python3 c_data_visualization/data_visualization.py',

        'Model_key': 'd_Machine_learning/model_training/model.py',

        'Deployment part_key': 'e_Deployment/app.py',

        'run all': 
        """
        python3 a_data_acquisition/data_aquisition.py
        python3 b_data_preparation/data_preparation_for_visualization.py
        python3 b_data_preparation/data_preparation_for_regression.py
        python3 c_data_visualization/data_visualization.py
        python3 d_Machine_learning/model_training/model.py
        python3 e_Deployment/app.py
        """,

        'Exit': 'Exit',
        'install': 'install',
    }

# Create the window
window = sg.Window('Immoweb project', 
                    layout,
                    default_element_size=(20, 5),
                    resizable=True,finalize=True)



# Event loop
for _ in cycle([True]):

    event, values = window.read()

    if event in keys:
        if event == "Exit":
            break
        if event == "install":
            with open('requirements.txt') as req:
                for line in req:
                    os.system(f'pip install {line}')

        os.system(keys[event])

    if event == None:
        break


window.close()