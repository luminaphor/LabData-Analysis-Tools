import xlsxwriter
import csv
import os
#import scipy
#import numpy

def convertToExp(s):
        newS=[]
        for i in s:
                newS.append(float(i))
        return newS

#def findSTDev(wbName,sheetName):
#       sheetName.write_formula('E1',' =STDEV()')

def plotGraph(wbName,sheetName):
        chart=wbName.add_chart({'type':'scatter'})

        chart.add_series({'categories': '={}!$A:$A'.format(sheetName)})
        chart.add_series({'values': '={}!$B:$B'.format(sheetName)})

        sheetName.insert_chart('E1',chart)

def readInData(fileName):
        with open(fileName) as csv_file:
                        
                csv_reader = csv.reader(csv_file,delimiter=',')
                line_count=0
                
                shifts=[]
                intensities=[]
                
                for row in csv_reader:
                        shift,intensity=row
                        
                        shifts.append(shift)
                        intensities.append(intensity)
                
                        line_count+=1

        shifts=convertToExp(shifts)
        intensities=convertToExp(intensities)
        
        print("Processed {} lines of data.".format(line_count))
        
        return shifts,intensities,line_count

def writeDataToDoc(x,y,wbName,sheetName):
        sheet=wbName.add_worksheet(sheetName)
        row=0
        for i in x:
                sheet.write(row,0,i)
                sheet.write(row,1,y[row])
                row+=1

#def getFiles(folderName,extension):
      #  fileNames=[]
      #  for file in os.listdir(folderName):
      #          if file.endswith(extension):
      #                  fileNames.append(file)
                        
        #return fileNames

       # print("These are all files found in the specified directory: ")

       # count=1
       # for file in fileNames:
       #         print("{}. {}".format(count,file))
       #         count+=1

       # choice=input("Use all for standard deviation?  y/n")

       # if choice == "y":
       #         print("Answered yes")
       #         return fileNames
                
       # elif choice == "n":
       #         chosenFileNames=[]
       #         print("Enter file numbers you wish to include. Type 'done' when ready.")
#
#                run=True
#                while run:
#                        index=input()
#                        if index=="done":
#                                run=False
#                        else:
#                                index=int(index)-1
 #                               chosenFileNames.append(fileNames[index])
                
  #              for file in chosenFileNames:
   #                     print(file)
                
    #            return chosenFileNames

def getFiles():
        
        fileNames=[]
        run = True
        
        currentPath=None
        while run:
                count = 1
                print("Listing all files in current directory. Type index of folder you would like to navigate to next. Type 'found' when at desired folder.")
                
                #for file in os.listdir():
                for file in os.listdir(currentPath):
                        #if file.endswith(extension):
                                #fileNames.append(file)
                        print("{}. {}".format(count,file))
                        count += 1
                                
                getIndex=input()
                
                if getIndex=='found':
                        run=False
                
                else:
                        getIndex=int(getIndex)
                        getIndex-=1
                        currentPath=(os.listdir()[getIndex])+'/'
                                
                        
        #return fileNames
                
        print("These are all CSV files found in the specified directory: ")
        count=1       
        for file in os.listdir(currentPath):
                if file.endswith(".CSV"):
                        fileNames.append(file)
                        #print("{}. {}".format(count,file))
                        #count+=1
       
        for file in fileNames:
                print("{}. {}".format(count,file))
                count+=1

        choice=input("Use all for standard deviation?  y/n")

        if choice == "y":
                print("Answered yes")
                return fileNames
                
        elif choice == "n":
                chosenFileNames=[]
                print("Enter file numbers you wish to include. Type 'done' when ready.")

                run=True
                while run:
                        index=input()
                        if index=="done":
                                run=False
                        else:
                                index=int(index)-1
                                chosenFileNames.append(fileNames[index])
                
                for file in chosenFileNames:
                        print(file)
                
                return currentPath,chosenFileNames
				
outputName= input("Enter a name for your output file: ")
outputName=outputName+".xlsx"
#outputName='ramanData.xlsx' #defines output filename
outputFile=xlsxwriter.Workbook(outputName) #defines output workbook
#retrievePath="Group 2 Raman Data"

#allDataFiles=getFiles(retrievePath,".CSV")
retrievePath,allDataFiles=getFiles()
for file in allDataFiles:
        shifts,intensities,linesRead=readInData(retrievePath+"\\"+file)
        
        writeDataToDoc(shifts,intensities,outputFile,file)

        #shifts=numpy.array(shifts)
        #intensities=numpy.array(intensities)

        #plotGraph(outputFile,file)

outputFile.close()
                
exit = input("--> Exit ?")
