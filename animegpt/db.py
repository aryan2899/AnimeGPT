from __future__ import annotations
import mysql.connector 
from typing import Union
from numpy.typing import NDArray

class DatabaseClient():
    def __init__(self, host: str, username: str, password: str, db: str) -> DatabaseClient:
        """
        Constructor for DB Class. Acts as a MYSQL Wrapper to interact with a specific MYSQL DB
        

        Args:
            host (str): MYSQL sever hostname
            username (str): MYSQL server username
            password (str): MYSQL server password
            db (str): Name of MYSQL Database to interact with 

        Returns:
            DB: DB object 
        """
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.connection = None
        self.cursor = None
    
    def _connection(self):
        """
        Creates a new connection object to MYSQL DB
        """
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                username = self.username,
                password = self.password,
                db = self.db)
        except mysql.ConnectionError as e:
            print(f'Error in connecting, {e}')
        
    def _cursor(self):
        """
        Creates a new cursor object for a MYSQL connection

        Raises:
            ValueError: If no MYSQL connection exsits
        """
        if self.connection == None:
            raise ValueError('No SQL Connection created, please create a connection first')
        
        self.cursor = self.connection.cursor()
        
    def connect(self):
        """
        Establishes a new connection and cursor to a MYSQL DB
        """
        self._connection()
        self._cursor()
    
    def close(self):
        """
        Closes a MYSQL DB connection and cursor
        """
        try:
            self.cursor.close()
        except:
            self.cursor = None
        try:
            self.connection.close()
        except:
            self.connection = None
        
        self.cursor = None
        self.connection = None
        
    def commit(self):
        """
        Commit a query change to MYSQL Database

        Raises:
            ValueError: If there is no MYSQL connection open
        """
        if self.connection == None:
            raise ValueError('No SQL Connection created, please create a connection first')
        
        self.connection.commit()
        
    def query(self, query: str, params: Union[tuple, list, NDArray] = None, many: bool = False):
        """
        Runs a MYSQL Query, requires a prior established MYSQL Connection and Cursor

        Args:
            query (str): Query to be run
            params (Union[tuple, list, NDArray], optional): A tuple containing values. Defaults to None.
            many (bool, optional): True if many params, false if only 1 set of params. Defaults to False.
        """
        if many == True:
            self.cursor.executemany(query, params)
        else:
            self.cursor.execute(query, params)
    