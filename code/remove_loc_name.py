import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='removes location_name column from the output csv file produced by reichlab_csv.py')
parser.add_argument('-f', '--file_name', required=True, help='name of csv file produced by reichlab_csv')
args = parser.parse_args()

df_state = pd.read_csv(args.file_name,  dtype=str)
df_state = df_state[df_state["location_name"] != "Vermont"]
df_state.drop("location_name", axis=1, inplace=True)
df_all = pd.concat([df_state],sort=False)

# formatted csv file name required for reichlab submission 
formatted_name = args.file_name.replace("_state", "")
#print("FORMATED NAME : ", formatted_name)

df_all.to_csv(formatted_name,index=False)