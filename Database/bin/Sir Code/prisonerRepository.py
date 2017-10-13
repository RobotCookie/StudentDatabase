import sys
sys.path.insert(0, './sqlite')

import helpers
from prisoner import Prisoner

class PrisonerRepository:
    
    def __init__(self, dbFile):
        self.dbFile = dbFile

        sql_create_prisoners_table = """ CREATE TABLE IF NOT EXISTS prisoners (
                                            id integer PRIMARY KEY,
                                            title text NOT NULL,
                                            first_name text NOT NULL,
                                            middle_name text NOT NULL,
                                            last_name text NOT NULL,
                                            sentenceType text NOT NULL
                                    ); """

        ## create the database connection
        conn = helpers.create_connection(dbFile)

        ## create the prisoners table if needed
        helpers.create_table(conn, sql_create_prisoners_table)
  
        ## close the connection
        conn.close()
        
    def create(self, prisoner):

        ## define the insert sql 
        sql_insert_prisoner = """ INSERT INTO prisoners (title, first_name, middle_name, last_name, sentenceType)
                                  VALUES (?, ?, ?, ?, ?); """

        try:
            ## create the database connection
            conn = helpers.create_connection(self.dbFile)

            ## open the cursor
            c = conn.cursor()

            ## execute the insert with the prisoner object
            c.execute(sql_insert_prisoner,
                      (prisoner.title, prisoner.firstname, prisoner.middlename, prisoner.lastname, prisoner.sentenceType))

            ## set the prisoner id
            prisoner.id = c.lastrowid

            ## commit
            conn.commit()
            
            ## close the connection
            conn.close()

            return prisoner
        
        except Error as e:
            print(e)

    def read(self, prisonerId):
        ## define the select sql
        sql_select_prisoner = """ SELECT * FROM prisoners WHERE id = ? """

        try:
            ## create the database connection
            conn = helpers.create_connection(self.dbFile)

            ## open the cursor
            c = conn.cursor()

            ## execute the sql
            c.execute(sql_select_prisoner, (prisonerId,))

            ## fetch one row from the database
            row = c.fetchone()[0]

            ## map the row to a Prisoner object
            p = Prisoner()
            p.id            = row[0]
            p.title         = row[1]
            p.firstname     = row[2]
            p.middlename    = row[3]
            p.lastname      = row[4]
            p.sentenceType  = row[5]

            ## commit
            conn.commit()
            
            ## close the connection
            conn.close()

            return p
        
        except Error as e:
            print(e)

    def readall(self):

        ## define the select sql
        sql_select_prisoner = """ SELECT * FROM prisoners """

        ## define a list for the prisoners
        prisoners = []
        
        try:
            ## create the database connection
            conn = helpers.create_connection(self.dbFile)

            ## open the cursor
            c = conn.cursor()

            ## execute the sql
            c.execute(sql_select_prisoner)

            ## fetch all the rows
            rows = c.fetchall()

            ## loop through all rows and create a prisoner object
            for row in rows:
                p = Prisoner()
                p.id            = row[0]
                p.title         = row[1]
                p.firstname     = row[2]
                p.middlename    = row[3]
                p.lastname      = row[4]
                p.sentenceType  = row[5]
                prisoners.append(p)

            ## commit
            conn.commit()
            
            ## close the connection
            conn.close()

            return prisoners

        except Error as e:
            print(e)

    def delete(self, prisonerId):
        ## define the delete sql
        sql_delete_prisoner = """ DELETE FROM prisoners WHERE id = ?; """

        try:
            ## create the database connection
            conn = helpers.create_connection(self.dbFile)

            ## open the cursor
            c = conn.cursor()

            ## execute the delete with the prisoner id
            c.execute(sql_delete_prisoner, (prisonerId,))

            ## commit
            conn.commit()
            
            ## close the connection
            conn.close()
        
        except Error as e:
            print(e)
