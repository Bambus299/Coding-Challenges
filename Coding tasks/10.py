


def kosinus_annaeherung(grad):
    rad = grad * 3.14159265 / 180.0
    x2 = rad * rad
    return 1.0 - x2 / 2.0 + (x2 * x2) / 24.0

def geo_distanz(p1, p2):
    mittlere_breite = (p1[0] + p2[0]) / 2.0
    d_lat = p1[0] - p2[0]
    d_lon = p1[1] - p2[1]
    
    korrigierter_lon = d_lon * kosinus_annaeherung(mittlere_breite)
    return d_lat**2 + korrigierter_lon**2

def finde_kuerzeste_route(start_koordinaten, ziel_liste):
    aktuelle_pos = start_koordinaten
    nicht_besucht = ziel_liste.copy()
    route = []
    
    while nicht_besucht:
        naechstes = min(nicht_besucht, key=lambda z: geo_distanz(aktuelle_pos, z['latlon']))
        route.append(naechstes['id'])
        
        aktuelle_pos = naechstes['latlon']
        nicht_besucht.remove(naechstes)
        
    return route

start = (78.000000, -40.750000)
destinations = [
    {"id": "01", "latlon": (47.000000, 8.500000)},
    {"id": "02", "latlon": (64.000000, 17.000000)},
    {"id": "03", "latlon": (37.500000, 14.100000)}
]

print("Berechnete Route:", finde_kuerzeste_route(start, destinations))
