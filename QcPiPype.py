import os
import subprocess
import platform
from time import sleep
import datetime
from multiprocessing import Process
from timeit import default_timer as timer
import shutil

def chainArt():
    print("""
.d888b.
.8888888
.8888888>               ____
 `Y888P' `=-=-=-=-=-=-<|____|
""")

def asciArt():
    print("""
______           _    _____  _____   ______  _ ______                    
|  ___|         | |  |  _  |/  __ \  | ___ \(_)| ___ \                   
| |_  __ _  ___ | |_ | | | || /  \/  | |_/ / _ | |_/ /_   _  _ __    ___ 
|  _|/ _` |/ __|| __|| | | || |      |  __/ | ||  __/| | | || '_ \  / _ | 
| | | (_| |\__ \| |_ \ \/' /| \__/\  | |    | || |   | |_| || |_) ||  __/
\_|  \__,_||___/ \__| \_/\_\ \____/  \_|    |_|\_|    \__, || .__/  \___|
                                                       __/ || |          
                                                      |___/ |_|   
                                        +-+
         +---+--+----+-+-+-+--+--+--+-+-+-+ | ++++++++++++++++++++++++++++
         |   |  |    +-+ | |  |  |  | | |+| |  @copyright Tyler Desharnais 
         |   |  |    |  ++ |  +--+--+-+ |+| | ++++++++++++++++++++++++++++
         +---+--+----+--++-+--+-------+-+-+ |
                                        +-+
==========================================================================
""")
    
def progressBar(progressMax, current):
    percent = int((current/progressMax)*100)
    drawMarkers = int(percent/10)
    drawLines = 10-drawMarkers
    marker = "█"
    line = "_"
    for i in range(drawMarkers):
        marker = marker + "█"
    for i in range(drawLines):
        line = line + "_"
    
    print("Progress Total\n-------------\n")
    print(f'{marker}{line} {percent}%')
    print("-----------------------------\n")

def findCwd(directory, workDir, osType):
    
    
    #subprocess.run(["cd","~"], check=True)
    if (osType == "Windows"):

        print(os.getcwd())
        print("I'm sorry. Windows isn't a currently supported OS for QcPiPype")
        
    else:
        root = "/"
        today = datetime.date.today()
        now = datetime.datetime.now()
        d1 = today.strftime("%d%m%Y")
        directPy = "PiPype"
        newDirect = now.strftime("%H%M") #filefolder
        os.chdir("/")
        os.chdir(workDir)

        if(os.path.isdir("PiPype")==False):
            os.mkdir(directPy)
            os.chdir(directPy)
        else:
            os.chdir(directPy)

        if(os.path.isdir(d1)==False):
            os.mkdir(d1)
            os.chdir(d1)


        else:
            os.chdir(d1)
            os.mkdir(newDirect)
            os.chdir(newDirect)
        
        print("Directories Created and Saved\n--------------\n")
        saveDirect = os.path.join(root,newDirect) #saves directory
        sleep(2)

        fileDict = []
        print("Finding FastQC Files")
        
        os.chdir(root)
        directoryPath = os.path.join(root,directory)
        
        print("Current FastQC files to link\n--------------\n")
        print(os.getcwd())
        print(directory)
        
        for file in os.listdir(directory):
            if file.endswith(".fastq"):
                print(file)
                fileDict.append(os.path.join(root,file))

        print("\nFiles have been added")
        sleep(2)
        print("")
        chainArt()
        print("------------------------\n")
        print(f'Linking and Chaining Files to {workDir}...')
        print("")

        os.chdir(root)
        os.chdir(workDir)
        os.chdir(directPy)
        os.chdir(d1)
        
        
        progressMax = len(fileDict)
        txtFileName = f'PypeOut{now.strftime("%H%M")}'

        for i in range(len(fileDict)):
            print(fileDict[i])
            newDir = directory+fileDict[i]
            subprocess.run(['ln','-sf',newDir])
            print(f'\nProgress: {(i/len(fileDict))*100}\n')
            print(fileDict[i]+ " has been linked")
        
        print("Files Linked.")
        sleep(1)
        os.system("clear")
        asciArt()
        print("Running FastQC Analysis...")
        sleep(2)

        #create file
        f = open(txtFileName, "x")
        f.close()

        #The magic happens here
        for i in range(len(fileDict)):      
            p = Process(target=spawnProcess,args=(txtFileName,fileDict[i],i,progressMax))
            p.start()
            print(f'Process for {fileDict[i]} is alive: {p.is_alive}')
        p.join()
        
        #check if processes are dead
        print("Checking if processes are dead")
        sleep(1)

        for i in range(len(fileDict)):
            print(f'Process for {fileDict[i]} is alive: {p.is_alive}')
        
        sleep(2)

       # os.system("clear")
        asciArt()
        print("\nAll processes have been executed\n")
        sleep(1)
        print("Gernerating Html reports..")
        sleep(1)
        HTMLSplit(d1,root,workDir,directPy)
        sleep(2)
        os.system("clear")
        asciArt()
        chainArt()
        print("-----------------------")
        print("Process Fully Complete!")
        print("-----------------------")
        sleep(0.5)
        print("Exiting") 
        print("-----------------------")
        sleep(4)
        exit()




               

                    

def HTMLSplit(d1,root,workDir,directPy):
    os.chdir(root)
    os.chdir(workDir)
    os.chdir(directPy)
    pathyPi = os.getcwd()
    os.chdir(d1)
    sourceyPi = os.getcwd()
    newFolder = 'HTMLReports'
    
    if(os.path.isdir(newFolder)):
        sourceFile = os.listdir(sourceyPi)
        newPath = os.path.join(d1,newFolder)
        osPath = os.path.join(os.getcwd(),newPath)
        
        for file in sourceFile:
            if file.endswith('.html'):
                shutil.move(os.path.join(os.getcwd(),file),os.path.join(pathyPi,file))
    else:
        sourceFile = os.listdir(sourceyPi)
        os.mkdir(newFolder)
        newPath = os.path.join(d1,newFolder)
        osPath = os.path.join(os.getcwd(),newPath)
        
        for file in sourceFile:
            if file.endswith('.html'):
                shutil.move(os.path.join(os.getcwd(),file),os.path.join(pathyPi,file))

       # subprocess.run(["cd","~"], check=True)
       # subprocess.run(["cd", workDir], check=True)
       
def spawnProcess(fileName, fileDir, fileNumber,progressMax):
    start = timer()
    
    print('Parent process id:', os.getppid())
    print('Process id:', os.getpid())
    print(f'File: {fileDir}')
    
    stringNum = str(fileNumber)
    txtName = fileName+stringNum
    concat = f'{txtName}.txt'
    newsplit = fileDir.split("/")
    
    with open(f'{newsplit[1]}.txt','x')as file:
        result = subprocess.run(['fastqc',newsplit[1]], stdout=file, text=True)
        print(f'Errors: {result.stderr}')
        print(result.stdout)
        
        
        
    #progressBar(progressMax,fileNumber)
    end = timer()
    print(f'\nTime Elapsed for Process ID {os.getpid()} : {end-start}\n')




def main():
    osType = platform.system()
    #directUse = "/data_drive/datasets/RCC_Data/Fasteris-Ochrophyte_Haptophyte"
    asciArt()
    directUse = input("Please input directory for extraction: ")
    root = input("State where the files should be stored: ")
    #root = "/home/desha005"
    findCwd(directUse, root, osType)
    




if __name__ == "__main__":
    main()

