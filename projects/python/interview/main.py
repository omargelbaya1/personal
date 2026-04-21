

# def get_second_largest(l:list[int]) -> int:
#     set_l=set(l)
#     max_no=max(l)
#     print(max_no)
#     set_l.remove(max_no)
#     print(set_l)
#     # pos_max= set_l.index(max_no)
#     # print(pos_max)
#     # set_l.pop(pos_max)
#     # print(l)
#     # print(max( set_l))
#     print(max(set_l))
#     return max( set_l)
    
# def get_positons_in_list(l_chars:list[str])->dict:
#     my_dict={}
#     for v in l_chars:
#         my_dict[v]=[]
#     for i,v in enumerate(l_chars):
#         my_dict[v].append(i)

#     print(my_dict)
#     return my_dict


# def get_items_which_occur_in_both_lists(l1:list[str],l2:list[str]) -> set[str]:
        
#         # set_l1=set(l1)
#         # set_l2=set(l2)

#         list_of_chars=[]

#         for i in l1:
#             for j in l2:
#                   if i==j:   
#                     list_of_chars.append(i)
        
#         set(list_of_chars)
#         print(list_of_chars)            
#         return list_of_chars

                  



# l1=["a","b","c"]
# l2=["a","d","e"]

# get_items_which_occur_in_both_lists(l1,l2)



# l_chars=['a','b','c','b']
# # l=[1,2,3,4]

# # get_second_largest(l)
# get_positons_in_list(l_chars)


country2colours = {
   "england": ["red", "white"],
   "scotland": ["blue", "white"],
   "northern ireland": ["red", "white"],
   "wales": ["red", "white", "green"],
}

def reverse_mapping(d:Dict[str,list[str]]) -> Dict[str,list[str]]:

    new_dict={}
    for i,v in d.items():
        for colour in v:
            new_dict[colour]=[]
            new_dict[colour].append(i)
    
    print(new_dict)

reverse_mapping(country2colours)        