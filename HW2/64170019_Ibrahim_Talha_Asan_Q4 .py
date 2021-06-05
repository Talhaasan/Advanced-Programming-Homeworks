class HashTable:

    def __init__(self):
        self.size =11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.hashValues = 49 # 49 is hash table total element number and I can not reach this number from given code.
                             #So, I manually give 49 value then I applied the requested operations.      
        

    def put(self,key,data):
     
      if self.size < self.hashValues:
           self.size = self.size * 5
           self.slots = [None] * self.size
           self.data = [None] * self.size
      else:
           self.size = self.size
           
      hashvalue = self.hashfunction(key,len(self.slots))
     
      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace
        

    def hashfunction(self,key,size):
        return hash(key)%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))
      data = None
      stop = False
      found = False
      position = startslot 
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)
    

H = HashTable()
H['Abondon']='TERK ETMEK'
H['Ability']='YETENEK'
H['Able']='MUKTEDIR'
H['Aboard']='(bir tasitin) ICINDE OLMAK'
H['About']='1.HAKKINDA 2.YAKLASIK OLARAK'
H['Above']='YUKARIDAKI'
H['Abroad']='YURTDISI'
H['Absence']='YOKLUK'
H['Absent']='1.YOK 2.EKSIK'
H['Absolute']='MUTLAK,KESIN'
H['Absurd']='SACMA'
H['Accept']='KABUL ETMEK'
H['Accident']='KAZA'
H['Accommodate']='YERLESTIRMEK'
H['Accommodation']='KONAKLAMA YERI'
H['Accompany']='ESLIK ETMEK'
H['According To']='GORE'
H['Account']='HESAP'
H['Accurate']='DOGRU,HATASIZ'
H['Accuse']='SUCLAMAK'
H['Ache']='AGRI'
H['Acquaint']='TANIMAK,BILMEK'
H['Across']='1.BIR UCTAN DIGERINE 2.DIGER TARAFTA'
H['Act']='1.DAVRANIS,2.DAVRANMAK'
H['Active']='ETKIN,FAAL'
H['Actor']='ERKEK OYUNCU'
H['Actress']='KADIN OYUNCU'
H['Actual']='GERCEK'
H['Add']='TOPLAMAK,EKLEMEK'
H['Address']='ADRES'
H['Administration']='IDARE'
H['Admire']='BEGENMEK,HAYRAN OLMAK'
H['Admit']='1.KABUL ETMEK 2.IZIN VERMEK'
H['Adult']='YETISKIN'
H['Advance']='1.ILERI 2.AVANS'
H['Advanced']='GELISMIS'
H['Advantage']='AVANTAJ'
H['Adventure']='MACERA'
H['Advertise']='REKLAM YAPMAK,ILAN VERMEK'
H['Advice']='TAVSIYE'
H['Advise']='TAVSIYE ETMEK'
H['Aerial']='ANTEN'
H['Aeroplane']='UCAK'
H['Affair']='1.OLAY 2.IS 3.ILISKI'
H['Affect']='ETKILENMEK'
H['Afford']='SATIN ALMA GUCU OLMAK'
H['Afraid']='KORKMAK'
H['After']='SONRA'

print(H.slots)
print(H.data)


