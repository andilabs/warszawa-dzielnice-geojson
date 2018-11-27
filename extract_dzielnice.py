import geojson

city_districts = None
with open('warszawa-dzielnice.geojson', 'r') as F:
    city_districts = geojson.loads(F.read())

for district in city_districts.features:
    district_name = district.properties.get('name').lower()
    with open(u'{}.geojson'.format(district_name), 'w') as WF:
        WF.write(geojson.dumps(district.geometry))
