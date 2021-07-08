
from db import mydb

cur = mydb.cursor()


cur.execute('''
    INSERT INTO todos(todo_name) 
    VALUES
        ("Play Football"),
        ("Learn Python"),
        ("Приготовить еду"),
        ("Починить дверь");
    
''')

mydb.commit()