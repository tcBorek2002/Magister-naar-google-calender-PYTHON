from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
global website
global inlogid
global jaar
global wachtwoordid
global naamschool
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


##############################################
# __          __  _ _                        #
# \ \        / / | | |                       #
#  \ \  /\  / /__| | | _____  _ __ ___       #
#   \ \/  \/ / _ \ | |/ / _ \| '_ ` _ \      #
#    \  /\  /  __/ |   < (_) | | | | | |     #
#     \/  \/ \___|_|_|\_\___/|_| |_| |_|     #
#                                            #   
#####                Uitleg:        ##########
#1: Vul de variabelen hieronder in, in het stukje tussen de ""
#Bijvoorbeeld: inlogid = "[VUL DIT IN]"
#2: Sla het bestand op,
#3: Voer het bestand uit!
#
#Variabelen:
#De website die direct naar de agendapagina van je magister gaat:
#(Verkijg die link door hem te kopieren. 1:Ga naar magister. 2:Log In 3: Ga naar je agenda. 4: Kopieer de link):
website = "https://zandvliet.magister.net/magister/#/agenda"
#De gebruikersnaam waarme je inlogt:
inlogid = "gebruikersnaam"
#Het wachtwoord waarme je inlogt:
wachtwoordid = "wachtwoord"
#De naam van de locatie die in google komt: (bv: naam school)
naamschool = "schoolnaam"
#Het huidige jaar:
jaar = "2019"
#Hieronder moet je de tijdstippen van alle lessen aangeven:
#(Let er hierbij wel op dat alle tijdstippen met één getal, met twee getallen moet worden gegeven:
#BV: 8 uur --> 08:00)
#Eerste les begintijdstip:
btijd1 = "08:10"
#Eerste les eindtijdstip:
etijd1 = "09:00"
#Dit gaat hieronder verder tot het achtste lesuur:
btijd2="09:00"
etijd2="09:50"
#
btijd3="09:50"
etijd3="10:40"
#
btijd4="11:10"
etijd4="12:00"
#
btijd5="12:00"
etijd5="12:50"
#
btijd6="13:15"
etijd6="14:05"
#
btijd7="14:05"
etijd7="14:55"
#
btijd8="14:55"
etijd8="15:45"
#
#Dit zijn alle variabelen. Voer nu het programma uit!
#
#
#
#
#
#Github: https://github.com/tcBorek2002/Magister-naar-google-calender-PYTHON
#©Borek Bandell 2019

def dagverkrijgen():
    global monthletter
    global dag
    global jaartal
    global datumg
    datetransfer = datumtekst.split()
    dag = datetransfer[1]
    maand = datetransfer[2]
    jaartal = jaar
    if(maand == "januari"):
        monthletter = "1"

    elif(maand == "februari"):
        monthletter = "2"

    elif(maand == "maart"):
        monthletter = "3"

    elif(maand == "april"):
        monthletter = "4"

    elif(maand == "mei"):
        monthletter = "5"

    elif(maand == "juni"):
        monthletter = "6"

    elif(maand == "juli"):
        monthletter = "7"

    elif(maand == "augustus"):
        monthletter = "8"

    elif(maand == "september"):
        monthletter = "9"

    elif(maand == "oktober"):
        monthletter = "10"

    elif(maand == "november"):
        monthletter = "11"

    elif(maand == "december"):
        monthletter = "12"
    
    jaartalg = str(jaartal)
    monthletterg = str(monthletter)
    dagg = str(dag)
    #Hoe de datum in google komt:
    datumg = jaartalg+"-"+monthletterg+"-"+dagg

def lesachtg():
    tijdstip = uurachttekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    beginacht = datumg+"T"+btijd+":00+01:00"
    eindacht= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurachttekst+ " - " + lesachttekst,
      'location': naamschool,
      'description': '',
      'start': {
        'dateTime': beginacht,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindacht,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ lesviertekst) 

def lesacht():
    global lesachttekst
    global uurachttekst
    try:
        #achtste les
        lesacht = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[9]/td[3]/span/span[2]")
        lesachttekst = lesacht.text
        uuracht = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[9]/td[3]/span/span[1]")
        uurachttekst = uuracht.text
        lokaalacht = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[9]/td[3]/span/span[3]")
        print("Achtste les: "+uurachttekst+" - "+ lesachttekst + " " + lokaalacht.text)
        print("Dit zijn alle lessen voor vandaag")
        lesacht()
    except :
        print("Dit zijn alle lessen voor vandaag")

def leszeveng():
    tijdstip = uurzeventekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    beginzeven = datumg+"T"+btijd+":00+01:00"
    eindzeven= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurzeventekst+ " - " + leszeventekst,
      'location': naamschool,
      'description': '',
      'start': {
        'dateTime': beginzeven,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindzeven,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ leszeventekst)     

def leszeven():
    global leszeventekst
    global uurzeventekst
    try:
        #zevende les
        leszeven = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[8]/td[3]/span/span[2]")
        leszeventekst = leszeven.text
        uurzeven = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[8]/td[3]/span/span[1]")
        uurzeventekst = uurzeven.text
        lokaalzeven = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[8]/td[3]/span/span[3]")
        print("Zevende les: "+ uurzeventekst + " - "+ leszeventekst + " " + lokaalzeven.text)
        leszeveng()
        lesacht()
    except :
        print("Dit zijn alle lessen voor vandaag")
    
def leszesg():
    tijdstip = uurzestekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    beginzes = datumg+"T"+btijd+":00+01:00"
    eindzes= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurzestekst+ " - " + leszestekst,
      'location': naamschool,
      'description': '',
      'start': {
        'dateTime': beginzes,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindzes,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ leszestekst) 

def leszes():
    global leszestekst
    global uurzestekst
    try:
        #zesde les
        leszes = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[7]/td[3]/span/span[2]")
        leszestekst = leszes.text
        uurzes = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[7]/td[3]/span/span[1]")
        uurzestekst = uurzes.text
        lokaalzes = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[7]/td[3]/span/span[3]")
        print("Zesde les:   "+ uurzestekst +" - "+ leszestekst+ " " + lokaalzes.text)
        leszesg()
        leszeven()
    except :
        print("Dit zijn alle lessen voor vandaag")

def lesvijfg():
    tijdstip = uurvijftekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    beginvijf = datumg+"T"+btijd+":00+01:00"
    eindvijf= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurvijftekst+ " - " + lesvijftekst,
      'location': naamschool,
      'description': '',
      'start': {
        'dateTime': beginvijf,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindvijf,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ lesvijftekst)     

def lesvijf():
    global lesvijftekst
    global uurvijftekst
    try:
        #vijfde les
        lesvijf = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[6]/td[3]/span/span[2]")
        lesvijftekst = lesvijf.text
        uurvijf = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[6]/td[3]/span/span[1]")
        uurvijftekst = uurvijf.text
        lokaalvijf = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[6]/td[3]/span/span[3]")
        print("Vijfde les:  "+ uurvijftekst + " - "+ lesvijftekst +" "+ lokaalvijf.text)
        lesvijfg()
        leszes()
    except :
        print("Dit zijn alle lessen voor vandaag")
        
def lesvierg():
    tijdstip = uurviertekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    beginvier = datumg+"T"+btijd+":00+01:00"
    eindvier= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurviertekst+ " - " + lesviertekst,
      'location': naamschool,
      'description': '',
      'start': {
        'dateTime': beginvier,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindvier,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ lesviertekst)    

def lesvier():
    global lesviertekst
    global uurviertekst
    try:
        #vierde les
        lesvier = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[5]/td[3]/span/span[2]")
        lesviertekst = lesvier.text
        uurvier = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[5]/td[3]/span/span[1]")
        uurviertekst = uurvier.text
        lokaalvier = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[5]/td[3]/span/span[3]")
        print("Vierde les:  "+uurviertekst +" - "+ lesviertekst + " "+ lokaalvier.text)
        lesvierg()
        lesvijf()
    except :
        print("Dit zijn alle lessen voor vandaag")

def lesdrieg():
    tijdstip = uurdrietekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    begindrie = datumg+"T"+btijd+":00+01:00"
    einddrie= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurdrietekst+ " - " + lesdrietekst,
      'location': naamschool,
      'description': '',
      'start': {
        'dateTime': begindrie,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': einddrie,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ lesdrietekst)



def lesdrie():
    global lesdrietekst
    global uurdrietekst
    try:
        #derde les
        lesdrie = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[4]/td[3]/span/span[2]")
        lesdrietekst = lesdrie.text
        uurdrie = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[4]/td[3]/span/span[1]")
        uurdrietekst = uurdrie.text
        lokaaldrie = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[4]/td[3]/span/span[3]")
        print("Derde  les:  "+uurdrietekst+ " - " +lesdrietekst + " "+ lokaaldrie.text)
        lesdrieg()
        lesvier()
    except :
        print("Dit zijn alle lessen voor vandaag")

def lestweeg():
    global maand
    tijdstip = uurtweetekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    begintwee = datumg+"T"+btijd+":00+01:00"
    eindtwee = datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurtweetekst+ " - " + lestweetekst,
      'location': naamschool,
      'description': '',
      'start': {
        'dateTime': begintwee,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindtwee,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ lestweetekst)


def lestwee():
    #tweede les
    global uurtweetekst
    global lestweetekst
    lestwee = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[3]/td[3]/span/span[2]")
    lestweetekst = lestwee.text
    uurtwee = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[3]/td[3]/span/span[1]")
    uurtweetekst = uurtwee.text
    lokaaltwee = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[3]/td[3]/span/span[3]")
    print("Tweede les:  "+ uurtweetekst +" - "+ lestweetekst + " " + lokaaltwee.text)
    lestweeg()
    lesdrie()



def leseeng():
    global maand
    dagverkrijgen()
    tijdstip = uureentekst
    #default begin: '2019-02-26T06:00:00+01:00'
    #default eind:  '2019-02-26T07:00:00+01:00'
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    
    begineen = datumg+"T"+btijd+":00+01:00"
    eindeen = datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uureentekst+ " - " + leseentekst,
      'location': naamschool,
      'description': '',
      'start': {
        'dateTime': begineen,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindeen,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ leseentekst)

def leseen():
    global uureentekst
    global leseentekst
    #eerste les
    leseen = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[2]/td[3]/span/span[2]")
    leseentekst = leseen.text
    uureen = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[2]/td[3]/span/span[1]")
    uureentekst = uureen.text
    lokaaleen = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[2]/td[3]/span/span[3]")
    hween = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[3]/td[4]/span")
    print("Eerste les:  "+ uureentekst+ " - " + leseentekst +" " + lokaaleen.text)
    leseeng()
    lestwee()


def datum():
    global datumtekst
    #De datum verkrijgen
    datum = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[1]/td/p/span/strong")
    datumtekst = datum.text
    print("          "+datumtekst)
    leseen()


def verzamelen():
    #tijd om rooster te laden
    #default tijd = 4
    time.sleep(9)
    print("Datum en lessen inladen...")
    datum()
    
def inloggen():
    id_box = driver.find_element_by_id("username")
    id_box.send_keys(inlogid)
    #vult gebruikersnaam in
    print("Op doorgaan drukken")
    time.sleep(.3)
    enterknop = driver.find_element_by_id("username_submit")
    enterknop.click()
    #klikt op doorgaan knop
    print("Wachtwoord invoeren...")
    time.sleep(.3)
    ww_box = driver.find_element_by_id("password")
    ww_box.send_keys(wachtwoordid)
    #vult wachtwoord in
    time.sleep(.3)
    print("Weer op doorgaan drukken...")
    enterknop2 = driver.find_element_by_id("password_submit")
    enterknop2.click()
    print("Rooster wordt geladen...")
    #druk op doorgaan
    verzamelen()

def openmagister():
    global driver
    driver = webdriver.Chrome()
    driver.get(website)
    #open chrome in magister
    print("Website wordt geladen...")
    time.sleep(2)
    #website tijd geven om te laden, anders is de code te snel en komer er errors
    print("Leerlingnummer invullen...")
    inloggen()
    


def gstarten():
    global creds
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    


gstarten()
openmagister()
