from tkinter import Tk, simpledialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from exceptions import UserExit



def GUI2():
    Tk().withdraw()
    name_range = simpledialog.askstring(title="Welcome to Immi's Wonderland",
                                        prompt="If you have a CSV file with multiple sequences that you would like to create a heatmap for, please enter in the column and row numbers for the sequence NAMES/IDENTIFIERS, not the nucleotide sequences.\n\n"
                                                "For example, A1:A2500 will select the first 2500 entries in the A-column as sequence names. This allows you to pick and choose your desired range\n"
                                                "Bear in mind these sequence names will be the filenames of the completed heatmaps")

    sequence_range = simpledialog.askstring(title="Welcome to Immi's Wonderland",
                                            prompt="Select the range for the actual nucleotide sequences you would like to create heatmaps for")


    number_seq = simpledialog.askinteger(title="Welcome to Immi's Wonderland",
                                         prompt='How many sequences are you trying to create heatmaps for? Please enter in a number without commas'
                                                'If you just want to analyze a single sequence, please either close this window or enter 1.')
    open_txt = askopenfilename()
    save_csv = asksaveasfilename()
    save_heatmap = asksaveasfilename()

    return open_txt, save_csv, save_heatmap, name_range, sequence_range, number_seq
