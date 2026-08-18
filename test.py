import pyodbc

server = r"JAYAPRAKASHDE\SQLEXPRESS"
database = "AIProjectMentor"

try:
    connection = pyodbc.connect(
        f"DRIVER={{SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    print("✅ SQL Server connection successful!")

    cursor = connection.cursor()
    cursor.execute("SELECT @@VERSION")

    row = cursor.fetchone()

    print("\nSQL Server Version:")
    print(row[0])

    connection.close()
    print("\nConnection closed.")

except pyodbc.Error as e:
    print("❌ Connection failed!")
    print(e)