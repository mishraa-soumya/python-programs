def matrix_transpose():
    m = [[1, 2], [3, 4], [5, 6]]
    # Finding transpose using list comprehension
    # res = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    # for row in res:
        #    print(row)
    res = []
    for i in range(len(m[0])):
        print(f"i => {i}")
        rows = []
        for j in range(len(m)):
            print(f"j => {j}")
            print(f"m[j][i]: {m[j][i]}")
            rows.append(m[j][i])
        else:
            res.append(rows)
    else:
        print(f"The transpose matrix is: {res}")

matrix_transpose()