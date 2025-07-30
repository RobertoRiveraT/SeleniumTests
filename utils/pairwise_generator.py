from allpairspy import AllPairs

def generate_combinations():
    parameters = [
        ["azul", "rosa", "negro"],  # color
        ["gorro", "auriculares"],   # hat
        ["mochila", "ninguno"],     # accessory
    ]

    return list(AllPairs(parameters))
