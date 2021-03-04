import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from functions import *

if __name__ == '__main__':
    with open("C:/Users/imran/documents/direct_to_file.txt", 'r') as rf:  # Open txt file from BacPP
        f_contents = rf.readlines()  # Generate list from contents of file
        final_str = TxtToStr(f_contents)  # format contents into string
        x = final_str.split(',')
        x = list(filter(None, x))  # remake formatted list

        csv_ready_dict = GenerateCSV(x=x)  # produce CSV from the formatted list

        df = pd.DataFrame(csv_ready_dict, columns=['position', 'nt', 's24', 's28', 's32', 's38', 's54', 's70'])
        df.to_csv(r'C:/users/imran/documents/dicttoxl.csv', index=False) # save CSV to your computer
        heatmap_df = pd.read_csv(r'C:/users/imran/documents/dicttoxl.csv')

        heatmap = GenerateHeatMap(df=heatmap_df)
        plt.show()  # shows the heatmap




