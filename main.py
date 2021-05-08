import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from functions import *
from tkinter import Tk, simpledialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from exceptions import UserExit
from GUI import GUI2


if __name__ == '__main__':
    open_txt, save_csv, save_heatmap, name_range, sequence_range, number_seq = GUI2()
    try:
        if number_seq is None:
            raise UserExit
        elif number_seq == 1:
            with open(open_txt, 'r') as rf:  # Open txt file from BacPP
                heatmap, fig = SingleSequence(rf=rf, save_csv=save_csv)
                fig.savefig(save_heatmap + '.png')
                plt.show()  # shows the heatmap
        elif number_seq > 1:


    except Exception:
        if UserExit:
            pass







