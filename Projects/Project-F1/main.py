# Importing required modules
from tabulate import tabulate
import sys
# Main dictionary to store drivers detail and lap timing
main_dict={}

def load_files():
# This function loads the required files and stores the details into main_dict
    global f,f1,f2,f3,main_dict
    try:
        # Open files containing driver details and lap times
        f=open("f1_drivers.txt",'r')
        f1=open("lap_times_1.txt",'r')
        f2=open("lap_times_2.txt",'r')
        f3=open("lap_times_3.txt",'r')

        # Read driver details and store in main_dict
        for x in f.readlines():
            x=x.replace('\n','')
            main_dict[x.split(',')[1]]={'detail':{'Jersey':x.split(',')[0],'Fullname':x.split(',')[2],'Sponcer':x.split(',')[3]}}
    except:
        # Handling missing files
        print("File not found!!!")
        quit()

def vizualization(x,y,xlabel,ylabel,title):
# Function to visualize data using a bar chart
    try:
        choice=input("Do you want to vizualize this data(Y/N): ").lower()
        if choice=='y':
            import matplotlib.pyplot as plt
            plt.barh(x,y)
            plt.xlabel(xlabel,fontsize=17)
            plt.ylabel(ylabel,fontsize=17)
            plt.title(title,fontsize=20)
            plt.grid(axis='x',linestyle='--',color='#000000',alpha=0.6)
            plt.show()
        else:
            pass
    except:
        # Handling missing library
        print("Sorry!! Required Library not found")

def lap_values(fn,n):
# This function updates lap time in the main_dict
    global main_dict
    global lapn
    lapn={} # Temporary dictionary to store lap time
    next(fn) # Skip the headers
    for x in fn.readlines():
        x=x.replace('\n','')
        if x[:3] in lapn.keys():
            lapn[x[:3]].append(float(x[3:]))
        else:
            lapn[x[:3]]=[]
            lapn[x[:3]].append(float(x[3:]))
    for key,value in lapn.items():
        main_dict[key]=main_dict[key] | {f'lap{n}':value}

def racename(filename,n):
# Function to print the name of the race from the file
    filename.seek(0)
    print(f"The name of race {n} is {filename.readlines(1)[0].strip()}.")

def fastest(lap):
# Function to find and display the fastest driver for a specific lap
    lst=[]
    fast=10000
    for x,y in main_dict.items():
        if min(y[lap])<fast:
            lst.clear()
            fast=min(y[lap])
            lst.append(x)
    print(f"The fastest in {lap} is {lst[0]}[{main_dict[lst[0]]['detail']['Fullname']}] with speed {fast}.")

def individual_fastest():
# Function to display the fastest lap time of each driver
    lst=[]
    name=[]
    fast=[]
    for x,y in main_dict.items():
        min_time=min([min(y['lap1']),min(y['lap2']),min(y['lap3'])])
        lst.append([x,y['detail']['Jersey'],y['detail']['Fullname'],y['detail']['Sponcer'],min_time])
        name.append(y['detail']['Fullname'])
        fast.append(min_time)
        
    def return_position(d):
        return d[4]
    lst.sort(key=return_position,reverse=True)
    print("The fastest time of each driver is: ")
    print(tabulate(lst, headers=["Driver","Jersey No","Fullname","Team","Minimum time"],tablefmt="grid"))
    vizualization(name,fast,'Fastest Speed','Driver','Fastest time for each Driver')

def average_overall():
# Function to calculate and display the overall average time
    lst=[]
    for x,y in main_dict.items():
        lst+=y['lap1']
        lst+=y['lap2']
        lst+=y['lap3']
    print(f"The overall average time is {round(sum(lst)/len(lst),2)}.")

def individual_average():
# Function to display the average time of each driver
    lst=[]
    name=[]
    average=[]
    def return_position(d):
        return d[4]
    for x,y in main_dict.items():   
        lstp=[]
        lstp+=y['lap1']
        lstp+=y['lap2']
        lstp+=y['lap3']
        averagem=round(sum(lstp)/len(lstp),2)
        name.append(y['detail']['Fullname'])
        average.append(averagem)
        lst.append([x,y['detail']['Jersey'],y['detail']['Fullname'],y['detail']['Sponcer'],averagem])
    lst.sort(key=return_position,reverse=True)
    print("The average time of each driver is: ")
    print(tabulate(lst, headers=["Driver","Jersey No","Fullname","Team","Average time"],tablefmt="grid"))
    vizualization(name,average,'Average Speed','Driver','Average time for each Driver')

def formula_one():
# This function is a main menu to interact with the users
    if len(sys.argv)==2:
        choice=sys.argv[1]
        if choice=='1':
            racename(f1,1)
            racename(f2,2)
            racename(f3,3)
        elif choice=='2':
            fastest('lap1')
            fastest('lap2')
            fastest('lap3')
        elif choice=='3':
            individual_fastest()
        elif choice=='4':
            average_overall()
        elif choice=='5':
            individual_average()
        elif choice=='q':
            quit()
        else:
            print("Invalid code entered")
    else:
        print("Insufficient arguements passed")

# Initializing the required functions
load_files()           
lap_values(f1,1)
lap_values(f2,2)
lap_values(f3,3)

# Executes the formula_one function when the script is run directly.
if __name__=="__main__":
    formula_one()











