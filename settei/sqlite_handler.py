from sqlite3 import connect,Connection,Cursor,Row

class SqliteHandler():
    def __init__(self):
        self.connection: Connection = connect("settei")
        # self.connection.row_factory = Row
        self.cursor: Cursor = self.connection.cursor()

    def create(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS table_configs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id_package INTEGER,
                            robot TEXT,
                            branch TEXT,
                            filename TEXT,
                            data TEXT,
                            datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS table_idpackages (
                                id_package INTEGER PRIMARY KEY AUTOINCREMENT,
                                package TEXT
                            )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS table_configlist (
                                id_package INTEGER,
                                branch  TEXT,
                                filename TEXT
                            )''')

    def insert_idPackage(self,package):
        self.cursor.execute(f'''INSERT INTO table_idpackages (package)
                                SELECT '{package}'
                                WHERE NOT EXISTS (
                                    SELECT * FROM table_idpackages WHERE 
                                    package='{package}'
                                )
                            ''')
        self.connection.commit()
    
    def insert(self,package,robot,branch,filename,data):
        self.cursor.execute(f'''INSERT INTO table_configs (id_package,robot,branch,filename,data)
                                VALUES ( (SELECT id_package 
                                FROM table_idpackages WHERE package='{package}'),
                                '{robot}','{branch}','{filename}','{data}')
                            ''')
        self.connection.commit()

    def insert_listconfig(self,package,branch,filename):
        id_package = f'''SELECT id_package 
                        FROM table_idpackages WHERE package='{package}' '''

        self.cursor.execute(f'''INSERT INTO table_configlist (id_package,branch,filename)
                                SELECT ({id_package}),'{branch}','{filename}'
                                WHERE NOT EXISTS (
                                    SELECT * FROM table_configlist WHERE
                                    id_package=({id_package}) AND
                                    branch = '{branch}' AND
                                    filename = '{filename}'
                                )
                            ''')
        self.connection.commit()

    def load_filename(self,package,branch):
        self.cursor.execute(f'''SELECT filename FROM table_configlist INNER JOIN table_idpackages 
                                ON table_configlist.id_package=table_idpackages.id_package WHERE
                                package = '{package}' AND
                                branch = '{branch}'
                            ''')
        return self.cursor.fetchall()

    def load_data(self,package,robot,branch,filename)->str:
        self.cursor.execute(f'''
                            SELECT data FROM table_configs INNER JOIN table_idpackages
                            ON table_configs.id_package = table_idpackages.id_package
                            WHERE package = '{package}' AND
                            robot = '{robot}' AND
                            branch = '{branch}' AND
                            filename = '{filename}' ORDER BY id DESC LIMIT 1''')
        return self.cursor.fetchone()

    def load_listpackage(self):
        self.cursor.execute(f'''
                            SELECT * FROM table_idpackages ''')
        return self.cursor.fetchall()

    def select_data(self,package,robot,branch,filename):
        self.cursor.execute(f'''
                            SELECT id,filename,datetime FROM table_configs 
                            INNER JOIN table_idpackages
                            ON table_configs.id_package = table_idpackages.id_package
                            WHERE package = '{package}' AND
                            robot = '{robot}' AND
                            branch = '{branch}' AND
                            filename = '{filename}'
                            ''')
        return self.cursor.fetchall()

    def select_data_from_id(self,id):
        self.cursor.execute(f'''
                            SELECT data FROM table_configs 
                            WHERE id = {id}
                            ''')