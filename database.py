from utils import region_pop, ctry_pop
from config import conn, create_db, create_table, show_tables, insert_into_table, select_records



def main():
    """Create connection, and tables"""
    DB_NAME = 'World_population'
    sql_query = f"CREATE SCHEMA IF NOT EXISTS {DB_NAME}"
    try:
        # create DB
        create_db(DB_NAME, sql_query)
    except Exception as e:
        print(f"Error message: {e}")
    
    # create a table Region_Population
    table_name = 'Region_Population'
    sql_query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name}
                        (
                            ID INT NOT NULL,
                            Variant VARCHAR(100),
                            Region VARCHAR(100),
                            Notes VARCHAR(100),
                            Country_code INT,
                            Type VARCHAR(100),
                            Parent_code INT,
                            Years DATE,
                            Population_Thousands INT                    
                        )
                """
    try:
        create_table(table_name, sql_query)
    except Exception as e:
        print(f"Error message: {e}")
    # query
    sql_query = f"""
                    INSERT INTO {table_name}
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """ 
    # create df
    region_population = region_pop()
    # Add all the rows to a list
    val_reg_pop = []
    for row in region_population.itertuples():
        val_reg_pop.append(row[1:])
    try:
        # populate table
        insert_into_table(table_name, sql_query, val_reg_pop)
    except Exception as e:
        print(f"Error message: {e}")
    # create a table Countries_population
    table_name = 'Countries_population'
    sql_query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name}
                        (
                            ID INT NOT NULL,
                            Variant VARCHAR(100),
                            Country VARCHAR(100),
                            Country_code INT,
                            Type VARCHAR(100),
                            Parent_code INT,
                            Years DATE,
                            Population_Thousands INT                    
                        )
                """
    
    try:
        # create a table Countries_population
        create_table(table_name, sql_query)
    except Exception as e:
        print(f"Error message: {e}")

    sql_query = f"""
                    INSERT INTO {table_name}
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """ 
    # create df
    countries_population = ctry_pop()
    # Add all the rows to a list
    val_ctry_pop = []
    for row in countries_population.itertuples():
        val_ctry_pop.append(row[1:])
    try:
        # populate table
        insert_into_table(table_name, sql_query, val_ctry_pop)
    except Exception as e:
        print(f"Error message: {e}")

    # show tables
    show_tables()


if __name__ == "__main__":
    main()

    
    sql_query = """
                    SELECT * FROM region_population
                        LIMIT 5
                """
    try:
       # select some records
       select_records(sql_query)
    except Exception as e:
        print(f"Error message: {e}")
    # close connection
    conn.close()
    