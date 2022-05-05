from ast import Global
import csv
import random
import getpass
from distutils.errors import DistutilsFileError
from ntpath import join
from operator import index
import time
import shutil
import tkinter
import tempfile
import subprocess
from tkinter import *
from tkinter import ttk
from cgitb import enable, text
from cProfile import label
from tokenize import Name
from doctest import master
from datetime import datetime
from tracemalloc import start
from random import expovariate
from turtle import color, update, width
from tkcalendar import DateEntry
from sqlite3 import enable_shared_cache
from tkinter.filedialog import askdirectory, asksaveasfile





def settemp():
    #Get local temp file
    temploc = tempfile.gettempdir()
    #Clean string
    temploc = temploc.replace('\'', '\\')
    #Make file name
    now = datetime.now()
    currenttime = now.strftime("%H%M%S")
    #Set output string
    temploc = '"%s""%s".csv' % (temploc, currenttime)
    #Clean output string
    temploc = temploc.replace('"', '')
    #Change global temp location avarible
    global templocation
    templocation = temploc
    return temploc
#Init Clear Temp location 
templocation = ""

def donthing():
    print("Do Nothing")

#Initial Canvas frame
root = tkinter.Tk()
#Set Program Name
root.title("Gary")
#Set c as canvas
c = tkinter.Canvas(root, bg="White", height=655, width=1000)
c.pack(fill="both", expand=True)



#Init Tree/Table Back Frame
#Treeframe = tkinter.Frame(c)
Treeframe = Frame(c, width= 600 , height=550)
Treeframe.pack(pady=10)
c.create_window(693, 302, window=Treeframe)


#scrollbar 
scrolly = Scrollbar(Treeframe)

scrolly.pack(side=RIGHT, fill=Y)

c.pack()

tree = ttk.Treeview(Treeframe, yscrollcommand=scrolly.set, height=550,  )

Treeframe.pack_propagate(0)




tree.pack()


#Configure croll bar
scrolly.config(command=tree.yview)
#tree.pack(fill='both', expand=True)



# Export Option Boxes
c1v = BooleanVar()
c1 = Checkbutton(root, text="Account Created", bg="White",variable=c1v)
c.create_window(83, 335, window=c1)
c2v = BooleanVar()
c2 = Checkbutton(root, text="Company", bg="White",variable=c2v)
c.create_window(185, 335, window=c2)
c3v = BooleanVar()
c3 = Checkbutton(root, text="Country", bg="White",variable=c3v)
c.create_window(270, 335, window=c3)
c4v = BooleanVar()
c4 = Checkbutton(root, text="Department", bg="White",variable=c4v)
c.create_window(180, 435, window=c4)
c5v = BooleanVar()
c5 = Checkbutton(root, text="EmailAddress", bg="White",variable=c5v)
c5.select()
c.create_window(74, 365, window=c5)

c6v = BooleanVar()
c6 = Checkbutton(root, text="Payroll Number", bg="White",variable=c6v)
c.create_window(190, 365, window=c6)
c7v = BooleanVar()
c7 = Checkbutton(root, text="Enabled", bg="White",variable=c7v)
c.create_window(283, 365, window=c7)
c8v = BooleanVar()
c8 = Checkbutton(root, text="LastLogonDate", bg="White",variable=c8v)
c.create_window(77, 435, window=c8)
c9v = BooleanVar()
c9 = Checkbutton(root, text="Manager", bg="White",variable=c9v)
c.create_window(61, 400, window=c9)
c10v = BooleanVar()
c10 = Checkbutton(root, text="Organization", bg="White",variable=c10v)
c.create_window(160, 400, window=c10)
c11v = BooleanVar()
c11 = Checkbutton(root, text="PrimaryGroup", bg="White",variable=c11v)
c.create_window(270, 400, window=c11)

def getexports():
    exports = []
    exports.clear
    if c1v.get() == True:
        exports.append("Created")
    if c2v.get() == True:
        exports.append("Company")
    if c3v.get() == True:
        exports.append("Country")
    if c4v.get() == True:
        exports.append("Department")
    if c5v.get() == True:
        exports.append("EmailAddress")
    if c6v.get() == True:
        exports.append("EmployeeNumber")
    if c7v.get() == True:
        exports.append("Enabled")
    if c8v.get() == True:
        exports.append('LastLogonDate')
    if c9v.get() == True:
        exports.append("Manager")
    if c10v.get() == True:
        exports.append("Organization")
    if c11v.get() == True:
        exports.append("PrimaryGroup")
    return exports

"""

tree['show'] = 'headings'


#def treeviewup():
for child in tree.get_children():
    tree.delete(child)

print(tree.winfo_width)

tree["columns"] = []

cols = []

cols.append("Username")
cols.append("Full Name")

seout = getexports()  
for x in seout:
    cols.append(x)

tree["columns"] = cols
out = tree["columns"]

wi = int(600/len(out))
print("wi = ", wi)

for idx, val in enumerate(out):
    o = idx
    print("setting ", o, " to ", wi)
    if o == len(out):
        tree.column(o, stretch=NO, minwidth=0, width=wi, anchor=CENTER)
    else:
        tree.column(o, stretch=NO, minwidth=0, width=wi, anchor=CENTER)


tree.pack()
#if len(exports) > 1:
for x in out:
    tree.heading(x, text=x)
    print(x)

print("Leaving function")


"""


def treewi():
    for child in tree.get_children():
        tree.delete(child)


    print(tree.winfo_width)

    tree["columns"] = []

    cols = []

    cols.append("Full Name")
    cols.append("Username")

    seout = getexports()  
    for x in seout:
        cols.append(x)

    tree["columns"] = cols
    out = tree["columns"]

    wi = int(600/len(out))
    print("wi = ", wi)
    print("len =", len(out))

    for idx, val in enumerate(out):
        o = idx 
    if o == len(out):
        tree.column(o, stretch=YES, minwidth=20, width=wi, anchor=E)
    else:
        tree.column(o, stretch=YES, minwidth=0, width=wi, anchor=CENTER)
   
   
    #if len(exports) > 1:
    for x in out:
        tree.heading(x, text=x)
        print(x)
    print("Leaving function")


    tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
    tree.heading('#0', text="")
  

treewi()


#treeviewup()

###test1 = tkinter.Button(text="Search ", command=treewi,bd="0", bg="Light Grey", height=5, width=53)
###c.create_window(579, 500, window=test1)


# update csv viewer for in datr range


def updatetree(floc, switch):
    treewi()
    tree.delete(*tree.get_children())
    with open(floc) as f:
        reader = csv.DictReader(f, delimiter=',')
        next(f)


        filters = getexports()  
        print(len(filters))

        if len(filters) == 1:
            for row in reader:
                Name = row['DisplayName']
                email = row['sAMAccountName']
                s1 = row[str(filters[0])]
                tree.insert("", 0, values=(Name, email, s1))
        elif len(filters) == 2:
            for row in reader:
                Name = row['DisplayName']
                email = row['sAMAccountName']
                s1 = row[str(filters[0])]
                s2 = row[str(filters[1])]
                tree.insert("", 0, values=(Name, email, s1, s2))
        elif len(filters) == 3:
            for row in reader:
                Name = row['DisplayName']
                email = row['sAMAccountName']
                s1 = row[str(filters[0])]
                s2 = row[str(filters[1])]
                s3 = row[str(filters[2])]
                tree.insert("", 0, values=(Name, email, s1, s2, s3))
        elif len(filters) == 4:
            for row in reader:
                Name = row['DisplayName']
                email = row['sAMAccountName']
                s1 = row[str(filters[0])]
                s2 = row[str(filters[1])]
                s3 = row[str(filters[2])]
                s4 = row[str(filters[3])]
                tree.insert("", 0, values=(Name, email, s1, s2, s3, s4))
        elif len(filters) == 5:
            for row in reader:
                Name = row['DisplayName']
                email = row['sAMAccountName']
                s1 = row[str(filters[0])]
                s2 = row[str(filters[1])]
                s3 = row[str(filters[2])]
                s4 = row[str(filters[3])]
                s5 = row[str(filters[4])]
                tree.insert("", 0, values=(Name, email, s1, s2, s3, s4, s5))
        elif len(filters) == 6:
            for row in reader:
                Name = row['DisplayName']
                email = row['sAMAccountName']
                s1 = row[str(filters[0])]
                s2 = row[str(filters[1])]
                s3 = row[str(filters[2])]
                s4 = row[str(filters[3])]
                s5 = row[str(filters[4])]
                s6 = row[str(filters[5])]
                tree.insert("", 0, values=(Name, email, s1, s2, s3, s4, s5, s6))
        elif len(filters) == 7:
            for row in reader:
                Name = row['DisplayName']
                email = row['sAMAccountName']
                s1 = row[str(filters[0])]
                s2 = row[str(filters[1])]
                s3 = row[str(filters[2])]
                s4 = row[str(filters[3])]
                s5 = row[str(filters[4])]
                s6 = row[str(filters[5])]
                s7 = row[str(filters[6])]
                tree.insert("", 0, values=(Name, email, s1, s2, s3, s4, s5, s6, s7))
        else:
            for row in reader:
                Name = row['DisplayName']
                email = row['sAMAccountName']
                tree.insert("", 0, values=(Name, email))
        
        #root.config(cursor="")
        #root.configure()

            #tree.pack()
            #c.pack()





def run(cmd):
    print(cmd)
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    CREATE_NO_WINDOW = 0x08000000
    completed = subprocess.run(["powershell", "-Command", cmd],startupinfo=si, capture_output=True, creationflags=CREATE_NO_WINDOW)
    return completed


# (left hor, left ver, right hor, right ver)
# username box
c.create_rectangle(10, 30, 380, 100, fill='white',
                   outline='Light Grey', width=2)


# username text
namehed = tkinter.Label(root, text="Username",
                        background="White", anchor="nw", wraplength=100)
c.create_window(55, 29, window=namehed)
# username input
#name = str(getpass.getuser())
#print(name)
namein = tkinter.Text(root, background="White", wrap='none')
namein.configure(wrap=None)

#namein.insert(name)
c.create_window(105, 65, window=namein, width=150, height=25)
namein.focus()

# get input


def getIn():
    inpu = namein.get(1.0, "end-1c")
    return inpu


# created between box
c.create_rectangle(10, 120, 380, 190, fill='white',
                   outline='Light Grey', width=2)


# horizontal -> vertical

# date pickers
# start date headrer
caltitle = tkinter.Label(root, text="Created Between",
                         background="White", anchor='nw', wraplength=100)
c.create_window(75, 125, window=caltitle, width=100, height=30)

calstarthe = tkinter.Label(root, text="&",
                           background="White", anchor="nw", wraplength=100)
c.create_window(160, 154, window=calstarthe)

# star date picker
calstart = DateEntry(root, date_pattern='dd/mm/y',  selectmode='day')
c.create_window(85, 155, window=calstart, width=110, height=21)

# end date picker
calend = DateEntry(root, date_pattern='dd/mm/y', selectmode='day')
c.create_window(237, 155, window=calend, width=110, heigh=21)


# sort dates and returns them in the correct format
def sortdate():
    startd = str(calstart.get_date())
    startd = startd.replace("-", "/")
    endd = str(calend.get_date())
    endd = endd.replace("-", "/")
    return startd, endd

# prepares powershell request and returns string


def userinrange(sdate, endd, loc):

    filters = getexports() 
    filterstring = ""
    for x in filters:
        filterstring = x, ","

        
    com = dropdowncoms.get()
    dep = dropdowndeps.get()
    
    filters = getexports() 
    filters = filters 
    filterstring = ','.join(filters)  
    
    print("filters len =" ,len(filters))

    
    command = 'Get-ADUser -Filter * -Properties Created,DisplayName,sAMAccountName  | Where-Object { $_.Created -gt "%s"  -and $_.Created -le "%s"} | select DisplayName,sAMAccountName  |Export-CSV -path %s' % (sdate, endd, loc)
    
    if com != "All companies" and dep != "All Departments" and len(filters) >= 1:
        command = 'Get-ADUser -Filter {(Company -eq "%s") -and (department "%s")} -Properties %s,Created,DisplayName,sAMAccountName | Where-Object { $_.Created -gt "%s"  -and $_.Created -le "%s"} | select  %s,DisplayName,sAMAccountName | Export-CSV -path %s' % (com, dep,filterstring, sdate, endd,filterstring, loc)
    elif com != "All companies" and dep != "All Departments" and len(filters) == 0:
        command = 'Get-ADUser -Filter {(Company -eq "%s") -and (department "%s")} -Properties Created,DisplayName,UserLogonName | Where-Object { $_.Created -gt "%s"  -and $_.Created -le "%s"} | select DisplayName,UserLogonName | Export-CSV -path %s' % (com, dep, sdate, endd, loc)
    #companies
    elif com != "All companies" and len(filters) >= 1:
        command = 'Get-ADUser -Filter {Company -eq "%s"} -Properties %s,Created,DisplayName,sAMAccountName | Where-Object { $_.Created -gt "%s"  -and $_.Created -le "%s"} | select %s,DisplayName,sAMAccountName | Export-CSV -path %s' % (com, filterstring, sdate, endd, filterstring, loc)
    elif com != "All companies" and len(filters) == 0:
        command = 'Get-ADUser -Filter {Company -eq "%s"} -Properties Created,DisplayName,sAMAccountName | Where-Object { $_.Created -gt "%s"  -and $_.Created -le "%s"} | select DisplayName,sAMAccountName | Export-CSV -path %s' % (com, sdate, endd, loc)
    #departments
    elif dep != "All Departments" and len(filters) >= 1:
        command = 'Get-ADUser -Filter {Department -eq "%s"} -Properties %s,Created,DisplayName,sAMAccountName | Where-Object { $_.Created -gt "%s"  -and $_.Created -le "%s"} | select %s,DisplayName,sAMAccountName | Export-CSV -path %s' % (dep, filterstring, sdate, endd, filterstring, loc)
    elif  dep != "All Departments" and len(filters) == 0:
        command = 'Get-ADUser -Filter {Department -eq "%s"} -Properties Created,DisplayName,sAMAccountName | Where-Object { $_.Created -gt "%s"  -and $_.Created -le "%s"} | select DisplayName,sAMAccountName | Export-CSV -path %s' % (dep, sdate, endd, loc)
    elif len(filters) >= 1:
            command = 'Get-ADUser -Filter * -Properties %s,Created,DisplayName,sAMAccountName  | Where-Object { $_.Created -gt "%s"  -and $_.Created -le "%s"} | select %s,DisplayName,sAMAccountName | Export-CSV -path %s' %(filterstring, sdate, endd, filterstring, loc)
    #command = 'Get-ADUser -Filter * -Properties Created,EmailAddress,Displayname,whencreated | Where-Object { $_.Created -gt "%s"  -and $_.Created -le "%s"} | select whencreated, EmailAddress, DisplayName |Export-CSV -path %s' % (
    #   sdate, endd, loc)
    print("Command to powershell =", command)
    return command


# when run button pressed gets date sorts and then runs command
def searchfun():



    inp = getIn()
    # if username input is has text search for user instead
    if len(inp) > 1:
        getuser()
    else:
        dates = sortdate()
        print("Getting user from date ranges", dates[0], " + ", dates[1])
        # set temp path to save file
        loc = settemp()
        psstr = userinrange(dates[0], dates[1], loc)
        output = run(psstr)
        updatetree(loc, 1)
        print(output)


    root.config(cursor="arrow")


def saveas():
    if len(templocation) > 1:
        oldloc = str(templocation)
        oldloc = oldloc.replace('\\', "/")
        oldloc = oldloc.replace('"', '')
        newloc = askdirectory()
        newloc = newloc.replace('\\', "/")
        newloc = newloc.replace('"', '')
        newloc = "%s//GaryOutput.csv" % (newloc)
        print(oldloc, newloc)
        shutil.copy2(oldloc, newloc)
    else:
        tkinter.messagebox.showerror(
            title="Error", message="No data to export")


# drop down list
comps = ["All companies", "18 Montrose", "9600", "Big and Tall", "Brandmax", "Brands Inc", "BrandsInc", "Contoso", "Cruise", "Cruise Fashion", "Delima", "Direct Golf", "Disport",
         "DSILES", "Dsiport", "EDI Helpdesk", "Evans Cycles", "Everlast Fitness", "Everlast Gyms", "Everlastfitness", "Firetrap", "Fitness", "Flannels", "Fraser Group", "Frasers Group",
         "Frasers Groups", "Gaelic Boots", "GAME", "Heatons", "House of Fraser", "IBML", "Jack Wills", "Lillywhites", "lmstore", "Lonsdale Boxing", "Mega Sport", "Megasport", "Nevica",
         "Partoo Admin", "Printworks", "Pulp", "PWPTennis", "Republic", "Robinsons", "SD Fitness", "Slazenger", "Smith Brooks", "Sorting Systems", "Soulcal", "Sport Service GmbH",
         "Sport2000", "Sportland", "Sports Direct", "Sports Direct Asia", "Sports Direct Fitness", "Sports Direct Property", "Sports Soccer", "Sports World", "Sportsdirect",
         "SportsDirect Fitness", "Sportsdirect.com", "Sportsdirectfitness", "Sports-soccer", "sweatshop", "Tucci Store", "USC", "Vanmildert", "Yeomans"]
var = StringVar()
dropdowncoms = ttk.Combobox(root, textvariable=var)
dropdowncoms['values'] = comps
dropdowncoms.current(0)
dropdowncoms['state'] = 'readonly'
c.create_window(100, 248, window=dropdowncoms)

# organization box
c.create_rectangle(10, 210, 380, 285, fill='white',
                   outline='Light Grey', width=2)

# dropdown list header
drophea = tkinter.Label(text="Organization Filter", bg="White")
c.create_window(77, 208, window=drophea)


# departments drop down list
deps = ["All Departments", "046801", "545", "801", "805", "808", "8830 Europe Finance Dept", "8886 Austria Retail Projects", "9100 Retail Support", "9918", "Aberdeen GA 2375", "Aberdeen SPD GA 2972",
        "Aberystwyth SPD GA 2850", "Administration 9150", "Aintree FIT 1082", "Alfa SL LV 1202", "Amstetten SD AT 1034", "Area Managers 9101", "Area/Regional Managers 9101", "Atria Mall MY 1636",
        "Austria Buying 8894", "Austria Controlling 8882", "Austria Corporate 8891", "Austria Goods Receipts 8889", "Austria IT 9601", "Austria Marketing 8881", "Austria Picking 8888",
        "Austria Retail Projects 8886", "Aylesbury 0210", "Aylesbury HOF 2002", "B 3.OG", "B 6.OG", "Ballymena GA/BE 2331", "Bangor FIT 2640", "Barker Ross Admin Team 9918", "Barnsley FIT 2760",
        "Barnstaple RP 0702", "Barrow FIT 2642", "Basingstoke GA 2388", "Bath FL 2880", "Bath HOF 2003", "Bath HOF GA 2898", "Belfast Abbey GA 2391", "Belfast Boucher FIT 2753",
        "Belfast Connswatr GA 2392", "Belfast FL 2196", "Belfast GA 2390", "Belfast HOF 2004", "Best Connection Admin Team 9918", "Best Connection Day Shift 9910", "Best Connection Evening Shift 9911",
        "Best Connection Grimsby 9899", "Best Connection Night Shift 9912", "Best Connection Part time Days 9956", "Best Connection Web 9910", "Best Connection Web 9916", "Bicester 0004",
        "Birkenhead GA 2395", "Birm Solihull FL 1565", "Birmingham Fort Pk 2177", "Birmingham HOF 2006", "Birmingham HOF EV 2626", "Birmingham SPD GA BE 2830", "Blackburn FIT 2714", "Bletchley 0217",
        "Blue Arrow Admin Team 9919", "Blue Arrow Day Shift 9913", "Blue Arrow Web 9917", "Bluewater GA 2399", "Bluewater HOF 2007", "Boscombe GA 2403", "Bournemouth 0223", "Bournemouth HOF 2008",
        "Bracknell GA 2404", "Bradford Forster Sq 0152", "Bradford GA/BE 2405", "Braintree SPD GA BE 2831", "Brands Shared Service Centre 9003", "Brighton GA 2408", "Bristol Cribbs GA/BE 2409",
        "Bristol Filton FIT 2646", "Bristol Galleries GA 2410", "Bristol HOF 2009", "Bristol Imp FIT 2763", "Bromley GA 2411", "BSL Sports Directory 8938", "Budapest Arena HU 0469",
        "Bukit Bintang MY 1651", "Bukit Tinggi MY 1597", "Bullring GA 2412", "Burton On Trent FIT 2754", "Bury Rock GA 2416", "Bury St Edmunds FIT 1107", "Bury St Edmunds GA 2415",
        "Business Analytics & Integration 9203", "Buying 9000", "Buying Design 9032", "Caerphilly GA 2417", "Camberley HOF 2010", "Cambridge FIT 2650", "Canterbury FIT 2651", "Cardiff FIT 2652",
        "Cardiff HOF 2011", "Cardiff St Davids 0434", "Cardiff Tablot GA 2423", "Carlisle FIT 2755", "Carlisle GA 2424", "Carlisle HOF 2012", "Castleford JWO 2252", "Central I-City MY 1860", "Chatham GA 2427", "Check - Possible Error 99999", "Chelmsford EV 2077", "Chelmsford GA 2428", "Cheltenham 2 FIT 2653", "Cheltenham FIT 1109", "Cheltenham HOF 2013", "Cheshire Oaks GA 2429", "Cheshunt Brookfield 2787", "Chesterfield GA 2431", "Colchester FIT 1111", "Colchester SPD GA 2862", "Commercial Analytics 9040", "Commercial Design 9032", "Commercial Division 9000", "Commercial Division 9000", "Commercial Management 9030", "Commercial Planning 9031", "Commercial Projects 8945", "Commercial Projects Flannels 8946", "Commercial Projects HOF 8947", "Commercial Trading 9033", "Contractors 10001", "Contractors 9898", "Contractors 9898 (IT Infrastructure Data 9607)", "Copius 9965", "Corby GA 2436", "Corporate (Finance) 9450", "Coventry Precinct GA 2438", "Craigavon GA/BE 2440", "Croydon FIT 1112", "Croydon HOF 2017", "Cwmbran GA 2444", "Cwmbran HOF 2018", "Darlington HOF 2019", "Dataran Pahlawan MY 2203", "Denton Crown 1801", "Derby FIT 2655", "Derby FL 2980", "Derby GA 2446", "Derry FRA 2735", "Derry SPD GA BE 2959", "Dewsbury 0402", "Diamond Recruitment 9961", "Digital Department 9036", "Digital Risk 9177", "Directors & Dept Heads 9500", "Distribution 9700", "Distribution General 9701", "Doncaster GA 2448", "Doncaster HOF 2020", "Doncaster Wheatley 0162", "DoubleTake 8998", "Douglas SPD GA 2849", "Dudley Merryhill GA 2450", "Dunfermline GA 2453", "Dunstable EV 2695", "Dunstable FIT 2657", "Dunstable SPD GA 2906", "East Kilbride FIT 1534", "East Kilbride GA 2455", "Ecomm Operations 8763", "Ecomm User Experience 9240", "E-Commerce 9175", "E-Commerce Buying 9176", "E-Commerce London 8743", "Edinburgh Waverly GA 2461", "Elevation Programme 9044", "EMEA HR Department 9120", "Epsom FIT 1114", "Epsom HOF 2023", "Europe Administration 8810", "Europe Buying Department 8800", "Europe Contractors 8867", "Europe Distribution 8860", "Europe Finance Dept 8830", "Europe Human Resource Department 8820", "Europe Human Resource Dept 8820", "Europe Human Resourse Dept 8820", "Europe IT Dept 8855", "Europe Logistics 8859", "Europe Marketing 8806", "Europe Retail 8802", "Europe Retail Support 8805", "Evans B2B 9046", "Evans Commercial 9048", "Evans Customer Services 9054", "Evans HR 9045", "Evans Marketing 9050", "Evans Retail Support 9055", "Evans Warehouse 9052", "Evening Shift P/T/L 9833", "Ewell FIT 2658", "Exeter GA 2465", "External 10001", "F30 1.OG", "F30 1OG. Logistik", "F30 2.OG", "F30 EG", "F30 LOG 1.OG", "F30 LOG 2.OG", "Facilities", "Facilities 9859", "Finance 9400", "First Choice 9962", "Flannels", "Flannels Buying Department 8730", "Flannels Evening Warehouse 9823", "Flannels London Office 8734", "Flannels Marketing 8735", "Flannels Warehouse General 9821", "FLT Drivers - Night Shift F/T 9850", "Food & Beverage - Lion Hotel 9251", "Fork Lift Truck Drivers - Days 9817", "Fosse Park 0125", "Fosse Park GA/BE 2821", "Frasers Group Brand 9035", "Galleria SD AT 1022", "GAME BELONG 9088", "GAME Business Planning 9097", "GAME Business Support 9086", "GAME Commercial 9087", "GAME Customer Services 9076", "GAME DC Engineering 9071", "GAME DC Goods In 9072", "GAME DC Online 9073", "GAME DC Picks 9074", "GAME DC QA 9075", "GAME Directors 9093", "GAME eCommerce 9084", "GAME Finance 9081", "GAME Holding Department 9060", "GAME Insight 9092", "GAME Integration 9099", "GAME IT 9089", "GAME Marketing 9085", "GAME People 9095", "GAME Player1Events 9090", "GAME Property 9091", "GAME Retail Operations 9082", "GAME Supply Chain 9083", "GAME Trade Marketing 9096", "GAME Warehouse 9094", "General Warehouse - Flannels 9883", "Glasgow Easter FIT 2758", "Glasgow Fort EV 2174", "Glasgow Fort FIT 1746", "Glasgow Frasers 2025", "Glasgow GA/BE 2471", "Glasgow Silverburn 0767", "Glasgow St Enoch GA 2473", "Glenrothes GA 2475", "Gloucester FIT 2659", "Gloucester JWO 2272", "Graz EY MS AT 1054", "Grimsby WH", "Group HR Advisory 9301", "Group HR Business Partners 9302", "Guildford FIT 1117", "Guildford HOF 2027", "Guildford Ladymead 0234", "GUL International 9495", "Hadikgasse SE AT 1035", "Halifax FIT 2660", "Hanley GA 2482", "Head Office Security 9149", "Health & Safety 9325", "Heatons Buying 8979", "Heatons Finance 8983", "Heatons HR 8984", "Heatons IT Office", "Heatons Marketing 8987", "Heatons Merchandising", "Heatons Misc 8990", "Heatons Payroll", "Heatons Retail 8992", "Heatons Store Development 8944", "Heatons Warehouse 8991", "Heatons Warehouse Management 8996", "Hemel Hempstead GA 2487", "Hereford SPD GA 2861", "High Wycombe 0024", "High Wycombe HOF 2028", "HOF Buying 9235", "HOF Customer Services 9237", "HOF Loss Prevention 9246", "HOF Marketing 9247", "HOF Retail Support 9285", "Hohenems EY AT 1043", "Housekeeping - Lion Hotel 9252", "Hove FIT 1118", "Huddersfield HOF 2029", "Hull Ferensway 1569", "Hull Prospect GA/BE 2493", "Hull Southcoates FIT 2756", "Human Resources 9300", "Huntingdon FIT 1119", "IBML", "IBML Cavendish 9001", "IBML Hong Kong 9020", "IBML Shirebrook 9009", "Improvement Department 9602", "Intermark MY 1634", "Inverness FIT 2715", "IOI Puchong MY 2195", "Irvine GA 2499", "Isle of Wight GA 2500", "IT 8848", "IT 9600", "IT Delivery & Operations 9600", "IT Development Buying 9612", "IT Development ECommerce 9608", "IT Development Head Office 9610", "IT Development Retail 9611", "IT Development Warehouse 9609", "IT Helpdesk Shirebrook 9603", "IT InfoSec 9613", "IT Infrastructure Data 9607", "IT Infrastructure Networks 9605", "IT Infrastructure Systems 9606", "IT London 8745", "IT Workshop 9604", "Ixelles BE 0502", "Jack Wills Administration 9140", "Jack Wills Design 9145", "Jack Wills Garment Tech 9147", "Jarve SL EE 1161", "JW Sheffield Warehouse 9166", "Keighley FIT 1092", "Kettering FIT 1120", "Kings Heath FIT 1121", "Kings Lynn FIT 1122", "Kingston GA 2504", "Kingston U Thames 0294", "Klaipeda Akro AD LT 2158", "Krems SE AT 1033", "Kristiine SL EE 1172", "KSL Mall Johor MY 1631", "KSL Mall MY 1631", "Lakeside EV 2098", "Lakeside HOF 2032", "Lakeside SPD GA/BE 2506", "Large Property Projects Team 9201", "LDN Oxford Street FL 1796", "Leamington Spa HOF 2033", "Leeds Birstall FIT 2643", "Leeds Centre 1333", "Leeds Crownpoint 0418", "Leeds Headrow GA 2510", "Leeds Headrow SPD GA 2939", "Leeds HOF 2034", "Leeds JW 2283", "Leeds Station EV 2357", "Leeds White Rose GA 2509", "Leicester FIT 1747", "Leicester Flagshp FL 2711", "Leicester Gallowtree 1780", "Leicester SPD GA 2837", "Leigh FIT 2664", "Leisure Department 9190", "Liezen SD AT 1018", "Lincoln City FIT 1123", "Lincoln FIT 2665", "Lincoln GA 2513", "Lincoln HOF 2036", "Lindir IS 0560", "Linear Admin 9868", "Linear Agency Sheffield DC 9909", "Linear Day Shift 9872", "Linear Evening Shift 9867", "Linear Night Shift 9866", "Linear Part Time Days 9869", "Linz EY MS AT 1046", "Linz LW AT 1046", "Lion Hotel 9250", "Liverpool FIT 1125", "Liverpool GA 2942", "Livingston GA 2516", "Llanelli FIT 2663", "Llantrisant 0243", "Loch Lomond HOF 2037", "London Ox HOF GA BE 2870", "Londonderry FIT 2717", "Loss Prevention Department 9125", "Lovells General Recharge 9275", "Macclesfield FIT 2667", "Maidenhead 0017", "Maidstone GA 2523", "Maidstone HOF 2038", "Mailroom", "Mailroom Belgium", "Maintenance & Waste Team 9819", "Malaysia Administration 8948", "Malaysia Buying 8921", "Malaysia Design and Creative 8922", "Malaysia Directors 8923", "Malaysia Ecommerce 8924", "Malaysia Finance 8926", "Malaysia HR 8927", "Malaysia Inventory 8928", "Malaysia IT 8939", "Malaysia Learning and Development 8929", "Malaysia Marketing 8921", "Malaysia Marketing 8931", "Malaysia Projects 8933", "Malaysia Retail Operations 8934", "Malaysia Retail Support 8935", "Malaysia Visual Merchandising 8936", "Malaysia Warehouse 8937", "Manchester Denton GA 2525", "Manchester HOF 2039", "Manchester TRA GA/BE 2527", "Manchestr Arndale GA 2524", "Mariahilfer EY MS AT 1052", "Marketing Department 9106", "Meadowhall GA 2565", "Meadowhall Gallery 1769", "Megasport 8862", "Merchandising 9113", "Merthyr DW 2701", "Merthyr FL 2789", "Merthyr Tydfil DW GA 2951", "Merthyr Tydfil FIT 2668", "Metro Centre HOF 2041", "Metro GA 2949", "Mid Valley MY 1640", "Milngavie FIT 1128", "Milton Keynes 0130", "Milton Keynes GA/BE 2531", "Milton Keynes JW 2291", "Morecambe GA 2533", "New Cavendish Street", "Newark FIT 1129", "Newcastle FIT 2649", "Newcastle FL 1841", "Newport Measglas FIT 2670", "Newry Centre 2172", "Newry SPD GA BE 2829", "Nexus Day Shift 9913", "Nexus Part time Days 9957", "Nexus PT Eve 9973", "Nexus Sheffield DC 9924", "Non Executive Directors 9501", "Northfield FIT 1130", "Norwich HOF 2045", "Norwich HOF GA 2917", "Nottingham EV 2114", "Nottingham FIT 2671", "Nottingham FL 0786", "Nottingham HOF 2044", "Nottingham Vic GA 2545", "Oceanus Mall MY 1637", "Operational Analytics 8747", "Operational Finance 9412", "Operations London 8742", "Origo SL LV 1165", "Oxford Street 0666", "Oxford Street HOF 2046", "Paphos Polis Road CY 0594", "Part time Night Shift 11pm to 4am 9841", "Payroll 9350", "People 9122", "Perth GA 2547", "Peterborough GA 2548", "Photographers 9111", "Piccadilly LW 0602", "Please speak to tdooley before removing Member Of groups", "Plymouth Drake GA 2551", "Plymouth HOF 2047", "Plymouth SPD GA BE 2977", "Poole FIT 2672", "Portsmouth SPD GA BE 2851", "PR 9131", "Preston GA/BE 2554", "Pricing - part time 9824", "Projects Department 9104", "Property 9200", "Property London 9201", "Property Shirebrook 9200", "Property Utilities Dept 9204", "Psyche 9070", "Purchase Ledger 9401", "Reading HOF 2048", "Reading Oracle GA 2556", "Reception & Administration - Lion Hotel 9256", "Recruitment Department 9105", "Redditch GA 2557", "Retail Insight 8746", "Retail Projects Contractors 9114", "Retail Support 9100", "Rhyl GA 2559", "Romford GA 2561", "Rushden Lakes FRA 2035", "Saintes", "Sale FIT 1133", "Salisbury FIT 1134", "Schmiede LU 0538", "Scunthorpe SPD GA/BE 2337", "SDIL - Europe Distribution Center - HO 8866", "SDIL - Europe Distribution Center - Warehouse 8860", "SDIL - Mailroom", "Section Leaders - Day Shift 9825", "Section Leaders - Evening Shift 9838", "Section Leaders - Night Shift 9857", "Security Guards 9109", "See Keepass for Password", "Selby FIT 2673", "Sheffield EV 2118", "Sheffield Flagshp FL 2894", "Sheffield Warehouse Day Shift 9808", "Sheffield Warehouse Evening Shift 9807", "Sheffield Warehouse Night Shift 9809", "Shirebrook", "Shirebrook 0292", "Shirebrook BM 1364", "Shirebrook EV 2175", "Shirebrook FIT 1745", "Shirebrook FL 1736", "Shirebrook GAME Customer Services 9127", "Single Resource Day Shift 9875", "Single Resource Evening Shift 9876", "Single Resource Grimsby 9899", "Single Resource Night Admin 9874", "Single Resource Night Shift 9873", "Single Resource Part Time Days 9877", "Slough 0006", "Slough Bath Road 0316", "Smith and Brooks 9008", "Sofa.com Human Resources 9213", "Sofa.com Recharges 8825", "Solihull HOF 2052", "Southampton FL 2780", "Southend GA 2571", "Southport EFC 1543", "Southport FIT 2675", "Sportland Accounts 8845", "Sportland Administration 8846", "Sportland Buying 8851", "Sportland HR 8847", "Sportland Marketing 8849", "Sportland Retail 8850", "Sportland Warehouse 8852", "Sports Direct Asia", "Sports Direct.com", "Sportsland IT 8848", "St Austell SPD GA 2940", "St Helens 0317", "St Helens FIT 1093", "St Pauls EV 2120", "St Polten Eybl EY AT 1029", "Staff Development & Training Department 9107", "Staffing Match Night Shift 9873", "StHelen Milverny FIT 2676", "Stockport Courts 0101", "Stratford GA 2581", "Stratford Westfield 0094", "Subang Jaya MY 1594", "Sunderland FIT 2677", "Sunderland SPD GA 2847", "Sunway Putra Mall MY 1635", "Sunway Pyramid MY 2627", "Sunway Velocity MY 1593", "Supervisory 9818", "Supervisory 9828", "Supervisory 9858", "Supplier Compliance - MBX Owner Rachel Stockton", "Sustainability 9397", "Sutton BM 2931", "Sutton Coldfield GA 2584", "Sutton Coldfield HOF 2053", "Sutton GA 2826", "Sutton GA BE 2326", "Swansea SPD GA 2864", "Swindon 0107", "Swindon FIT 2678", "Tabletennispro Grimsby 9475", "Tall.Kristiine SD EE 1547", "Technical Services 9130", "Teeside SPD GA 2954", "Telford HOF 2055", "Thurrock FIT 1740", "Thurrock Junction 1738", "Torquay GA 2591", "Transline Admin Team 9919", "Transline Day Shift 9913", "Transline Evening Shift 9914", "Transline Night Shift 9915", "Transline Web 9917", "Transline Weekend 9917", "Tropicana Gardens MY 2161", "TTPro 9454", "Tunstall FIT 2680", "Udini Mall MY 1638", "Ulemiste Centr SD EE 1256", "Ulemiste SL EE 1169", "Unique Catering 9925", "Universal Cycles 9011", "USC Buying 9465", "USC Marketing 9463", "Victoria HOF 2056", "Vienna North EYMS AT 1053", "Visual Projects Flannels 8941", "Visual Projects HOF 8942", "Visual Projects JW 8944", "Visual Projects USC 8943", "Vivacity Kuching MY 1641", "Vocklabruck SD AT 1026", "Vosendorf EY WS AT 1051", "Wakefield GA 2594", "Warehouse (General) 9800", "Warehouse Administration 9826", "Warehouse Automation 9602", "Warehouse Improvement 9614", "Warehouse Long Term Sickness 9806", "Warehouse Training Department 9815", "Watford FL 1837", "Watford High Street 1661", "Watford JW 2318", "Wels Eybl EY MS AT 1045", "West End EV 2124", "West Thurrock GA 2604", "Westfield HOF 2057", "Westwood Cross GA 2606", "WHO's - Day Shift F/T 9820", "WHO's - Evening Shift F/T 9830", "WHO's - Night Shift F/T 9840", "Witney GA 2612", "Wolverhampton FRA 2624", "Wolverhampton SPD GA 2832", "Worcester HOF 2059", "Worgl SD AT 1014", "Worthing GA 2618", "Wrexham FIT 2681", "Wrexham SPD GA BE 2825", "Yard Shunters 9703", "Yeovil TRI 1768", "York FL 2135", "York GA/BE 2621", "Zaragoza ES 0485"]
var1 = StringVar()
dropdowndeps = ttk.Combobox(root, textvariable=var1)
dropdowndeps['values'] = deps
dropdowndeps.current(0)
dropdowndeps['state'] = 'readonly'
c.create_window(260, 248, window=dropdowndeps)


# output filter box
c.create_rectangle(10, 305, 380, 460, fill='white',
                   outline='Light Grey', width=2)

# output filter header
outhead = tkinter.Label(text="Extra Outputs", bg="White")
c.create_window(65, 303, window=outhead)



# info box
c.create_rectangle(10, 480, 380, 640, fill='white',
                   outline='Light Grey', width=2)

# info header
drophea = tkinter.Label(text="Info", bg="White")
c.create_window(41, 479, window=drophea)


# info header
Info = 'Hi 👋 here’s some basic info to help you better understand Gary. The search button has two functions. If the username textbox contains any characters Gary will search for the specific user ignoring any filters but still export the “Extra Outputs” If the username box is empty Gary will get all users within the specified filters. Gary will not work if the machine does not have access to the sportski.com AD Server. For any bugs or suggestions please message “Huseyin Ucur” '
drophea = tkinter.Label(text=Info, bg="White", justify=LEFT,  wraplength=340)
c.create_window(193, 560, window=drophea)

def searchbut():
    print("updated mouse")
    root.config(cursor="wait")

    print("updating root")
    root.after(200, look)
    print("search function")


# button find user by date range
runb = tkinter.Button(text="Search ", command=searchbut,
                      bd="0", bg="Light Grey", height=3, width=53)
c.create_window(579, 614, window=runb)

# button to dubplicate temp file to preferd location and name
export = tkinter.Button(text="Export to CSV", command=saveas,
                        bd="0", bg="Light Grey", height=3, width=30)
c.create_window(885, 614, window=export)

# get user


def getuser():
    name = getIn()
    loc = settemp()
    loc = loc.replace('"', "")
    name = name.replace('"', "")
    print("---------------------------------------")
   #print(name, loc)

    filters = getexports() 
    filters = filters 
    filterstring = ','.join(filters)  
 
    if len(filters) >= 1:
        command = 'Get-ADUser -Identity %s -Properties %s,DisplayName,sAMAccountName | select %s,DisplayName,sAMAccountName | Export-CSV -path %s ' %(name, filterstring, filterstring, loc)
    else:
        command = 'Get-ADUser -Identity %s -Properties DisplayName,sAMAccountName | select DisplayName,sAMAccountName | Export-CSV -path %s ' %(name, loc)  

    print(command)
    out = run(command)
    out = str(out)
    error = " Cannot find an object with identity"
    if error in out:
        tkinter.messagebox.showwarning(title="Error", message="No User Found")
    else:
        updatetree(loc, 2)




def upmo(self):
    print("updated mouse")
    root.config(cursor="wait")
    print('Formatting input box')
    namein.delete('end-1c', 'end')
    print("updating root")
    root.after(500, look)
    print("search function")


def look():
    searchfun()
    


root.bind('<Return>', upmo)

root.config(cursor="")

c.pack()
root.mainloop()

