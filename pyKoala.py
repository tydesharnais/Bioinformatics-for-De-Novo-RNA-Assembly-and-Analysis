import matplotlib.pyplot as plt 
import numpy as np
import pyfiglet as Figlet
from time import sleep

#need total entries
#need total entries that were annotated 
#how many splits
# 

def print_Results(dictionary):
    print("\nFinal Results\n--------------------------------------")
    for x in dictionary:
         print(f'{x} : {dictionary.get(x)}') 
    print("\n--------------------------------------\n")

def nice_pie_Chart(dictionary, s_Name):
         # Creating explode data
         # split dictionary into keys and values
    keys, values = zip(*dictionary.items())
    y_Array = np.array(values)
    
    
    
    # Creating color parameters
    colors = ( "#000000", "#380356", "#6b0078",
            "#93009c", "#b000b2", "#1A0554")
    
    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }
    
    labels_X = list(keys)
    print(labels_X)
    
    # Creating plot
    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(y_Array,
                                    autopct = lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '',
                                    explode = None,
                                    labels=labels_X,
                                    shadow = True,
                                    colors = colors,
                                    startangle = 90,
                                    wedgeprops = wp,
                                    textprops = dict(color ="white"))
    
    # Adding legend
    ax.legend(wedges, keys,
            title ="Annotation Type",
            loc ="center left",
            bbox_to_anchor =(1, 0, 0.5, 1))
    
    plt.setp(autotexts, size = 8, weight ="bold")
    ax.set_title(f'Annotation Distrubtion of Species: {s_Name}')

    #plt.show()
    plt.savefig(f'pyKoala_{s_Name}.png', bbox_inches='tight')

def reset_Colors():
    print(Figlet.color_to_ansi('RESET',False))
    print(Figlet.color_to_ansi('RESET',True))   

def add_to_key(dictionary, key, new_I):
    value = dictionary.get(key)
    new_Value = new_I+int(value)
    dictionary[key] = new_Value
    

def pieChart(dictionary, s_Name):
    # split dictionary into keys and values
    keys, values = zip(*dictionary.items())
    y_Array = np.array(values)
    plt.pie(y_Array, labels=keys, autopct='%1.1f%%')
    plt.legend(title = "Annotation Type")
    plt.title(f'Annotation Distrubtion of Species: {s_Name}')
    plt.show()

def main():

    title =Figlet.figlet_format("PyKoala",'doh', width=200)
    print(Figlet.color_to_ansi("DEFAULT",True))
    print(Figlet.color_to_ansi('MAGENTA',False))
  
    print(title)
    print("--------------------------------------------------------------------------------------------------------------------------")
    
    print("--------------------------------------------------------------------------------------------------------------------------")
    print(Figlet.color_to_ansi('RESET',False))
    print(Figlet.color_to_ansi('CYAN',False))
    #blast dictionary for values 
    blastk_Dict = {
        "Carbohydrate metabolism": 0,
        "Energy metabolism": 0,
        "Lipid metabolism": 0,
        "Nucleotide metabolism": 0,
        "Amino acid metabolism": 0,	
        "Metabolism of other amino acids": 0,
        "Glycan biosynthesis and metabolism": 0,
        "Metabolism of cofactors and vitamins": 0,
        "Metabolism of terpenoids and polyketides": 0,
        "Biosynthesis of other secondary metabolites": 0,
        "Xenobiotics biodegradation and metabolism": 0,
        "Genetic information processing": 0,
        "Environmental information processing": 0,
        "Cellular processes": 0,	
        "Organismal systems": 0,	
        "Human diseases": 0,
        "Protein families: metabolism": 0,
        "Protein families: genetic information processing": 0,	      
        "Protein families: signaling and cellular processes": 0,
        "Unclassified: metabolism": 0,
        "Unclassified: genetic information processing": 0,
        "Unclassified: signaling and cellular processes": 0
        }

    species_Name = input("Species Name: ")
    files = int(input("How many Splits for BlastKoala files?: "))
    entries = 0
    annotated = 0

    for i in range(files):
        print(f'\n\nFile #: {i+1}')
        temp_I = int(input("How many Entries: "))
        temp_A = int(input("How many Entries Annotated: "))

        entries = entries + temp_I
        annotated = annotated + temp_A

        for x in blastk_Dict:
            temp_V = int(input(f'# of Hits for {x}: '))
            add_to_key(blastk_Dict,x,temp_V)
            print(f'\n New value for {x} : {blastk_Dict.get(x)}\n')
        
        percent_Annotated = (annotated / entries) * 100

        print(f'Total Entries: {entries}\nTotal Annotated: {annotated}\nTotal Percentage Annotated: {percent_Annotated}')

        nice_pie_Chart(blastk_Dict, species_Name)
        print_Results(blastk_Dict)
        reset_Colors()



    # for x in blastk_Dict:
    #     print(f'{x} : {blastk_Dict.get(x)}')
    #     mod = blastk_Dict.get(x)
    #     add_to_key(blastk_Dict,x,10)
       
    # for x in blastk_Dict:
    #     print(f'{x} : {blastk_Dict.get(x)}')


if __name__ == "__main__":
    
    print('-----------------------------------------\nCreated by Ty Desharnais\nhttps://www.github.com/tydesharnais\nhttps://www.linkedin.com/in/ty-desharnais/\n')
    sleep(3)

    try:
        main()
    except KeyboardInterrupt:
        print(Figlet.color_to_ansi('RED',False))
        print("\n(!): Program Exit\n------------------")
        reset_Colors()
        print("Reverting Color Codes\n")
        sleep(1)
        try:
            import sys
            sys.exit(0)
        except SystemExit:
            import os
            os._exit(0)
        
