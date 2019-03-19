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


#call generate(holes, zeros, 0, intlistlist)
def generate(first, holeslen, zeros, hole, intlistlist, holes):
    if hole == holeslen-1:
        holes[hole] = zeros
        intlistlist.append(holes)
        return
    else:
        holes = [0 for _ in range(holeslen)]
        holes[hole] = first
        generate(1, holeslen, zeros-first, hole+1, intlistlist, holes)
    return intlistlist
print(generate(5, 3, 6, 0, [], []))

def gen(runs, zeros):
    #need to generate where one has most
    intlistlist = []
    for run in range(runs):
        intlist = [0 for _ in range(runs)]
        for x in range(zeros):
            rem = zeros - x

