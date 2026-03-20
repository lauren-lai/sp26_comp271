def replace_with_ranks(values: list[int]) -> list[int]:
    """
    Return a new list where each distinct value is replaced
    by its rank in sorted order.

    Precondition:
        values contains distinct integers.

    Postcondition:
        Returns a list of the same length.
    """
    ranked = []
    unsorted = values.copy()
    values.sort()
    
    for i in range(len(unsorted)):
        found = False
        j = 0
        while not found and (j < len(values)):
            if unsorted[i] == values[j]:
                ranked.append(j)
                found = True
            else:
                j += 1

    return ranked



def print_pairs_with_sum(values: list[int], target: int) -> None:
    """
    Print every pair of numbers in values whose sum equals target.

    Precondition:
        values is a list of integers.

    Postcondition:
        Prints each discovered pair.
    """
    for i in range(len(values)):
        for j in range(i, len(values)):
            if (values[i] + values[j]) == target:
                print(f"{values[i]}, {values[j]}")


def is_subset(list1: list[int], list2: list[int]) -> bool:
    """
    Return True if every element of list2 appears in list1.

    Precondition:
        list1 and list2 are lists of integers.

    Postcondition:
        Returns True exactly when list2 is a subset of list1.
    """
    is_subset = False

    for i in range(len(list2)):
        found = False
        j= 0
        while not found and (j < len(list1)):            
            if list2[i] == list1[j]:
                found = True
                is_subset = True
            j += 1
        if not found and is_subset: # previous matches, but now error
            is_subset = False

    return is_subset
        
            

def main() -> None:
    # Uncomment after implementing the functions.

    print(replace_with_ranks([10, 50, 35, 82, 13]))
    print_pairs_with_sum([10, 50, 35, 82, 13, 25], 60)
    print(is_subset([10, 50, 35, 82, 13, 25], [10, 35, 13]))
    print(is_subset([10, 50, 35, 82, 13, 25], [10, 35, 13, 8]))
    

if __name__ == "__main__":
    main()