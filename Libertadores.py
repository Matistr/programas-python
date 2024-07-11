libertadores = ["u de chile", "nacional", "boca", "palmeiras"]

for lib1 in libertadores:
    for lib2 in libertadores:
        if lib1 != lib2:
            print(f"Partido de {lib1} vs {lib2}")