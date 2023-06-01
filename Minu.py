import random

def juhuslikaeg(vahemik_min, vahemik_max):
    aeg = random.randint(vahemik_min, vahemik_max) + random.random()
    return round(aeg, 3)

def vorminda_ajavormingusse(aeg):
    tundide_arv = int(aeg / 3600)
    minutite_arv = int((aeg % 3600) / 60)
    sekundite_arv = int(aeg % 60)
    millisekundid = int((aeg % 1) * 1000)
    ajavorming = '{:02d}:{:02d}:{:02d}.{:03d}'.format(tundide_arv, minutite_arv, sekundite_arv, millisekundid)
    return ajavorming

def valjasta_tulemused(ringiajad, kokkuaeg):
    print("Võistlus tulemused:")
    for osaleja in kokkuaeg:
        print(f"{osaleja[0]} - {vorminda_ajavormingusse(osaleja[1])}")
    print()
    print("Iga sõitja ringiajad:")
    for raja_aeg in ringiajad:
        print(f"{raja_aeg[0]} - {vorminda_ajavormingusse(raja_aeg[1])}")

def voistlus():
    osalejad = ['Kati', 'Mari', 'Joss', 'Karl', 'Luke']
    ringide_arv = 10
    ringiajad = []
    kokkuaeg = []