#General
#For multiple sequences
#0*(1+0+)+1+0*

#For two
#0*1+0+1+0*
#Need to find all permutations of leftover 0s for number of runs equal to req+1 
#where only the first and last 0 run can have a length of 0
# from itertools import combinations

# def intlist_gen(listlen, intreqs):
#     zeros = listlen - sum(intreqs)
#     z_runs = len(intreqs) + 1
#     list(combinations(range()))

        
# intlist_gen(6, [1, 1, 1])


# #call generate(holes, zeros, 0, intlistlist)
# def generate(first, holeslen, zeros, hole, intlistlist, holes):
#     if hole == holeslen-1:
#         holes[hole] = zeros
#         intlistlist.append(holes)
#         return
#     else:
#         holes = [0 for _ in range(holeslen)]
#         holes[hole] = first
#         generate(1, holeslen, zeros-first, hole+1, intlistlist, holes)
#     return intlistlist
# print(generate(5, 3, 6, 0, [], []))

# def gen(runs, zeros):
#     #need to generate where one has most
#     intlistlist = [] 
#     for run in range(runs):
#         intlist = [0 for _ in range(runs)]
#         for x in range(zeros):
#             rem = zeros - x

def sorted_k_partitions(seq, k):
    """Returns a list of all unique k-partitions of `seq`.

    Each partition is a list of parts, and each part is a tuple.

    The parts in each individual partition will be sorted in shortlex
    order (i.e., by length first, then lexicographically).

    The overall list of partitions will then be sorted by the length
    of their first part, the length of their second part, ...,
    the length of their last part, and then lexicographically.
    """
    n = len(seq)
    groups = []  # a list of lists, currently empty

    def generate_partitions(i):
        if i >= n:
            yield list(map(tuple, groups))
        else:
            if n - i > k - len(groups):
                for group in groups:
                    group.append(seq[i])
                    yield from generate_partitions(i + 1)
                    group.pop()

            if len(groups) < k:
                groups.append([seq[i]])
                yield from generate_partitions(i + 1)
                groups.pop()

    result = generate_partitions(0)

    # Sort the parts in each partition in shortlex order
    result = [sorted(ps, key = lambda p: (len(p), p)) for ps in result]
    # Sort partitions by the length of each part, then lexicographically.
    result = sorted(result, key = lambda ps: (*map(len, ps), ps))

    intlistlist = []
    for i in result:
        if i not in intlistlist:
            intlistlist.append(i)

    return intlistlist

#Input: listlen: Total length of list to work within
#       intreqs: ordered list for order and length of runs
#Returns: list of lists with proper order and length of runs
def generate(listlen, intreqs):
    intlistlist = []
    zeros = listlen - sum(intreqs)
    holes = len(intreqs) + 1
    z_inter_list = [0 for _ in range(zeros)]
    z_combs = sorted_k_partitions(z_inter_list, holes)
    #For each possible 0 run spot (hole)
    for hole in range(holes):
        #For comb each z_comb
        for comb in z_combs:
            intlist = []
            #For each 0 run in one comb
            for z_run in range(len(comb)):
                #Add that many zeros to the list
                intlist.extend([0 for _ in range(len(comb[z_run]))])
                #For each 1 run in intreqs
                if not z_run == len(intreqs):
                    #Add that many ones to the list
                    intlist.extend([1 for _ in range(intreqs[z_run])])
            intlistlist.append(intlist)
    return intlistlist




# for groups in sorted_k_partitions([0,0,0,0,0,0], 3):
#         print(3, groups)

#print(sorted_k_partitions([0,0,0,0,0,0], 3))


for intlist in generate(9, [2, 1]):
    print(intlist)