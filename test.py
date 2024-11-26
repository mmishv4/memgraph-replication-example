from neo4j import GraphDatabase

WRITE_URI = "bolt://localhost:7692"
READ_URI = "bolt://localhost:7693"


def execute_query(uri, query):
    driver = GraphDatabase.driver(uri, auth=("memgraph", "password"))
    session = driver.session()
    try:
        result = session.run(query)
        return result.data()
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        session.close()


def execute_write_query():
    query = "CREATE (a:Test {name: 'Test Write'}) RETURN a"
    execute_query(WRITE_URI, query)
    print("Write query executed successfully.")


def execute_read_query():
    query = "MATCH (a:Test) RETURN a LIMIT 1"
    result = execute_query(READ_URI, query)
    print("Read query executed successfully.")
    for record in result:
        print(record)


if __name__ == "__main__":
    execute_write_query()
    execute_read_query()
