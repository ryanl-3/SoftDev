from random import randint

krewes1 = {1:["1", "2", "3"], 2:["A", "B", "C"]}
krewes2 = {
    2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"],
    7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
    8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
}
krewes3 = {}
krewes4 = {1:["1"], 2:[]}
krewes5 = {1:[], 2:[]}

file = open("krewes.txt")
text = file.read()

pd = []
devo = []
ducky = []

diction = {}

def categorize(s):
    individual = s.split("@@@")
    for e in individual:
        t = e.split("$$$")
        pd.append(t[0])
        devo.append(t[1])
        ducky.append(t[2])
    for p in range(0, len(pd)):
        exists = False
        l = [devo[p] + " " + ducky[p]]
        for k in diction.keys():
            if pd[p] == k:
                diction[pd[p]] = diction[pd[p]] + l
                exists = True
        if not exists:
            diction[pd[p]] = l
    return None


def getRandom(dictionary):
    
    if len(dictionary) == 0:
        return "ERROR: Dictionary has no values"  	 
    key = []
    for e in dictionary.keys(): #gets all the keys
        key.append(e)
    while True:
        if len(key) == 0:
            return "ERROR: all lists empty"
        period = key[randint(0, len(key)-1)]  #chooses a random key
        if len(dictionary.get(period)) == 0:
            key.remove(period)
        else:
            r = randint(0, len(dictionary.get(period))-1) #chooses random index of the list associated with the random key
            k = dictionary.get(period)  #gets the list associated with the random key
            break
    return k[r] #returns value at random index of random lis
categorize(text)
print(diction)
print(getRandom(diction))
