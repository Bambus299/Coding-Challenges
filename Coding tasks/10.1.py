import req
import post

start_data = req.get_data("10")
print(start_data)


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

def löse_rätsel_10(api_daten):
    if isinstance(api_daten['start'], str):
        start = tuple(map(float, api_daten['start'].split(',')))
    else:
        start = api_daten['start']
        
    ziel_liste = []
    for d in api_daten['destinations']:
        if isinstance(d['latLon'], str):
            latlon = tuple(map(float, d['latLon'].split(',')))
        else:
            latlon = d['latLon']
            
        ziel_liste.append({"id": d['id'], "latLon": latlon})
        
    aktuelle_pos = start
    nicht_besucht = ziel_liste.copy()
    route = []
    
    while nicht_besucht:
        naechstes = min(nicht_besucht, key=lambda z: geo_distanz(aktuelle_pos, z['latLon']))
        route.append(naechstes['id'])
        aktuelle_pos = naechstes['latLon']
        nicht_besucht.remove(naechstes)
        
    return {"route": route}

solution = löse_rätsel_10(start_data)
print(solution)

answer = post.post_data("10" , solution)
print(answer)
