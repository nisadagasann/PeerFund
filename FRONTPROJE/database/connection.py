import pyodbc

def get_connection():
    try:
        connection = pyodbc.connect(
            r"Driver={ODBC Driver 18 for SQL Server};"
            r"Server=LAPTOP-8CIIC8KV\SQLEXPRESS;"  # Sunucu adınız
            "Database=NewPeerFund;"  # Veritabanı adınız
            "Trusted_Connection=yes;"  # Windows Authentication
            "TrustServerCertificate=yes;"  # Sertifika doğrulama hatasını geç
        )
        print("Veritabanı bağlantısı başarılı!")
        return connection
    except pyodbc.Error as e:
        print("Veritabanı bağlantı hatası:", e)
        return None

if __name__ == "__main__":
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sys.tables")
        for row in cursor.fetchall():
            print("Tablo:", row.name)
        conn.close() 