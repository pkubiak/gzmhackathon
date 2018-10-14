import csv
from tqdm import tqdm
from collections import Counter, defaultdict


with open('/run/media/solmyr/Maxtor/dane/f_napelnienie/f_napelnienie.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    flow_in, flow_out = defaultdict(int), defaultdict(int)
    limit = 1_000_000

    def save(fp):
        print('Saving')
        with open(fp, 'w') as file:
            for key in flow_in:
                file.write(f"{key[0]}\t{key[1]}\t{key[2]}\t{flow_in[key]}\t{flow_out[key]}\n")

    for i, row in tqdm(enumerate(reader)):
        date = row['doba_komunikacyjna_id']
        przystanek_id = int(row['przystanek_id'])
        wsiadlo = int(row['wsiadlo'])
        wysiadlo = int(row['wysiadlo'])

        year, month = int(date[0:4]), int(date[4:6])
        key = (year, month, przystanek_id)

        flow_in[key] += wsiadlo
        flow_out[key] += wysiadlo

        if i % 10_000_000 == 0:
            save('results.txt')
