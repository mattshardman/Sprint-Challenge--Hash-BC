#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # make the number of buckets equal to the length
    ht = HashTable(length)
    # add each item as its own key
    for i in range(length):
        # the value should be the hash key
        hash_table_insert(ht, weights[i], i)
    
    # loop through the weights list
    for i in range(length):
        # for each one check the hash table to see if there is an element that adds to make the limit
        needed_value = limit - weights[i]

        el = hash_table_retrieve(ht, needed_value)

        # if there is return these two
        if el:
            if el > i:
                return (el, i)
            else:
                return (i, el)
            
    # otherwise return none
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
