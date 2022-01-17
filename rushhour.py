import pandas as pd
import argparse

def load_vehicles(df):
    

# parser for command line
if __name__ == '__main__':

    # Import CSV file and read to Pandas Dataframe
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', nargs='?', help="Add game csv path here", default="gameboards/Rushhour6x6_1.csv")
    file = parser.parse_args()
    df = pd.read_csv(file.csvfile)

    load_vehicles(df)

