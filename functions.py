import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def TxtToStr(txt):
    string = ''.join(txt[1:])
    final_str = string.replace('\t', ',').replace('\n', ',')

    return final_str

def GenerateCSV(x):

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
    while i < len(x):
        position.append(x[i])
        i += 9

    i = 2
    while i <= len(x):
        seq.append(x[i])
        i += 9

    i = 3
    while i <= len(x):
        s24.append(x[i])
        i += 9

    i = 4
    while i <= len(x):
        s28.append(x[i])
        i += 9

    i = 5
    while i <= len(x):
        s32.append(x[i])
        i += 9

    i = 6
    while i <= len(x):
        s38.append(x[i])
        i += 9

    i = 7
    while i <= len(x):
        s54.append(x[i])
        i += 9

    i = 8
    while i <= len(x):
        s70.append(x[i])
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

    # # # # CREATE 1D ARRAYS
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
    fig, ax = plt.subplots(figsize=(20,5))  # change size of the window and heatmap plot by changing parameters
    heatmap = sns.heatmap(data=all_sigma, xticklabels=nucleotides, yticklabels=y_label)  # Change heatmap design by changing parameters

    return heatmap