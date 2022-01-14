import pandas as pd
import argparse

# load car files
# make a dictionary
vehicle = {}

with open(file_load, 'r') as file:
    csv_car_file = csv.DictReader(file)
    for row in csv_car_file:



# parser for command line
if __name__ == '__main__':

    # Import CSV file and read to Pandas Dataframe
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', nargs='?', help="Add game csv path here", default="gameboards/Rushhour6x6_1.csv")
    file = parser.parse_args()
    df = pd.read_csv(file.csvfile)

    print(df)