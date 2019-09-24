import sqlite3
import os.path
#from .vulnerability import *

class Freenas_config():
    def __init__(self):
        self.conn= None
        self.c = None

    def open_config_db(self):
        
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        #return c

    def get_ssh_passwordauth(self):
        self.c.execute("SELECT ssh_passwordauth FROM services_ssh")
        result = self.c.fetchone()
        return result

    def print_curs(self):
        return type(self.c)

    def close_config_db(self):
        self.conn.close()

if __name__ == "__main__":

    scan = Freenas_config()
    scan.open_config_db()
    curs = scan.print_curs()
    print(curs)
    passwdauthenabled_check = scan.get_ssh_passwordauth()
    print(passwdauthenabled_check)
    scan.close_config_db()
