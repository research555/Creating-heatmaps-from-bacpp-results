import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def TxtToStr(txt):
    string = ''.join(txt[1:])
    final_str = string.replace('\t', ',').replace('\n', ',')

    return final_str

def GenerateCSV(list):

    i = 0
    position = []
    seq = []
    s24 = []
    s28 = []
    s32 = []
    s38 = []
    s54 = []
    s70 = []

    # # # # FILL IN RESPECTIVE LISTS # # # #
    while i < len(list):
        position.append(list[i])
        i += 9

    i = 2
    while i <= len(list):
        seq.append(list[i])
        i += 9

    i = 3
    while i <= len(list):
        s24.append(list[i])
        i += 9

    i = 4
    while i <= len(list):
        s28.append(list[i])
        i += 9

    i = 5
    while i <= len(list):
        s32.append(list[i])
        i += 9

    i = 6
    while i <= len(list):
        s38.append(list[i])
        i += 9

    i = 7
    while i <= len(list):
        s54.append(list[i])
        i += 9

    i = 8
    while i <= len(list):
        s70.append(list[i])
        i += 9

    # # # # KEEP ONLY LAST NUCLEOTIDE FROM SEQUENCE # # # #
    nt = []
    for item in seq:
        nt.append(item[-1])

    csv_ready_dict = {
        'position': position,
        'nt': nt,
        's24': s24,
        's28': s28,
        's32': s32,
        's38': s38,
        's54': s54,
        's70': s70
    }
    return csv_ready_dict

def GenerateHeatMap(df):
    import seaborn as sns
    import numpy as np
    import matplotlib.pyplot as plt

    # # # # CREATE 1D ARRAYS # # # #
    nucleotides = ((np.asarray(df['nt'])))
    y_label = ['s24', 's28', 's32', 's38', 's54', 's70']
    s24 = ((np.asarray(df['s24'])))
    s28 = ((np.asarray(df['s28'])))
    s32 = ((np.asarray(df['s32'])))
    s38 = ((np.asarray(df['s38'])))
    s54 = ((np.asarray(df['s54'])))
    s70 = ((np.asarray(df['s70'])))

    # # # # STACK ARRAYS INTO 2D ARRAY # # # #
    all_sigma = np.stack((s24, s28, s32, s38, s54, s70))

    # # # # CREATE PLOT AND HEATMAP # # # #
    fig, ax = plt.subplots(figsize=(30, 4))  # change size of the window and heatmap plot by changing parameters
    heatmap = sns.heatmap(data=all_sigma, xticklabels=nucleotides, yticklabels=y_label, vmin=70, vmax=100)  # Change heatmap design by changing parameters

    return heatmap, fig


def GUI():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename, asksaveasfilename

    Tk().withdraw()
    open_txt = askopenfilename()
    save_csv = asksaveasfilename()
    save_heatmap = asksaveasfilename()

    return open_txt, save_csv, save_heatmap


def SingleSequence(rf, save_csv):

    bacpp_txt = rf.readlines()  # Generate list from contents of file
    final_str = TxtToStr(bacpp_txt).split(',')  # format contents into string
    bacpp_list = list(filter(None, final_str))  # remake formatted list

    csv_ready_dict = GenerateCSV(list=bacpp_list)  # produce CSV from the formatted list

    df = pd.DataFrame(csv_ready_dict, columns=['position', 'nt', 's24', 's28', 's32', 's38', 's54', 's70'])
    df.to_csv(save_csv + '.csv', index=False)  # save CSV to your computer
    heatmap_df = pd.read_csv(save_csv + '.csv')
    heatmap, fig = GenerateHeatMap(df=heatmap_df)

    return heatmap, fig

