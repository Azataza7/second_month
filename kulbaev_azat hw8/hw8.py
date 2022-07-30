import sqlite3
from sqlite3 import Error


def create_data_connection(db_name):
    connector = None
    try:
        connector = sqlite3.connect(db_name)
    except Error as e:
        print(e)

    return connector


def create_table(connector, sql):
    try:
        cursor = connector.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def create_product(connector, products):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity)
        VALUES(?, ?, ?)
        '''
        cursor = connector.cursor()
        cursor.execute(sql, products)
        connector.commit()
    except Error as e:
        print(e)


def change_price_quantity(connector, products):
    try:
        sql = '''UPDATE products SET price = ?, quantity = ? WHERE id = ?'''
        cursor = connector.cursor()
        cursor.execute(sql, products)
        connector.commit()
    except Error as e:
        print(e)


def delete_products(connector, id):
    try:
        sql = '''DElETE FROM products WHERE id = ?'''
        cursor = connector.cursor()
        cursor.execute(sql, (id,))
        connector.commit()
    except Error as e:
        print(e)


def all_products(connector):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connector.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        for i in row:
            print(i)
    except Error as e:
        print(e)


def select_products_price_quantity(connector, min_price, max_quantity):
    try:
        sql = '''SELECT * FROM products WHERE price < ? and quantity > ?'''
        cursor = connector.cursor()
        cursor.execute(sql, (min_price, max_quantity))
        row = cursor.fetchall()

        for i in row:
            print(i)
    except Error as e:
        print(e)


def search_product(connector, product_name):
    sql = '''SELECT * FROM product WHERE product_name like ?'''
    try:
        cursor = connector.cursor()
        cursor.execute(sql, [product_name])
        rows = cursor.fetchall()

        for r in rows:
            print(r)
    except Error as e:
        print(e)


connection = create_data_connection('''hw.db''')
create_products_table = '''
CREATE table products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NUll DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

if connection is not None:
    print('connection successfully!')
    # create_table(connection, create_products_table)

    # create_product(connection, ("Onion", 68.54, 5))
    # create_product(connection, ("Tomato", 98.23, 22))
    # create_product(connection, ("Potato", 77.12, 64))
    # create_product(connection, ("Ketchup", 77.12, 11))
    # create_product(connection, ("Apple", 99.3, 65))
    # create_product(connection, ("Pen", 100.0, 38))
    # create_product(connection, ("Pineapple", 50.2, 45))
    # create_product(connection, ("Bread", 41.82, 67))
    # create_product(connection, ("Cola Cola", 100.0, 1))
    # create_product(connection, ("Pepsi Cola", 32.0, 2))
    # create_product(connection, ("Vodka", 77.09, 9))
    # create_product(connection, ("Balalaika", 93.0, 7))
    # create_product(connection, ("Watermelon", 87.55, 13))
    # create_product(connection, ("Olive Oil", 66.12, 19))
    # create_product(connection, ("Sunflower Oil", 88.36, 21))

    # change_price_quantity(connection, (78.45, 125, 9))

    # delete_products(connection, 18)

    # all_products(connection)

    # select_products_price_quantity(connection, 100, 5)

    print('done')
