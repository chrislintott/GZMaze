import time
import pyperclip
import csv

#local information


def check_status(bar=1,bulge=0):
        
    clipboard_old=""
    while True:
        clipboard = pyperclip.paste()
        
        if (clipboard != clipboard_old):
            print "New ID!",clipboard
            clipboard_old = clipboard

            #Load data object for that classification
            # Have lookup table of the form id, bar, bulge  where bar&bulge are out of 1,0

            classification=read_object_classification(clipboard_old)  #in the form [id,bar,bulge]
            #classification=['1ds4',1,0]    #example of a barred galaxy withotu a bulge
            print "Galaxy data",classification,"Location data",bar,bulge
            status=bar==classification[1] and bulge==classification[2]

            if status:
                print "Success :) Do the things!"

            else:
                print "Fail :( No bubbles for you"

            print '-------------'

        time.sleep(0.5)


def read_object_classification(clipboard_old):
    filename="classification_data.csv"
    with open(filename) as f:
        reader=csv.reader(f,delimiter=',')
        next(reader)
        for row in reader:
            if row[0]==str(clipboard_old):
                row=[int(item) for item in row]
                return row
        print "Id not found. Return dummy data"
        return ['0000000',2,2]



def write_example_file():
    filename="classification_data.csv"
    IDS=['1243233','2345473','2233432','9987679','3345363','3934322']
    bulge=[0,0,0,1,1,1]
    bar=[1,0,0,1,0,1]
    with open(filename,'w') as f:
        writer=csv.writer(f)
        writer.writerow(['Id','bulge','bar'])
        for i in range(len(IDS)):
            writer.writerow([IDS[i],bulge[i],bar[i]])
