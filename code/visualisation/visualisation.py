import os
import csv
import matplotlib.pyplot as plt

# saving destination
outputDir = "docs/visualisation"
output_data = "data/output_data"

def outputCsv(workload, data):
    # Create csv filename based on the chosen workload by 
    # getting the last element from the workload path given
    if "\\" in workload:
        filename = "output_" + workload.split("\\")[-1]
    elif "/" in workload:
        filename = "output_" + workload.split("/")[-1]

    try:
        f = open(os.path.join(output_data, filename), 'w', newline='')
        # create the csv writer
        writer = csv.writer(f)
        for value in data:
            # write a row to the csv file
            writer.writerow(value)
        # close the file
        f.close()
    except Exception as e:
        print(e)

# creating scatter plot
def scatterPlot(workload, data):
    x = []
    y = []
    counter = 0
    
    # Constructing the x-axis and y-axis data list
    for value in data:
        x.append(counter)
        y.append(value)
        counter += 1

    # Generating the Scatter plot using the data lists
    plt.scatter(x, y)

    # Set the plot's title
    plt.title("Random Algorithm - %s" % workload.split("\\")[-1].replace(".csv", ""))
    
    # Set the x-axis and y-axis titles
    plt.xlabel("Amount of Runs")
    plt.ylabel("Amount of Steps")

    # Create plot's name based on the chosen workload by 
    # getting the last element from the workload path given
    if "\\" in workload:
        graph = 'random_algorithm_' + workload.split("\\")[-1].replace(".csv", "") + '.png'
    elif "/" in workload:
        graph = 'random_algorithm_' + workload.split("/")[-1].replace(".csv", "") + '.png'
    
    # Saving the plot
    plt.savefig(os.path.join(outputDir, graph))
    
    # Show the plot
    plt.show()