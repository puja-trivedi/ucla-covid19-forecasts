import argparse
from data import *
import os

def check_dir(path):
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(path)
        #print("The new directory is created!")

parser = argparse.ArgumentParser(description='get historical data from given dataset')
parser.add_argument('-b', '--begin_date', required=True, help='start date of historical date given in %Y-%m-%d format')
parser.add_argument('-e', '--end_date', required=True, help='end date of historical date given in %Y-%m-%d format')
parser.add_argument('-l', '--level', default = "state", help='state, nation or county')
parser.add_argument('-s', '--state', default = "default", help='state')
parser.add_argument('-n', '--nation', default = "default", help='nation')
parser.add_argument('-d', '--dataset', default = "JHU", help='nytimes')
args = parser.parse_args()

data = NYTimes(level='states') if args.dataset == "NYtimes" else JHU_US(level='states')

state = args.state
state_table = data.table[data.table['state'] == us.states.lookup(state).name]
tab = state_table


date = pd.to_datetime(tab['date'])
start = datetime.datetime.strptime(args.begin_date, '%Y-%m-%d')
end = datetime.datetime.strptime(args.end_date, '%Y-%m-%d')
mask = (date >= start) & (date <= end)
#df = tab[mask][['date','cases','deaths']]
df = tab[mask]
dir_path = "historical_data/"
check_dir(dir_path)
file_name = args.state + "_" + args.begin_date + "_" + args.end_date + "_histData.csv"
#df.to_csv(dir_path + file_name, index=False)
df.to_csv(dir_path + file_name)
print("Done retrieving historical data.\nSaved in: " + dir_path+file_name)