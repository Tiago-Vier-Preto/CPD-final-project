from Table import Table
from tabulate import tabulate

Table = Table("enemDB")

print("Table Creation\n")
Table.create_table("enemDB")

# id , Sexo, Faixa Etária, Cor/Raça, Situação E.M, Tipo de Escola, UF, Nota Matemática Nota CN, Nota Redação 

print("Table Insert\n")
Table.insert_into_table("enemDB", ["M", 1, 2, 3, 62, 2, 44, 55, 10])
Table.insert_into_table("enemDB", ["M", 1, 2, 3, 62, 2, 55, 10, 99])
Table.insert_into_table("enemDB", ["F", 1, 2, 3, 62, 2, 10, 99, 100])
Table.insert_into_table("enemDB", ["F", 1, 2, 3, 62, 2, 62, 22, 88])
records, columns = Table.select_from_table("enemDB",['*'])
print(tabulate(records, headers=columns))

print("Table Record Deletion\n")
column = "Nota Redação"
operator = "="
value = 88
is_not = False
Table.delete_record("enemDB", column, operator, value, is_not)
records, columns = Table.select_from_table("enemDB",['*'])
print(tabulate(records, headers=columns))


print("Table Record Updation\n")
set_column = "Cor/Raça"
set_value = 4
cond_column = "Nota Redação"
cond_operator = "="
cond_value = 10
is_not = False
Table.update_record("enemDB", set_column, set_value, cond_column, cond_operator, cond_value, is_not)
records, columns = Table.select_from_table("enemDB",['*'])
print(tabulate(records, headers=columns))


print("Table Record Selection\n")
select_columns = ["id","Nota Matemática"]
cond_column = "Nota CN"
cond_operator = ">="
cond_value = 11
is_not = False
records, columns = Table.select_from_table("enemDB", select_columns, cond_column, cond_operator, cond_value,
                                           is_not)
print(tabulate(records, headers=columns))