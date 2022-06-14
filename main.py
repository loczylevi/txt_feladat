"""
Figyelem!
Ne módosítsd ezt a fájlt.
a statisztika.py -ban dolgozz.
"""


from statisztika import *

txt = """Lorem ipsum dolor sit amet consectetur adipisicing elit.
Quaerat porro voluptates deserunt, totam eius fuga autem doloremque, molestias ex cum iusto? Consequatur quisquam delectus nam assumenda nemo veritatis ea, minima sunt? Commodi cumque rerum deleniti nam iusto quasi?
Non perspiciatis amet nisi! Ea unde libero dolorum beatae soluta, atque saepe exercitationem nostrum numquam, quam quibusdam adipisci esse labore quas nisi quaerat ab quasi, accusantium reprehenderit rem nulla temporibus?
Cupiditate atque reprehenderit dolore praesentium beatae ex aut minus dolorem sunt rem aperiam exercitationem magni ducimus corporis laudantium, debitis non nam consequuntur doloremque eaque ut molestiae? Nulla, corrupti sequi? Molestias!
Illo cumque minima autem mollitia! Quia dignissimos et accusamus corporis amet, cum quidem, ea, voluptates officiis adipisci beatae deserunt officia neque. Dolor consequatur cum corrupti nemo, quis magni expedita velit?"""
f1 = karakterek_szama(txt)
f2 = szavak_szama(txt)
f3 = sorok_szama(txt)
f4 = e_betuk_szama(txt)
f5 = lorem_szavak_szama(txt)
f6 = legritkabb_karakter(txt)
f7 = leghosszabb_sor_hossza(txt)

print(
f'''
1. A karakterek száma: {f1}
2. A szavak száma: {f2}
3. A sorok száma: {f3}
4. Az "r" betük száma: {f4} 
5. A "lorem" szavak száma: {f5}
6. A legritkább karakter: {f6} 
7. A leghosszabb sor hossza: {f7} 
    
''')
