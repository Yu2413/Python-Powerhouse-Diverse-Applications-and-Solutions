import pymysql

# Database connection details
host = "localhost"
user = "your_username"
password = "your_password"
database = "your_database"

# Function to establish a database connection
def connect_to_database():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected to the database successfully!")
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to create a table
def create_table(connection):
    try:
        with connection.cursor() as cursor:
            sql = """
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                position VARCHAR(100) NOT NULL,
                salary DECIMAL(10, 2) NOT NULL
            )
            """
            cursor.execute(sql)
            connection.commit()
            print("Table 'employees' created successfully!")
    except pymysql.Error as e:
        print(f"Error creating table: {e}")

# Function to insert data into the table
def insert_data(connection, name, position, salary):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, position, salary))
            connection.commit()
            print(f"Inserted data for {name} successfully!")
    except pymysql.Error as e:
        print(f"Error inserting data: {e}")

# Function to query all data from the table
def query_data(connection):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM employees"
            cursor.execute(sql)
            results = cursor.fetchall()
            print("Employees:")
            for row in results:
                print(row)
    except pymysql.Error as e:
        print(f"Error querying data: {e}")

# Function to update data in the table
def update_data(connection, employee_id, new_salary):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE employees SET salary = %s WHERE id = %s"
            cursor.execute(sql, (new_salary, employee_id))
            connection.commit()
            print(f"Updated salary for employee ID {employee_id} successfully!")
    except pymysql.Error as e:
        print(f"Error updating data: {e}")

# Function to delete data from the table
def delete_data(connection, employee_id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM employees WHERE id = %s"
            cursor.execute(sql, (employee_id))
            connection.commit()
            print(f"Deleted employee with ID {employee_id} successfully!")
    except pymysql.Error as e:
        print(f"Error deleting data: {e}")

# Main function to demonstrate the usage
def main():
    # Connect to the database
    connection = connect_to_database()
    if not connection:
        return

    try:
        # Create the table
        create_table(connection)

        # Insert some data
        insert_data(connection, "John Doe", "Software Engineer", 75000.00)
        insert_data(connection, "Jane Smith", "Data Scientist", 85000.00)

        # Query and display all data
        query_data(connection)

        # Update an employee's salary
        update_data(connection, 1, 80000.00)

        # Query and display all data after update
        query_data(connection)

        # Delete an employee
        delete_data(connection, 2)

        # Query and display all data after deletion
        query_data(connection)

    finally:
        # Close the database connection
        connection.close()
        print("Database connection closed.")

# Run the script
if __name__ == "__main__":
    main()