import psycopg2  #these are imported
import psycopg2.extras as ext 

def run_sql(sql, values = None): #creating a function with parameters to send to database
    conn = None         #this is none meaning you can leave it empty and stil run, doesnt need value
    results = []

    try:
        conn=psycopg2.connect("dbname='music_collection'") #this provides a connection to the database task_manager
        cur = conn.cursor(cursor_factory=ext.DictCursor)  ##cursor lets you piont at specific database info, this converts databse tuple return as python dict
        cur.execute(sql, values) #cursor/execute function,passing in values
        conn.commit()     #this makes the changes permanent
        results = cur.fetchall() #variable is cursor function
        cur.close()      #closes cursor object
    except (Exception, psycopg2.DatabaseError) as error: #
        print(error)
    finally:
        if conn is not None:
            conn.close() #closes the connection
    return results