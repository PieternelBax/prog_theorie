import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('csvfile', nargs='?', help="Add game csv path here", default="gameboards/Rushhour6x6_1.csv")
file = parser.parse_args()
df = pd.read_csv(file.csvfile)

print(df)

