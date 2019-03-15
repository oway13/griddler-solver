#Input: List of 0/1 integers
#Returns: String of 0/1 integers
def toBin(intlist):
    return ''.join(str(e) for e in intlist)

#Input: list of equal length bit strings
#Returns: bit string of common bits
def common(bitlist):
    comlist = int(bitlist[0], 2)
    strlen = len(bitlist[0])
    for bitstring in bitlist:
        bint = int(bitstring, 2)
        comlist = bint & comlist
    comlist = bin(comlist)
    return comlist.zfill(strlen)

#Inputs: matchlist: list of positions that all intlists must have set
#        intlist: Single intlist to match against
#Returns: Boolean, whether or not they match
def match(matchlist, intlist):
    match = int(matchlist, 2)
    qint = int(toBin(intlist), 2)
    return match & qint == match

#Input: Int
#Returns: Int's Bitstring
def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

#Input: listlen: Total length of list to work within
#       intreqs: ordered list for order and length of runs
#Returns: list of lists with proper order and length of runs
def intlist_gen(listlen, intreqs):
    intlistlist = []
    blanks = listlen - sum(intreqs)
    betweens = len(intreqs) - 1

    #If multiple, but only one possible value
    if blanks == betweens:
        intlist = []
        for i in range(len(intreqs)):
            for j in range(intreqs[i]):
                intlist.append(1)
            intlist.append(0)
        intlist.pop()
        intlistlist.append(intlist)
        return intlistlist
    #If one, but only one possible value
    elif blanks == 0 and betweens == 0:
        intlist = []
        for i in range(intreqs[0]):
            intlist.append(1)
        intlistlist.append(intlist)
        return intlistlist
    #If one, but many possible values
    elif betweens == 0 and not blanks == 0:
        for i in range(blanks+1):
            intlist = []
            b_used = 0
            for j in range(i):
                intlist.append(0)
                b_used += 1
            for k in range(intreqs[0]):
                intlist.append(1)
            for l in range(blanks - b_used):
                intlist.append(0)
            intlistlist.append(intlist)



    return intlistlist

#Inputs: matchlist: list of positions that all intlists must have set
#        intlistlist: list of generated intlists that haven't been filtered
#Returns: list of intlists with non-matching intlists removed
def remove_nonmatches(matchlist, intlistlist):
    filtered_intlistlist = []
    for intlist in intlistlist:
        if match(matchlist, intlist):
            filtered_intlistlist.append(intlist)
    return filtered_intlistlist


#Inputs: intlist: list of 0/1 integers, 
#        intreqs: ordered list for order and length of runs
#Process: generates list of all possible bit strings that match requirements,
#         that also matches bits that are already there. Then calls common to
#         find the bits that are common to all bit strings. These are ones we
#         know are correct.
#Returns: list of 0/1 integers, hopefully partially solved, but not all will be
def partial_solve_array(intlist, intreqs):
    return

print(common(['1010', '1010', '1011']))
print(common(['0010', '0010', '0011']))


print("If multiple, but only one possible value")
print(intlist_gen(6, [1,2,1]))
print("If one, but only one possible value")
print(intlist_gen(6, [6]))
print("If one, but many possible values")
print(intlist_gen(6, [2]))
print(intlist_gen(6, [1]))
print(intlist_gen(6, [3]))
print("If many, but many possible values")
print(intlist_gen(6, [2, 1]))
print(intlist_gen(6, [1, 2]))
print(intlist_gen(6, [2, 2]))
print(intlist_gen(6, [1, 1, 1]))
print(intlist_gen(7, [1, 2, 1]))
print(intlist_gen(7, [2, 1, 1]))