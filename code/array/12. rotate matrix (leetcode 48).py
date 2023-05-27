# import numpy as np
# matrix = np.array([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,13,16]])
# print(matrix)
#
# n=len(matrix)
# no_of_layers = n//2
# #let tl=tops_col, tr=rights_row, br=bottoms_col, bl=lefts_row
# for layer in range(no_of_layers):
#     tops_col = layer-1 #for layer-0 ,tops_col initially = -1
#     rights_row = layer-1
#     bottoms_col = (n-layer) #for layer-0, bottoms_col initially = 4
#     lefts_row = (n-layer)
#
#     for square_no in range(layer,(n-layer)-1):
#         tops_col+=1
#         rights_row+=1
#         bottoms_col-=1
#         lefts_row-=1
#         # top to right
#         temp1 = matrix[rights_row][n-1-layer]
#         matrix[rights_row][n-1-layer] = matrix[layer][tops_col]
#
#         # right to bottom
#         temp2 = matrix[n-1-layer][bottoms_col]
#         matrix[n - 1 - layer][bottoms_col] = temp1
#
#         # bottom to left
#         temp1 = matrix[lefts_row][layer]
#         matrix[lefts_row][layer] = temp2
#
#         # left to top
#         matrix[layer][tops_col] = temp1
#
# print(matrix)










import numpy as np

matrix = np.array([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,13,16]])
matrix = np.array([[5,1,9,11,12],[2,4,8,10,96],[13,3,6,7,97],[15,14,13,16,98],[99,95,94,93,90]])

print(matrix)

n=len(matrix)
# tl={'row':0,'col':-1}
# tr={'row':-1,'col':n-1}
# bl={'row':n-1+1,'col':0}
# br={'row':n-1,'col':n-1+1}

# tl={'row':0,'col':0}
# tr={'row':0,'col':n-1}
# bl={'row':n-1,'col':0}
# br={'row':n-1,'col':n-1}

no_of_layers = n//2 #int(n/2)
# print(no_of_layers)
for layer in range(no_of_layers):
    # print("layer-",layer)
    tl = {'row': layer, 'col': layer-1}
    tr = {'row': layer-1, 'col': n-layer- 1}
    bl = {'row': n-layer-1+1, 'col': layer}
    br = {'row': n-layer- 1, 'col': n-layer-1+1}
    for i in range(layer,n-layer-1):
        # print("i-",i)
        tl['col']+=1
        tr['row']+=1
        br['col'] -= 1
        bl['row']-=1

        # print(tl,tr,br,bl)
        # print("tl", matrix[tl['row']][tl['col']])
        # print("tr", matrix[tr['row']][tr['col']])
        # print("br", matrix[br['row']][br['col']])
        # print("bl", matrix[bl['row']][bl['col']])
        temp1 = matrix[tr['row']][tr['col']]
        matrix[tr['row']][tr['col']] = matrix[tl['row']][tl['col']]
        # tr-br
        temp2 = matrix[br['row']][br['col']]
        matrix[br['row']][br['col']] = temp1

        # br-bl
        temp1 = matrix[bl['row']][bl['col']]
        matrix[bl['row']][bl['col']] = temp2

        # bl-tl
        matrix[tl['row']][tl['col']] = temp1
    # tl->tr->br->bl->tl
    print()

    # tl-tr


print(matrix)
#



