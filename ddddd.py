def calculate_structure_sum ():
    content = 0
    d_c = data_structure[0]
    d_c1 = data_structure[1]
    d_c2 = data_structure[2]
    d_c3 = data_structure[3]
    d_c4 = data_structure[4]

    if d_c in data_structure:
        content += sum(d_c)
    elif d_c1 in data_structure:
        content += (sum(d_c1.values())) + (len(d_c1.keys()))
    elif d_c2 in data_structure:
        c = d_c2[1].values()
        d = d_c2[1].keys()
        j = d_c2[0], sum(c), sum((len(i) for i in d))
        content += sum(j)
    elif d_c3 in data_structure:
        content += len(d_c3)
    elif d_c4 in data_structure:
        a = list(*list(*d_c4[1]))
        b = a[0], len(a[1]), len(a[2][0]), a[2][1]
        content += sum(d_c4[0], sum(b))
    print(content)
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

calculate_structure_sum()
