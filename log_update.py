# importing required library
import base
import mysql.connector
from datetime import datetime

def update_log(script_name,status,reason):

    print('connecting to mySql db!!')
    # connecting to the database
    try:
        dataBase = mysql.connector.connect(
            host="irisetl-db.mysql.database.azure.com",
            user="increff_root",
            passwd="smartfashion@123",
            database="irisx-etl-training")
        cursorObject = dataBase.cursor()
        sql = "INSERT INTO toylogs (script_name, run_time, status, reason) VALUES (%s, %s, %s, %s)"
        val = (script_name, str(datetime.utcnow()), status, reason)

        # preparing a cursor object
        cursorObject.execute(sql, val)
        dataBase.commit()

        # disconnecting from server
        dataBase.close()

        print('logs updated succesfully')

    except Exception as log_error:
        print(log_error)
        base.driver.quit()

