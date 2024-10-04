import module_EM as EM

Row = int(input("Enter the number of row : "))
Column = int(input("Enter the number of column : "))

augmented_matrix = []
print("Enter the entries of augmented matrix row wise")

for row in range(Row) :
    a = []
    for column in range(Column) :
        a.append(int(input()))
    augmented_matrix.append(a)

EM.show_matrix(augmented_matrix, Row, Column)
print("|")

# make Identity Matrix
I_matrix = []
c = Column
if (Row < c):
  c = Row
for row in range(Row):
  b = []
  for column in range(c):
    if row == column :
      b.append(1)
    else :
      b.append(0)
  I_matrix.append(b)

EM.show_matrix(I_matrix, Row, Row)
print("|")

result_matrix = augmented_matrix.copy()
E_matrix = I_matrix.copy()
P_matrix = I_matrix.copy()
free_variable = []
temp = []
pivot_position = []
variable_value = []
col_permu = []
r = 0
c = 0
i_column = 0
i_row = 0
i_per_column = 0
free_variable_status = False
column_permutation_status = False

for i in range(Column-1):
  variable_value.append(0)

#convert augmented matrix to upper matrix
while i_column < Row:
  if(result_matrix[r][c] != 0):
    result_matrix = EM.cal_EM(result_matrix, r, c, E_matrix, Row, Column)
    a = []
    a.append(r)
    a.append(c)
    pivot_position.append(a)
    c+=1
    r+=1
  else:
    i_row = r
    while i_row < Row:
      if(result_matrix[i_row][c] != 0):
        print("Row Permutation")
        temp = P_matrix[r]
        P_matrix[r] = P_matrix[i_row]
        P_matrix[i_row] = temp
        result_matrix = EM.matrix_multiply(P_matrix, result_matrix)
        result_matrix = EM.cal_EM(result_matrix, r, c, E_matrix, Row, Column)
        EM.show_matrix(result_matrix, Row, Column)
        temp = P_matrix[r]
        P_matrix[r] = P_matrix[i_row]
        P_matrix[i_row] = temp
        a = []
        a.append(r)
        a.append(c)
        pivot_position.append(a)
        c+=1
        r+=1
        free_variable_status = False
        break
      else:        
        free_variable_status = True
      i_row+=1
    if(free_variable_status):
      print("free variable")
      i_per_column = c 
      while i_per_column < (Column-1):
        if(result_matrix[r][i_per_column] != 0):
          print("Column Permutation")
          for i in range(Row):
            temp = result_matrix[i][c]
            result_matrix[i][c] = result_matrix[i][i_per_column]
            result_matrix[i][i_per_column] = temp
          result_matrix = EM.cal_EM(result_matrix, r, c, E_matrix, Row, Column)
          EM.show_matrix(result_matrix, Row, Column)
          a = []
          a.append(c)
          a.append(i_per_column)
          col_permu.append(a)
          a = []
          a.append(r)
          a.append(c)
          pivot_position.append(a)
          c+=1
          r+=1
          break
        i_per_column+=1
  i_column+=1

if len(pivot_position) < Column:
  col = len(pivot_position)
  while col < Column-1:
    free_variable.append(col)
    col+=1

print("Index Column Free Variable: " + str(free_variable))
print("Pivot Position: " + str(pivot_position))
print("Column Permutation: " + str(col_permu))

#tranform to row  echelon from
for pivot in reversed(pivot_position):
  row = pivot[0]
  column = pivot[1]
  i_row = (row-1)
  
  while i_row > -1:
    if(i_row == column):
      l = 0
      E_matrix[i_row][column] = l
      result_matrix = EM.matrix_multiply(E_matrix, result_matrix)
      E_matrix[i_row][column] = 1
    else:
      l = (result_matrix[i_row][column]/result_matrix[row][column])*(-1)
      E_matrix[i_row][column] = l
      result_matrix = EM.matrix_multiply(E_matrix, result_matrix)
      E_matrix[i_row][column] = 0      
    EM.show_matrix(result_matrix, Row, Column)
    print("|")
    i_row-=1

#check consistent or inconsistent
if(len(pivot_position) == Row):
  consistent = True
else:
  consistent = EM.consistent_check(result_matrix,pivot_position, Row, Column)


if(consistent):
  #find value of variable
  if(not free_variable):
    for pivot in pivot_position:
      row = pivot[0]
      column =pivot[1]
      a = result_matrix[row][Column-1]/result_matrix[row][column]
      variable_value[column] = a
  else:
    i_column = 0
    while i_column < (Column-1):
      if i_column in free_variable:
        variable_value[i_column] = 1
      i_column+=1
    for pivot in pivot_position:
      row = pivot[0]
      column = pivot[1]
      for i in free_variable:
        result_matrix[row][Column-1] -= result_matrix[row][i]
      a = result_matrix[row][Column-1]/result_matrix[row][column]
      variable_value[column] = a
  if(col_permu):
    for i in reversed(col_permu):
      col1 = i[0]
      col2 = i[1]
      temp = variable_value[col1]
      variable_value[col1] = variable_value[col2]
      variable_value[col2] = temp
      
  #show aswer
  index = 1
  for i in variable_value:
    print("X" + "[" + str(index) + "]" + " is " + str(i))
    index+=1

else:
  print("This system is inconsistent")
