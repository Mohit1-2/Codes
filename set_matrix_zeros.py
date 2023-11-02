def main():
    matrix = [[1,2,3], [4,5,3], [7,0,9]]
    row_len = len(matrix)
    col_len = len(matrix[0])
    set_matrix_zeros(matrix, row_len, col_len)
    print(matrix)

def set_matrix_zeros(matrix, row_len, col_len):
    temp_row = [-1] * row_len
    temp_col = [-1] * col_len

    for row in range(row_len):
        for col in range(col_len):
            # if matrix value is zero then make temp_row and temp_col also 0 to keep track of zero
            if matrix[row][col] == 0:
                temp_row[row] = 0
                temp_col[col] = 0
    
    for row in range(row_len):
        for col in range(col_len):
            # if we find any of the temp_row and temp_col as 0 then make that row or column 0
            if temp_row[row]==0 or temp_col[col] == 0:
                matrix[row][col] = 0


if __name__ == "__main__":
    main()