import os
import csv
import matplotlib.pyplot as plt

outputDir = "code/visualisation/output"


def outputCsv(workload, data):
    if "\\" in workload:
        filename = "output_" + workload.split("\\")[-1]
    elif "/" in workload:
        filename = "output_" + workload.split("/")[-1]

    try:
        f = open(os.path.join(outputDir, filename), 'w', newline='')
        # create the csv writer
        writer = csv.writer(f)
        for value in data:
            # write a row to the csv file
            writer.writerow(value)
        # close the file
        f.close()
    except Exception as e:
        print(e)


def scatterPlot(workload, data):
    x = []
    y = []
    counter = 0
    for value in data:
        x.append(counter)
        y.append(value)
        counter += 1
    plt.scatter(x, y)
    plt.title("Random Algorithm - %s" % workload.split("\\")[-1].replace(".csv", ""))
    plt.xlabel("Amount of Runs")
    plt.ylabel("Amount of Steps")

    if "\\" in workload:
        graph = 'random_algorithm_' + workload.split("\\")[-1].replace(".csv", "") + '.png'
    elif "/" in workload:
        graph = 'random_algorithm_' + workload.split("/")[-1].replace(".csv", "") + '.png'
    plt.savefig(os.path.join(outputDir, graph))
    plt.show()