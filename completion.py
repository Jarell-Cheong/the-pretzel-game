''' Detect if a pretzel link is the unlink or not '''


# Move 1's to the left
def move_ones(link):

    for i in range(len(link)):
        if link[i] == 1:
            link.insert(0, link.pop(i))

    return link


# Move -1's to the right
def move_neg_ones(link):

    for i in range(len(link)):
        if link[i] == -1:
            link.insert(len(link) - 1, link.pop(i))

    return link


# Move -2's to the left next to 1's
def move_neg_twos(link):
    
    one_index = -1

    for i in range(len(link)):
        if link[i] == 1:
            one_index += 1
    
    for i in range(len(link)):
        if link[i] == -2:
            link.insert(one_index + 1, link.pop(i))

    return link


# Move 2's to the right next to -1's
def move_twos(link):
    
    neg_one_index = len(link)

    for i in range(len(link)):
        if link[i] == -1:
            neg_one_index -= 1
    
    for i in range(len(link)):
        if link[i] == 2:
            link.insert(neg_one_index - 1, link.pop(i))

    return link


# Cancel out 1's with -1's
def reduce_ones(link):
    
    if link[0] != 1 or link[len(link) - 1] != -1:
        return link

    link.pop(0)
    link.pop(len(link) - 1)

    return reduce_ones(link)


# Cancel out -2's with remaining 1's and replace with 2's
def neg_twos_to_twos(link):

    if link[0] == 1:

        if -2 not in link:
            return link

        link.pop(link.index(-2))
        link.pop(0)
        link.insert(len(link), 2)

        return neg_twos_to_twos(link)

    return link


# Cancel out 2's with remaining -1's and replace with -2's
def twos_to_neg_twos(link):

    if link[len(link) - 1] == -1:

        if 2 not in link:
            return link

        link.pop(link.index(2))
        link.pop(len(link) - 1)
        link.insert(0, -2)

        return twos_to_neg_twos(link)

    return link


# Return the pretzel link in normal form
def normal_form(link):
    
    link = move_ones(link)
    link = move_neg_ones(link)
    link = move_neg_twos(link)
    link = move_twos(link)
    link = reduce_ones(link)
    
    if link[0] == 1:
        return neg_twos_to_twos(link)

    elif link[len(link) - 1] == -1:
        return twos_to_neg_twos(link)

    else:
        return link


# Return True if list represents the unlink and False otherwise
def check(link):
    
    link = normal_form(link)

    if len(link) == 1:
        return True

    elif len(link) == 2:

        if 1 in link or -1 in link:
            return True

        else:
            return False

    else:
        return False