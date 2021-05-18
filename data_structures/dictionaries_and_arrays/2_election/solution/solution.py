#Completed
def election_winner(clst):
    election_dict = {name:0 for name in clst}
    for name in clst:
        if name in election_dict.keys():
            election_dict[name]+=1
    print(election_dict)
    sorted_dict = sorted(election_dict.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_dict)
    #sorted_dict = sorted(election_dict, key=lambda x: (-election_dict[x], x))
    #return sorted_dict[0]
    return sorted_dict[0][0]
    
    

clst = ["Trump", "Bernie", "Bernie", "Oprah", "Biden", "Bernie", "Trump"]
clst2 = ["Trump", "Bernie", "Bernie", "Trump"]
print(election_winner(clst)) #== "Bernie"
print(election_winner(clst2)) #== "Bernie"