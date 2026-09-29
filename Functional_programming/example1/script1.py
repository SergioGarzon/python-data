# Compression examples

list_data = [10, 15, 88, 99, 101, 151, 163, 177, 201, 202, 350, 368]

list_compression = [l for l in list_data if (l % 2) == 0]

for lc in list_compression:
    print(lc)