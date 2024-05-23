import mysql.connector
# try:
connection = mysql.connector.connect(host = "127.0.0.1", port=3306, user = "root",password = "123456B")

#     if connection.is_connected(): 
#         print("Connected to MySQL database") 
#     else: 
#         print("Failed to connect to MySQL database") 
# except mysql.connector.Error as e: 
#     print(f"Error connecting to MySQL database: {e}")
    
cursor=connection.cursor()
cursor.execute('CREATE DATABASE my_db')

create_pizza_table_query="""
CREATE TABLE my_db.Pizza(
    id INT PRIMARY KEY,
    name VARCHAR(40),
    describe VARCHAR(20),
    price INT
)
"""
create_ingredients_table_query="""
CREATE TABLE my_db.Ingredients(
    id INT PRIMARY KEY,
    name VARCHAR(40),
)
"""
create_customers_table_query="""
CREATE TABLE my_db.Customers(
    id INT PRIMARY KEY,
    FirstName VARCHAR(40),
    LastName VARCHAR(40),
    Phone VARCHAR(10),
    Email VARCHAR(15),
    Address VARCHAR(15)
)
"""
create_employees_table_query="""
CREATE TABLE my_db.Employees(
    id INT PRIMARY KEY,
    FirstName VARCHAR(40),
    LastName VARCHAR(40),
    Phone VARCHAR(10),
    Email VARCHAR(15),
    Position VARCHAR(15)
)
"""

create_pizzaingredients_table_query="""
CREATE TABLE my_db.PizzaIngredients(
    PizzaID INT FOREIGN KEY REFERENCES Pizza(id)
    IngredientID INT FOREIGN KEY REFERENCES Ingredients(id)
)
"""

insert_pizza_query="""
INSERT INTO my.db.Pizza (id,name,describe,price)
VALUES (1,"Migruli","dadlidir",7),
       (2,"Qarisiq","cox dadlidi",15),
       (3,"Toyuqlu","damdadli",10),
       (4,"Gobelekli","BOMBASTIC DADLIIIIII",12)
"""

insert_ingredient_query="""
INSERT INTO my.db.Ingredient (id,name)
VALUES (1,"gobelek"),
       (2,"zeytun"),
       (3,"pendir")
"""
insert_customers_query="""
INSERT INTO my.db.Customers (id,FirstName,LastName,Phone,Email,Address)
VALUES (1,"Mubariz","Agayev","055-642-12-12","MUBAGA@gmail.com","nesimi"),
       (2,"Shams","Shirali","050-642-12-12","SHAMSHIR@gmail.com","razin")
"""
insert_employees_query="""
INSERT INTO my.db.Employees (id,FirstName,LastName,Phone,Email,Position)
VALUES (1,"Zehra","Shirali","070-642-12-12","ZEHRSHIR@gmail.com","Mudir"),
       (2,"Saafa","Hacizada","077-642-12-12","SAAFHACI@gmail.com","Muavin")
"""

insert_pizzaingredients_query="""
INSERT INTO my.db.PizzaIngredients (PizzaID,IngredientID)
VALUES (1,2),
       (2,1),
       (3,3)
"""


cursor.execute(create_pizza_table_query)
cursor.execute(create_ingredients_table_query)
cursor.execute(create_customers_table_query)
cursor.execute(create_employees_table_query)
cursor.execute(create_pizzaingredients_table_query)
cursor.execute(insert_pizza_query)
cursor.execute(insert_ingredient_query)
cursor.execute(insert_customers_query)
cursor.execute(insert_employees_query)
cursor.execute(insert_pizzaingredients_query)