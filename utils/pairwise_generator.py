# utils/pairwise_generator.py

from allpairspy import AllPairs

def generate_indexed_combinations(category_counts):
    """
    Generates pairwise test combinations based on the number of options in each category.

    Pairwise (also called "all pairs") testing is a combinatorial testing technique that 
    significantly reduces the total number of combinations you need to test. Instead of 
    generating the full Cartesian product (all possible combinations of values), it ensures 
    that *every possible pair of values across parameters appears at least once* in the 
    generated set.

    Example:
    --------
    category_counts = {
        "Size": 3,        # Possible values: 0, 1, 2
        "Color": 2,       # Possible values: 0, 1
        "Eyes": 2         # Possible values: 0, 1
    }

    Full Cartesian product would be:
        3 x 2 x 2 = 12 total combinations.

    Pairwise will reduce this (e.g., ~4-5 combinations) while still covering every pair 
    (Size, Color), (Size, Eyes), and (Color, Eyes) at least once.
    """

    # 1) Build a list of parameter value ranges:
    #    For each category, create a list of possible indices [0..count-1].
    #    Example: {"Size": 3, "Color": 2} --> [[0, 1, 2], [0, 1]]
    parameters = [list(range(count)) for count in category_counts.values()]

    # 2) Keep the keys (category names) in a separate list so we can map
    #    indices back to category names later.
    keys = list(category_counts.keys())

    # 3) Use AllPairs from allpairspy to generate the reduced set of combinations.
    #    AllPairs iterates through the parameter lists and produces the minimum
    #    number of combinations needed to ensure every possible PAIR of values 
    #    appears at least once.
    #
    #    Example (from above):
    #        Input parameters: [[0, 1, 2], [0, 1]]
    #        Possible output:
    #           [0, 0]
    #           [1, 1]
    #           [2, 0]
    #           [0, 1]
    #
    #    Note: The order of values may be different on each run, but all pairs
    #          across parameters will be represented.
    combinations = list(AllPairs(parameters))

    # Return:
    #  - keys: list of category names, used for labeling
    #  - combinations: list of index combinations (pairwise reduced)
    return keys, combinations
