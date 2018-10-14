from tqdm import tqdm
import csv, sys, pprint, math
# import dateutil.parser
import datetime
from collections import Counter, defaultdict
import numpy as np


times_of_day = ['noc'] * 6 + ['rano'] * 3 + ['przedpoludnie'] * 3 + ['wczesne popoludnie'] * 4 + ['pozne popoludnie'] * 3 + ['wieczor'] * 3 + ['noc'] * 2
assert len(times_of_day) == 24

required_keys = ('linia_id', 'przystanek_id', 'poprzedni_przystanek_id', 'planowana_godzina', 'zrealizowana_godzina')

if __name__ == '__main__':
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        count, suma = Counter(), defaultdict(int)
        delays = []

        for i, row in tqdm(enumerate(reader)):
            # values = list(map(row.get, required_keys))
            # print(values)
            if all(row[key] != '' for key in required_keys):
                # 2015-09-09 09:04:07'
                # dateutil.parser.parse(row['zrealizowana_godzina'])
                # dateutil.parser.parse(row['planowana_godzina'])
                zrealizowana_godzina = datetime.datetime.strptime(row['zrealizowana_godzina'], '%Y-%m-%d %H:%M:%S')
                planowana_godzina = datetime.datetime.strptime(row['planowana_godzina'], '%Y-%m-%d %H:%M:%S')

                delay = (zrealizowana_godzina - planowana_godzina).total_seconds()
                if abs(delay) > 1200: continue
                # if delay < -1000:
                #     pprint.pprint(row)
                #     print('>> ', delay)
                # if delay > 1800:
                #     continue
                # delays.append(delay)

                time_of_day = times_of_day[planowana_godzina.hour]
                key = (row['przystanek_id'], row['poprzedni_przystanek_id'], time_of_day)
                count[key] += 1
                suma[key] += delay
            if i % 1_000_000 == 0:
                with open('delays.tsv', 'w') as output:
                    for key in count:
                        output.write('\t'.join(map(str, [*key, suma[key] / count[key]]))+'\n')

        # res = {'stops': {}, 'delays': {}}
        #
        # for i, count in count.most_common(100):
        #     avg_delay = suma[i] / count
        #     res['stops'][i[1]] = [0.0, 0.0]
        #     res['stops'][i[2]] = [0.0, 0.0]
        #     res['delays'][f"{i[1]}_{i[2]}"]  = avg_delay
        #     print(i, avg_delay)
        # import json
        # print(json.dumps(res))

    # import matplotlib.pyplot as plt
    # hist, bins = np.histogram(delays, bins=200)
    # hist = list(map(lambda x: math.log(x+1), hist))
    # width = 0.7 * (bins[1] - bins[0])
    # center = (bins[:-1] + bins[1:]) / 2
    # plt.bar(center, hist, align='center', width=width)
    #
    # from scipy.stats import skewnorm
    # a = 4.8
    # x = np.linspace(-2500, 2500, 1000)
    # rv = skewnorm(a)
    # plt.plot(x, 9.5*rv.pdf(x/500+0.25), 'k-', lw=2, label='frozen pdf')
    # plt.show()
