import sqlite3

def create_connection(db_file):
    """
    Create a database connection to SQLite database or PostgreSQL
    """
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def create_table(conn):
    """
    Create a metadata table to store document information
    """
    try:
        sql_create_metadata_table = """
        CREATE TABLE IF NOT EXISTS document_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            creation_date TEXT,
            file_path TEXT NOT NULL
        );
        """
        conn.execute(sql_create_metadata_table)
        print("Document metadata table created.")
    except sqlite3.Error as e:
        print(e)

def insert_metadata(conn, title, author, creation_date, file_path):
    """
    Insert document metadata into the table
    """
    sql = ''' INSERT INTO document_metadata(title,author,creation_date,file_path)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (title, author, creation_date, file_path))
    conn.commit()
    print("Metadata inserted successfully")

# Example usage:
if __name__ == '__main__':
    db_file = 'document_metadata.db'
    conn = create_connection(db_file)
    
    if conn is not None:
        create_table(conn)
        # Insert some example metadata
        insert_metadata(conn, 'Sample Document', 'John Doe', '2024-10-01', 'web_data.txt')
        conn.close()
