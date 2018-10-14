import csv
from tqdm import tqdm
from collections import defaultdict

def float2(x):
    return float(x.replace(',', '.'))


routes = defaultdict(list)
routes_id = dict()
keys = set()

import json

with open('/run/media/solmyr/Maxtor/dane/f_gps/f_gps.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    count = 0
    iter = tqdm(enumerate(reader))
    for i, row in iter:
        key = (row['doba_komunikacyjna_id'], row['linia_id'], row['kurs_id'], row['przystanek_id'])
        route = (int(row['przystanek_id']), int(row['poprzedni_przystanek_id']))
        if route[0] == -1 or route[1] == -1:
            continue

        if route not in routes_id:
            print(key)
            routes_id[route] = key
            keys.add(key)

        if key in keys:
            routes[key].append((row['data_czas_zdarzenia'], float2(row['dlugosc_geograficzna']), float2(row['szerokosc_geograficzna'])))
        count += 1
        iter.set_postfix(count=count)
        if count % 1_000_000 == 0:
            print('Saving', i)
            res = {}
            for key in routes_id:
                route = routes[routes_id[key]]
                res[f"{key[0]}_{key[1]}"] = [(x,y) for _, x, y in sorted(route)]

            with open('paths.json', 'w') as output:
                output.write(json.dumps(res))
