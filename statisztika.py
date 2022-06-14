# 1. A karakterek_szama(text)       függvény visszatér a karakterek számával. ('\n karakterekkel eggyütt')
# 2. A szavak_szama(text)           függvény visszatér a szavak számával.
# 3. A sorok_szama(text)            függvény visszatér a sorok számával.
# 4. Az e_betuk_szama(text)         függvény visszatér a 'e' betük számával.
# 5. A lorem_szavak_szama(text)     függvény visszatér a "lorem" szavak számával.
# 6. A legritkabb_karakter(text)    függvény visszatér a legritkábban előforduló karakterrel.
# 7. A leghosszabb_sor_hossza(text) függvény visszatér a leghosszabb sor hosszával.

# 1
def karakterek_szama(txt):
    sorok = txt.split("\n")
    ossz = len(sorok) + len(txt) 
    return ossz
# 2
def szavak_szama(txt):
    szavak = txt.split()
    return len(szavak)
# 3        
def sorok_szama(txt):
   sorok = txt.split("\n")
   return len(sorok)
# 4
def e_betuk_szama(txt):
  szamlalo = 0
  for betu in txt:
    if betu == "e":
      szamlalo = szamlalo + 1
  return szamlalo
        
# 5
def lorem_szavak_szama(txt):
  szamlalo = 0
  szavak = txt.split(" ")
  for betu in szavak:
    if "lorem" in betu:
      szamlalo = szamlalo + 1
  return szamlalo

# 6
def legritkabb_karakter(txt):
    stat = dict()
    for betu in txt:
      betu = betu
      stat[betu] = stat.get(betu, 0) + 1
    return min([(db, betu) for betu, db in stat.items()])[1]

      
# 7
def leghosszabb_sor_hossza(txt):
    sorok = txt.split("\n")
    leg_nagyobb =  max(sorok)
    return len(leg_nagyobb)












