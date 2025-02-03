from django.db import connection

def check_audience_credentials(username, password):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM audience WHERE username = %s AND password = %s", [username, password])
        row = cursor.fetchone()

        count = row[0]
        if count > 0:
            return True  # Username and password exist in the database
        else:
            return False