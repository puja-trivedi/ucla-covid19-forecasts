import csv
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='')
parser.add_argument('--PRED_DATA', '-p', default = "default",
                    help='name of file that contains predictions made from model')
parser.add_argument('--LEVEL', '-l', default = "default",
                    help='level : country, state, county')
parser.add_argument('--LEVEL_NAME', '-n', default = "default",
                    help='specific country, state, or county')                    
args = parser.parse_args()


# THIS WAY WORKS (BUT IT REMOVES HEADER/COLUMN NAMES):
# with open(args.PRED_DATA, 'r') as inp, open('first_edit.csv', 'w') as out:
#     writer = csv.writer(out)
#     for row in csv.reader(inp):
#         if row[0] < "2022-01-01":
#             writer.writerow(row)

df = pd.read_csv(args.PRED_DATA)
df = df[(df.Date > '2021-11-30') & (df.Date < '2022-01-01')]
df.to_csv('delta_pred' + '_' + args.LEVEL + '_' + args.LEVEL_NAME + '.csv', index=False)
