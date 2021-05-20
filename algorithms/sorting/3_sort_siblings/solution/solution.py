


def sort_siblings(sib_dict):
    return sorted(sib_dict.items(), key = lambda x: (x[1],x[0]))


sib_dict = {"Anton": 29,
            "Cosette": 3,
            "Nancy": 15,
            "Lucas": 15}

print(sort_siblings(sib_dict)) == [("Cosette", 3), ("Lucas", 15), ("Nancy", 15), ("Anton", 29)]
