def look_and_say_generator(start_num):
    element = start_num
    while True:
        yield element
        chains = get_chains(element)
        element = int(count_chains(chains))

def get_chains(element):
    element = str(element)
    chain, chains = "", []

    for digit in element:
        if chain == "":
            chain = digit
        elif digit in chain:
            chain = chain + digit
        else:
            chains.append(chain)
            chain = digit
    chains.append(chain)
    return chains

def count_chains(counts):
    element = ""
    for chain in counts:
        element = element + str(len(chain)) + chain[0]
    return element

sequence_gen = look_and_say_generator(3)

# Now we can print out some sequence members:
print(next(sequence_gen))
print(next(sequence_gen))
print(next(sequence_gen))