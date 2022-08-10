import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
import seaborn as sns 
import pandas as pd
import textwrap


__version__ = "v1.0"
eval_Modifer = 0 

#Gene Class
# Name (ex. TRINITY_DN3229_c0_g1_i122)
# List of expected proteins
# E-Values associated with that protein (tuple)
# How many times that protein was expected #

#########################################
# AUX FUNCTIONS 
# wrap_labels - wraps labels
# counter - counts listing instances
# auxLen - returns the length of x
####################################### 

#Taken from medium.com credit to Ted Petrou

def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                      break_long_words=break_long_words))
    ax.set_xticklabels(labels, rotation=0)

#Aux function to illstrate counting of instances

def counter(lst, x):
    return lst.count(x)

def auxLen(x):
    return len(x)

######################################################################
# GENE CLASS
# get_GeneName() returns gene name
# add_Protein() adds a species to the listed gene
# print_proteins() aux function to print out a given genes protein matches 
# return_Tuple() returns a tuple of the gene name + e-value
# return_Top() returns the top result of the species and e value
# return_proteins() returns all expected species 
# ###################################################################
# #

class Gene:
    list_total = [] # static 
    
    def __init__(self, name):
        self.name = name
        self.expected_Proteins = []
    
    #return gene name
    def get_GeneName(self):
        return self.name

    #add a protein
    def add_Protein(self, pN, eVal):
        if(int(sys.argv[1]) != 0):
            try:
                split_Val = eVal.split('e')          
                if(int(split_Val[1]) > int(sys.argv[1])):
                    #protein ommited
                    pass
                else:
                    self.expected_Proteins.append((pN, eVal))
            except:
                #single digit eval
                if(float(eVal) > float(sys.argv[1])):
                    pass
                else:
                    self.expected_Proteins.append((pN, eVal))
    

    #prints all proteins 
    def print_Proteins(self):
        for i in range(len(self.expected_Proteins)):
            print(f'Protein: {self.expected_Proteins[i][0]} | E-Value: {self.expected_Proteins[i][1]}')  
        return self.expected_Proteins

    # Returns a tuple of the protein and e-value
    def return_Tuple(self, num):
        try:
            return self.expected_Proteins[num]  
        except:
            pass
    # Returns a tuple of the protein and e-value
    def return_Top(self):
        try:
            return self.expected_Proteins[0] 
        except:
            return "NA"
    def return_proteins(self):
        try:
            return self.expected_Proteins
        except:
            pass

#If writer arg is turned on         
def writerArg(gene_List):
    with open('sample.txt', 'w') as writer:
            for item in gene_List:
                writer.write("%s\n" % item.get_GeneName())
                writer.write("%s\n" % item.print_Proteins())

# CHECK ARGS 
# checks the command line arguments #
# ######################################
# #
def check_Args():
    
    n = len(sys.argv)
    if(n >= 2):
        print(n)
        for i in range(len(sys.argv)):
            print(f'{i}: ARG {sys.argv[i]}')
        # Help option
        if(sys.argv[1] == "-h"): #-omit -w -h
            print(f'\nPyBlast {__version__}\n-------------\nMade Ty Desharnais\nwww.github.com/tydesharnais\n\n ')
            print("Command line usage: input an integer with the expected e-value amount")
            print("Ex: python3 terminal_PyBlast.py -50 = 1e-50\n\nAll results higher then this amount will be omitted as a predicted protein")
            print("e-value must be specified, where 0 is a completely random e-value listing")
            print("You can turn the file writer on with -w which will export a text file of your results")
            print("Example: python3 terminal_PyBlast.py -5 -w")
            exit()


        
        
        else:
            main()
    else:
        print("Error. Must specify e-value level. Use -h for help")

#
# MAIN()
# the body of the program 
# #

def main():
    omit_List = [] #list of the ommited results (if turned on)
    omit_Active = False #this is to save time with non omitted results

    maxInt = sys.maxsize

    #OMIT FOR LOOP
    if(len(sys.argv) >= 3):
        if(sys.argv[2] == "-omit" or sys.argv[3] == "-omit"):
            omit_File = input("Omit File Name: ")
            with open(omit_File,'r') as omit_reader:
                lines = omit_reader.readlines()
                print("\nTO BE OMITTED FROM RESULTS\n--------------------------------")
                for line in lines:
                    print(line.strip())
                    omit_List.append(line.strip())
                print("--------------------------------\n")

    # Dirty Code to select the highest CSV file limit : Credit to StackOverflow

    while True:
        try:
            csv.field_size_limit(maxInt)
            break
        except OverflowError:
            maxInt = int(maxInt*0.99999)

    print("\n\nPYBLAST\n---------------------------------\n")
    print(f'\n::: Size limit {maxInt} :::\n')

    answer = input("File name to examine: ")

    gene_List = [] # list of genes
    newGene = Gene("placeholder")
    newGene.add_Protein('place',1e3)
    gene_List.append(newGene)

    with open(answer, 'r') as fileOpener:
        reader = csv.reader(fileOpener, delimiter='\t')
        i = 0
        j = 0
        total = 0
       # gene_List = [] # list of genes
        for row in reader:
            for col in row: 
                
                if(i == 24):
                    # TRY BLOCK FOR BRACKETS
                    try:
                        splitLeft = col.split('[',)
                        splitRight = splitLeft[1].split(']')
                        final_Split = splitRight[0]
                        
                        #Here we are checking if the gene exists in a current list 
                        for i in range(len(gene_List)):
                            if(row[0] == gene_List[i].get_GeneName()):
                                gene_List[i].add_Protein(final_Split, row[10]) # add Tuple to Gene 
                                gene_List[i].list_total.append(final_Split) #append to static list 
                                break
                                
                            elif(i == len(gene_List)-1):
                                if(row[0] == gene_List[i].get_GeneName()):
                                    gene_List[i].add_Protein(final_Split, row[10]) # add Tuple to Gene 
                                    gene_List[i].list_total.append(final_Split) #append to static list 
                                    #gene_List[2].print_Proteins()
                                    break
                                else:
                                    newGene = Gene(row[0])
                                    newGene.list_total.append(final_Split) #append to static list 
                                    newGene.add_Protein(final_Split,row[10])
                                    gene_List.append(newGene) #append it to the list 
                                    break
                       
                    except:
                        #TRY BLOCK FOR NO BRACKETS
                        try:
                            
                            for i in range(len(gene_List)):
                                if(row[0] == gene_List[i].get_GeneName()):
                                    gene_List[i].add_Protein(col, row[10]) # add Tuple to Gene 
                                    gene_List[i].list_total.append(final_Split) #append to static list 
                                    break
                                elif(i == len(gene_List)-1):
                                    if(row[0] == gene_List[i].get_GeneName()):
                                        gene_List[i].add_Protein(col, row[10]) # add Tuple to Gene 
                                        gene_List[i].list_total.append(final_Split) #append to static list 
                                        break
                                    else:
                                        newGene = Gene(row[0])
                                        newGene.list_total.append(final_Split) #append to static list 
                                        newGene.add_Protein(col,row[10])
                                        gene_List.append(newGene) #append it to the list 
                                        break
                        #EXCEPT OS= GN AS SPLITTERS Per blast output data 
                        except:
                            splitLeft = col.split('OS=',)
                            splitRight = splitLeft[1].split(' GN')
                            final_Split = splitRight[0]
                            
                            
                            #Here we are checking if the gene exists in a current list 
                            for i in range(len(gene_List)):
                                if(row[0] == gene_List[i].get_GeneName()):
                                    gene_List[i].add_Protein(final_Split, row[10]) # add Tuple to Gene 
                                    gene_List[i].list_total.append(final_Split) #append to static list 
                                    break
                                    
                                elif(i == len(gene_List)-1):
                                    if(row[0] == gene_List[i].get_GeneName()):
                                        gene_List[i].add_Protein(final_Split, row[10]) # add Tuple to Gene 
                                        gene_List[i].list_total.append(final_Split) #append to static list 
                                        #gene_List[2].print_Proteins()
                                        break
                                    else:
                                        newGene = Gene(row[0])
                                        newGene.list_total.append(final_Split) #append to static list 
                                        newGene.add_Protein(final_Split,row[10])
                                        gene_List.append(newGene) #append it to the list 
                                        break
                            #print(f'{i}: Prediction ::: {final_Split} with an e-value of {row[10]}')

                else:
                    #print(f'{i}: {col}')
                    i = i +1
            i = 0
            j = j +1
            total = total +1
            #print(f'Total Sims run {total}')

    
    #for i in range(len(gene_List)):
   # for lists in gene_List[0].list_total:
        #print(lists)
    #    print(f'---------------------------\nGene: {gene_List[i].get_GeneName()}\n---------------------------')
    #    gene_List[i].print_Proteins()

    #Writer output option
    if(len(sys.argv)==3):
        if(sys.argv[2]=='-w'):
            writerArg(gene_List)
    
        
    xData = []
    yData = []
    pieData = []

    total_Data = []
    #Graphing
   # print(gene_List)
    print(len(gene_List))
    for i in range(len(gene_List)): # E-value
        if(i!=0):
            #print(gene_List[i].get_GeneName())
            name =gene_List[i].get_GeneName()
            
            #print(gene_List[i].return_Top()[-1])
            tups =gene_List[i].return_Top()
            if(tups=="N/A"):
                new_Name = f'{tups}'
            else:
            #    new_Name = f'{tups[0]}'
            #    xData.append(new_Name)
                pieData.append(tups[0])
                total_Data.append(tups)

            # try:
            #     split = tups[1].split('e')
            #     print(split)
            #     if(tups[1]=='o'):
            #         #print(tups)
            #         yData.append(0)
            #     else:
                    
            #         yData.append(np.absolute(float(split[1])))

            # except:
            #     xData.remove(new_Name)
            #     pass
            #     #yData.append(tups)

    
    length = len(total_Data)
    #print(total_Data)
    for i in range(len(total_Data)):
        element = total_Data[i]
        
        try:   
            split = element[1].split('e')
            
            if(element[1]=='o'):
                        #print(tups)
                element[1] = 0
            else:
                total_Data.append((total_Data[i][0],split[1]))
        except:
            #print(f'E-Value Not available : {total_Data[i]}')
            continue
    del total_Data[:length]           
  
    list_X = list(map(lambda x: x[0], total_Data))
    list_Sort = list(map(lambda x: np.absolute(float(x[1])), total_Data))
    merged_Total = list(tuple(zip(list_X,list_Sort)))
    
    merged_Total.sort(key=lambda x : x[1], reverse=True)
    
    

    
    
    x_bar = [i[0] for i in merged_Total]
    y_bar = [i[1] for i in merged_Total]
    

    predef_Amount = 10
    otra = 0
    overflow_Elem = 0 #0 
    
    y_bar = list(map(lambda x: np.absolute(float(x)), y_bar))

    for i in range(len(y_bar)):
        
        if(i > predef_Amount):
            overflow = y_bar[i]
            #print(y_bar[i])
            otra = otra+float(overflow)
            overflow_Elem = overflow_Elem + 1
            #print(f'OVERFLOW NOW {overflow} : Overflow elem : {otra}')
        else:
            continue

    del x_bar[predef_Amount:]
    del y_bar[predef_Amount:]
    
    overflow_Elem = float(overflow_Elem)
    y_Bar_Mean = (otra / overflow_Elem)
   
    x_bar.append('Others')
    y_bar.append(y_Bar_Mean)

    
    # Creating our own dataframe
    data = {"Gene Name": x_bar,
            "E-value": y_bar}
        
    df = pd.DataFrame(data, columns=['Gene Name', 'E-value'])
    df.explode('E-value')
    
    df['E-value'] =  df['E-value'].astype('float')
   # print(df.to_string())
    plt.figure(figsize=(8,6))
    plt.xticks(fontsize= 6)
     #Iterrating over the bars one-by-one
    
    
    plots = sns.barplot(x="Gene Name", y="E-value", data=df)
    for bar in plots.patches:
    
        # Using Matplotlib's annotate function and
        # passing the coordinates where the annotation shall be done
        plots.annotate(format(bar.get_height(), '.2f'),
                    (bar.get_x() + bar.get_width() / 2,
                        bar.get_height()), ha='center', va='center',
                    size=8, xytext=(0, 5),
                    textcoords='offset points')
        
 
    # Setting the x-acis label and its size
    plt.xlabel("Gene Name and Expected Result", size=15)
    
    
    # Setting the y-axis label and its size
    plt.ylabel("E-Value", size=15)
    
    # Finallt plotting the graph
    new_Answer = answer.split('.')

    figName = f'{new_Answer[0]}_box.png'
    wrap_labels(plots,10,True)
    plt.savefig(figName, bbox_inches="tight")

    #################################################
    # PIE CHART
    #################################################

    #Create a set of elements where there are no duplicates
    
    new_Set = set(pieData)
    new_Unique_List = list(new_Set)
    #create a list of integers to map to the set
    int_set_map = []
    #extract data from the set and map to the pieData list to automate duplicates
    for i in range(len(new_Unique_List)):
        #print(f'{new_Unique_List[i]}')
        entry = new_Unique_List[i]
        int_Value = counter(pieData,entry)
        int_set_map.append(int_Value)
    list_Explode = []
    #for i in range(len(new_Unique_List)):
       # print(f'{new_Unique_List[i]} : {int_set_map[i]}')
    
    #Generating top 15 results and listing others as Others
    pie_Zip = list(zip(new_Unique_List,int_set_map))
    pie_Zip.sort(key=lambda x: x[1], reverse=True)
    #
    # others var counter as name 
    # if i > 15 
    # tup[1] + other etc..
    # predefined amount 
    # 
    # #
    predef_Amount = 10
    others = 0

    for i in range(len(pie_Zip)):
        if(i > predef_Amount):
            overflow = pie_Zip[i]
            others = others+overflow[1]
        else:
            continue
    
    xlabels = [i[0] for i in pie_Zip]
    ynums = [i[1] for i in pie_Zip]

    pie_Zip.append(("Others",others))
    num_N = 0
    
    for i in range(len(xlabels)):
        if(xlabels[i]=='N'):
            num_N = i        
    xlabels.remove(xlabels[num_N])
    ynums.remove(ynums[num_N])
    
    del xlabels[predef_Amount:]
    del ynums[predef_Amount:]

    xlabels.append("Others")
    ynums.append(float(others))

   
    
         # Creating explode data
    explodeE = (0.1, 0.2, 0.4, 0.3, 0.1, 0,0.2,0.3,0.1,0.3,0.0)
    
    
    # Creating color parameters
    colors = ( "orange", "cyan", "brown",
            "grey", "indigo", "beige")
    
    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }
    
    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)
    
    # Creating plot
    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(ynums,
                                    autopct = lambda pct: func(pct, int_set_map),
                                    explode = explodeE,
                                    labels = None,
                                    shadow = True,
                                    colors = colors,
                                    startangle = 90,
                                    wedgeprops = wp,
                                    textprops = dict(color ="magenta"))
    
    # Adding legend
    ax.legend(wedges, xlabels,
            title ="Species",
            loc ="center left",
            bbox_to_anchor =(1, 0, 0.5, 1))
    
    plt.setp(autotexts, size = 8, weight ="bold")
    ax.set_title("Species Prediction by top E-value")
    wrap_labels(ax,10)
    # show plo
    #t
    figName = f'{new_Answer[0]}_pie.png'
    plt.savefig(figName, bbox_inches="tight")

    print(f'-------------------------\nExecuted Code. Saved Box and Pie charts for {answer}\n-------------------------')
    




    
        
             
if __name__ == "__main__":
    check_Args()



#Graph of the whole thing 
#1. find way to split data 
#
# 2. find y axis value 
# 
# 
# 3. String Match the names of the trinity genes and split their results as lists according to their names
#  Ideas: lists of tuples, lists as 3-Dimensional vectors?
# Final prediction score for the genes ? 
# X- axis must be the trinity gene
# 
# X-Axis - frequency species 
# 10-100 sign threshold 
# y- axis number of genes hit within a threshold 
# 
# Pie Chart
# Count up the instances of each gene 
# Zip int Map and labels together and sort by results 
# Record the top 10-20 results and put that into a file
# 
# #