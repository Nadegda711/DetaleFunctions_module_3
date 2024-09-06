def calculate_structure_sum ():
    data_structure = [ [1, 2, 3],   {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),   "Hello",   ((), [{(2, 'Urban', ('Urban2', 35))}]) ]
    d_c = data_structure[0]
    d_c1 = data_structure[1]
    d_c2 = list(data_structure[2])
    d_c3 = data_structure[3]
    d_c4 = data_structure[4]
    a = list(*list(*d_c4[1]))

    num_and_len  = sum(d_c)
    num_and_len1 = sum(d_c1.values()) + sum(len(i) for i in d_c1.keys())
    num_and_len2 = d_c2[0] + sum(d_c2[1].values()) + sum(len(j) for j in d_c2[1].keys())
    num_and_len3 = len(d_c3)
    num_and_len4 = len(d_c4[0]) + a[0] + len(a[1]) + len(a[2][0]) + a[2][1]
    print(num_and_len+ num_and_len1+ num_and_len2+ num_and_len3+ num_and_len4)

calculate_structure_sum()
