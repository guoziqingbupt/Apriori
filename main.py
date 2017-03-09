import readData
from frequentCount import *
from aprioriGen import *

min_sup = 2
D = readData.readData("shoppingList.csv")


def miningFrequentItemSet(D, min_sup):

    # initialized
    frequentItemSets = []
    L1 = find_frequent_1_itemsets(D, min_sup)
    frequentItemSets.extend(L1)

    # find frequent itemset Lk, until it is empty
    Lk = L1
    while len(Lk) != 0:

        # here, Ck is also a semi-finished Lk which processed by link and prune
        Ck = apriori_gen(Lk)

        # obtain final frequent itemset Lk
        Lk = scanDataBase(D, min_sup, Ck)

        frequentItemSets.extend(Lk)

    return frequentItemSets

if __name__ == "__main__":
    print(miningFrequentItemSet(D, min_sup))
