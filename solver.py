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
    return

#Inputs: matchlist: list of positions that all intlists must have set
#        intlistlist: list of generated intlists that haven't been filtered
#Returns: list of intlists with non-matching intlists removed
def remove_nonmatches(matchlist, intlistlist):
    return


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