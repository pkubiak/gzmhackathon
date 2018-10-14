import csv, json, re, random
from collections import defaultdict, Counter


class Database:
    Cities = defaultdict(set)
    NodesGroups = defaultdict(list)
    Nodes = dict()
    with open('database/nodes.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            id = int(row['id'])
            name = re.sub(r'\(.*?\)', '', row['kod']).strip()
            name = re.sub(r'\d+$', '*', name)
            name = re.sub(r'\d+t$', '*t', name)

            Nodes[id] = name
            long = float(row['dlugosc_geograficzna'].replace(',', '.'))
            lat = float(row['szerokosc_geograficzna'].replace(',', '.'))
            if(abs(long) < 0.01 and abs(lat) < 0.01):
                continue
            NodesGroups[name].append([long, lat])
            Cities[row['gmina']].add(name)

        for name in NodesGroups:
            group = NodesGroups[name]
            long = sum(v for v, _ in group) / len(group)
            lat = sum(v for _, v in group) / len(group)
            NodesGroups[name] = {'long': long, 'lat': lat, 'name': name}
    NodesCounter = Counter()
    Routes = set()
    with open('database/routes.tsv') as tsvfile:
        for line in tsvfile:
            id, start, end = line.split('\t')
            start = Nodes[int(start)]
            end = Nodes[int(end)]
            NodesCounter[start] += 1
            NodesCounter[end] += 1
            Routes.add((start, end))
        print(len(Routes))


    Paths = dict()
    with open('database/paths.json') as jsonfile:
        Paths = json.load(jsonfile)


    Delays = dict()
    with open('database/delays.tsv') as tsvfile:
        for i, line in enumerate(tsvfile):
            start, end, time_of_day, delay = line.split('\t')
            start = int(start)
            end = int(end)
            if time_of_day != 'wczesne popoludnie': continue
            delay = float(delay)
            start = Nodes[start]
            end = Nodes[end]

            key = (start, end)
            if key not in Delays:
                Delays[key] = [0, 0]
            suma, count = Delays[key]
            Delays[key] = [suma + delay, count + 1]

    @staticmethod
    def routes_per_nodes(nodes):
        routes = {}
        for route in Database.Routes:
            if route[0] in nodes and route[1] in nodes:
                key = f"{route[0]}_{route[1]}"
                # if key in Database.Paths:
                #     routes[key] = [(y, x) for x, y in Database.Paths[key]]
                # # else:
                s0 = Database.NodesGroups[route[0]]
                s1 = Database.NodesGroups[route[1]]
                delay = Database.Delays.get(route)
                delay = delay[0] / delay[1] if delay else 0.0
                routes[key] = {'points': [[s0['lat'], s0['long']], [s1['lat'], s1['long']]], 'delay': delay}
        return routes
