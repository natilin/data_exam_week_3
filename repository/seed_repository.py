def is_table_exist(table):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = %s
                )
                """, (table,))
            res = cursor.fetchone()
    return res.get("exist")