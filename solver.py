#Input: List of 0/1 integers
#Returns: String of 0/1 integers
def toBin(intlist):
    return ''.join(str(e) for e in intlist)

#Input: list of bit strings
#Returns: bit string of common bits
def common(bitlist):
    comlist = bitlist[0]
    for b in bitlist:
        comlist &= b
    return comlist