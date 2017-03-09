import copy


def apriori_gen(L_k_subtract_1):
    """
    There are 2 steps in apriori_gen:
    1. link: execute l1 x l2, generate original Ck;
    2. prune: delete the candidate in Ck who has infrequent subset
    :param L_k_subtract_1: a list, each element is k-1 frequent itemset
    :return: a semi-finished k itemset candidates Lk
    """

    index1 = 0
    k = len(L_k_subtract_1[0]) + 1
    Ck = []

    # while: link process
    while index1 < len(L_k_subtract_1):

        # the itemset l1 that to be linked: l1 x l2
        l1 = L_k_subtract_1[index1]

        # traverse L(k - 1), find the other itemset l2
        for l2 in L_k_subtract_1[index1 + 1:]:

            if isLinkable(l1, l2):

                newItemSet = [item for item in l1[:k - 2]]

                # add tail element with order
                if l1[k - 2] < l2[k - 2]:
                    newItemSet.append(l1[k - 2])
                    newItemSet.append(l2[k - 2])
                else:
                    newItemSet.append(l2[k - 2])
                    newItemSet.append(l1[k - 2])

                Ck.append(newItemSet)

        index1 += 1

    # subSetTest: prune process
    return subSetTest(Ck, L_k_subtract_1)


def isLinkable(l1, l2):
    """
    :param l1: a list
    :param l2: a list
    :return: if l1 and l2 is linkable
    """

    n = len(l1)

    for index in range(n - 1):
        if l1[index] != l2[index]:
            return False
    return True


def subSetTest(Ck, L_k_subtract_1):
    """
    prune process: according to apriori, test if every itemset in Ck is possible frequent
    :param Ck: a list, and each element is also a list
    :param L_k_subtract_1: a list, and each element is also a list
    :return: a semi-finished Lk
    """

    # the cur itemset that to be tested.
    cur = 0
    n = len(Ck)

    semi_finished_Lk = []
    while cur < n:

        # testItemSet: a list
        testItemSet = Ck[cur]

        if not has_infrequent_subset(testItemSet, L_k_subtract_1):
            semi_finished_Lk.append(testItemSet)

        cur += 1

    return semi_finished_Lk


def has_infrequent_subset(testItemSet, L_k_subtract_1):
    """
    :param testItemSet: the candidate k itemset, is a list
    :param L_k_subtract_1: a list
    :return: testItemSet has a infrequent subset or not
    """

    for testSubSet in gen_ksub1_subsets(testItemSet):
        if testSubSet not in L_k_subtract_1:
            return True
    return False


def gen_ksub1_subsets(s):
    """
    get all k - 1 subsets of s
    :param s: a list, represents a itemset
    :return: a list, represents k - 1 subsets
    """

    index = 0
    k = len(s)

    result = []
    while index < k:

        exceptEle = s[index]
        temp = copy.deepcopy(s)
        temp.remove(exceptEle)

        result.append(temp)

        index += 1

    return result
