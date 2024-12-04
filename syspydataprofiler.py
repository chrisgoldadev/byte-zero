from ydata_profiling import ProfileReport
import pandas as pd
import os
import webbrowser 


class PyDataProfiler():
    
    # this class is designed to read csv file and return a data profiler html file
    def py_data_profiler(csv_filename, delimiter: str):
        
        print('Establishing variables...')
        BASE_DIR = os.getcwd()
        path = os.path.join(BASE_DIR, csv_filename)
        
        print(f'Reading {csv_filename} with pandas...')        
        df = pd.read_csv(path, delimiter=delimiter)
        
        print('Creating dataframe profile...')
        profile = ProfileReport(
            df, 
            title='dataset_profile.html'
            )
        
        filename = r'dataset_profile.html'
        save_to = os.path.join(BASE_DIR, filename)
        print(f'Saving profile to: {save_to}')
        profile.to_file(filename)
        
        while True:
            print('Do you want to review the created profile? It will be opened in your default web browser.')
            response = input('Type [Y/N]: ').strip().upper()
            
            if response == 'Y':
                try:
                    webbrowser.open(save_to)
                except Exception as e:
                    print(f'Error opening the file: {e}')
                break
            elif response == 'N':
                print("No problem!")
                break
            else:
                print('Invalid input, please enter Y for yes or N for NO.')