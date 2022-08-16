import re

import requests
from bs4 import BeautifulSoup


def activity(q):
    """dossier should be a JSON"""
    data_sources = ['https://nominatim.openstreetmap.org/ui/search.html?q=nevada+state+railroad+museum+carson+city']
    data_sources = ['https://nominatim.openstreetmap.org/ui/search.html']
    s = 'https://nominatim.openstreetmap.org/search.php?q=nevada+state+railroad+museum+carson+city&format=jsonv2'
    s = 'https://nominatim.openstreetmap.org/search.php?q=%s&format=jsonv2'
    s2 = 'https://nominatim.openstreetmap.org/ui/details.html?osmtype=W&osmid=407063554&class=tourism'
    s2 = 'https://nominatim.openstreetmap.org/ui/details.html?osmtype=W&osmid=%s&class=tourism'
    s3 = 'https://nominatim.openstreetmap.org/details.php?osmtype=W&osmid=407063554&class=tourism&addressdetails=1&hierarchy=0&group_hierarchy=1&format=json'
    s3 = 'https://nominatim.openstreetmap.org/details.php?osmtype=W&osmid=%s&class=tourism&addressdetails=1&hierarchy=0&group_hierarchy=1&format=json'

    print("Query: %s" % q)

    # Make request to first data source.
    r = requests.get(s % q)
    j = r.json()
    print("Number of results: %s" % len(j))
    for item in j:
        osm_id = item['osm_id']
        print("OSM ID: %s" % osm_id)

        r = requests.get(s3 % osm_id)
        event_name = r.json()['localname']
        wikidata_id = r.json()['extratags']['wikidata']
        print("Event name: %s" % event_name)
        print("Wikidata ID: %s" % wikidata_id)

        # Get the commons category link
        s4 = 'https://www.wikidata.org/wiki/Q14705239'
        s4 = 'https://www.wikidata.org/wiki/%s'
        r = requests.get(s4 % wikidata_id)
        soup = BeautifulSoup(r.content, 'html5lib')
        r = soup.findAll('a', href=re.compile("https://commons.wikimedia.org/wiki/Category.*"))
        if len(r) != 1:
            print("Too many")
            continue
        print("Going to: %s" % r[0]['href'])
        import ipdb;ipdb.set_trace()

        # Get scholia link and images
        r = requests.get(r[0]['href'])
        print(r.status_code)
        soup = BeautifulSoup(r.content, 'html5lib')
        s5 = 'https://scholia.toolforge.org/Q14705239'
        s5 = 'https://scholia.toolforge.org/%s' % wikidata_id
        r = soup.findAll('a', href=re.compile("https://commons.wikimedia.org/wiki/File:.*"))

    dossier = {
        'exp_id': 3,
        'type': 3,
        'image': 3,
        'name': 3,
        'description': 3,
        'hashtag': 3,
        'website': 3,
        'facebook': 3,
        'instagram': 3,
        'youtube': 3,
        'twitter': 3,
        'email': 3,
        'phone': 3,
        'addr1': 3,
        'addr2': 3,
        'city': 3,
        'state': 3,
        'zip': 3,
        'country': 3,
        'lat': 3,
        'long': 3,
        '': 3,
        '': 3,
    }
    return dossier


activity("nevada state railroad museum carson city")
