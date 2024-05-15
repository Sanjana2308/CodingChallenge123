class PropertyUtil:
    def get_DBconn():
        server_name = "DESKTOP-NG62K12\SQLEXPRESS"
        database_name = "HexawareOrdersDB"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        return conn_str