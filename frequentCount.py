import copy


def find_frequent_1_itemsets(D, min_sup):
    """

    :param D: a dictionary, represents the whole transaction database
    :param min_sup: the minimum support count
    :return: a list L1, the collection of frequent 1 sets, and each element is a list
    """

    L1 = []
    C1 = {}

    for TID in D:

        for item in D[TID]:
            if item not in C1:
                C1[item] = 1
            else:
                C1[item] += 1

    for itemset in C1:
        if C1[itemset] >= min_sup:
            L1.append([itemset])

    return L1


def subsets(S):
    """
    find all subsets of set S, each subset is ordered
    :param S: a list
    :return: a list, and each element is a list
    """
    S.sort()

    path = []
    step = 0
    result = []

    dfs(S, path, step, result)
    return result


def dfs(S, path, step, result):
    n = len(S)
    if step == n:
        temp = copy.deepcopy(path)
        result.append(temp)
        return

    dfs(S, path, step + 1, result)
    path.append(S[step])
    dfs(S, path, step + 1, result)
    path.pop()


def scanDataBase(D, min_sup, semi_finished_Lk):
    """
    scan the transaction database, filter the infrequent itemset
    :param D: a dictionary, represents the whole transaction database
    :param min_sup:
    :param semi_finished_Lk: a list, represents semi_finished itemset Lk
    :return: the final frequent itemset Lk
    """

    Lk = []
    k = len(semi_finished_Lk)
    counts = [0 for i in range(len(semi_finished_Lk))]

    for TID in D:

        subSets = subsets(D[TID])

        for subSet in subSets:

            if subSet in semi_finished_Lk:
                counts[semi_finished_Lk.index(subSet)] += 1

    index = 0
    while index < k:
        if counts[index] >= min_sup:
            Lk.append(semi_finished_Lk[index])
        index += 1
    return Lk
