import os
import pandas as pd
import numpy as np

def read_Data():
    with open('data.txt', 'r') as r:
        Lines = r.readlines()
        
  
            # remove spaces
        #lines = [line.replace(' ', '') for line in Lines]
        lines = [line.split() for line in Lines]
        
            


        # finally, write lines in the file
        with open('file.txt', 'w') as f:
            for i in range(len(lines)):
                f.writelines(f'{lines[i][0]},{lines[i][1]}\n')
            #f.writelines(str(lines))
        path = os.getcwd()
        os.rmdir('fafiles')
        os.mkdir('fafiles')
        
        os.chdir('fafiles')
        for i in range(len(lines)):
            textName = lines[i][0]
            textName_Append = textName+'.fa'
            with open(textName_Append,'w') as textWriter:
                #writer.write("%s\n" % item.get_GeneName())
                textWriter.write(">%s\n" % lines[i][0])
                textWriter.write("%s\n" % lines[i][1])
                textWriter.close()



def main():
    cols = [0,3]
    xl_File = pd.read_excel("TableS1.xlsx", sheet_name="Alignment matrix", usecols=cols)
    xl_File['Sequence']
    with open('data.txt', 'a') as f:
        dfAsString = xl_File.to_string(header=False, index=False)
        f.write(dfAsString)
    read_Data()
    
    














if __name__ == "__main__":
    read_Data()