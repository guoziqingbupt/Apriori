import csv


def readData(fileName):
    """
    read the csv data into a dictionary
    :param fileName:
    :return: a dictionary, as form as {TID: [items list]}
    """

    with open(fileName) as csvFile:

        reader = csv.reader(csvFile)

        transactions = {}

        for line in reader:

            ID = line[0]
            itemList = []

            for item in line[1:]:
                itemList.append(item)

            transactions[ID] = itemList

    return transactions


