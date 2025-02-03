from django.shortcuts import render, redirect
from main_app.audience.login import *
from main_app.audience.forms import *
from main_app.director.forms import *
from main_app.director.login import *
from main_app.database_manager.forms import *
from main_app.database_manager.login import *
from django.db import connection

# Main Homepage
def home(request):
    if request.method == "GET":
        #with connection.cursor() as cursor:
            #cursor.execute("INSERT INTO audience (username, password, name, surname) VALUES (%s, %s, %s, %s)", ["audience1", "audiencepass1", "a", "b"])
            #cursor.execute("INSERT INTO director (username, password, name, surname, platform_id, nation) VALUES (%s, %s, %s, %s, %s, %s)", ["kyle.balda","mynameiskyle9", "Kyle", "Balda", "10132", "German"])
            #cursor.execute("INSERT INTO database_manager (username, password) VALUES (%s, %s)", ["manager35", "managerpass35"])
            #cursor.execute("INSERT INTO movie (movie_id, movie_name, duration, director_username) VALUES (%s, %s, %s,%s)", ["20001", "Despicable Me", "2", "kyle.balda"])
            
        return render(request, 'home.html')

# Audience Login
def audience_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        check = check_audience_credentials(username, password)
        if(check):
            request.session['username'] = username
            return render(request, 'audience/audience_home.html')
        context = {'login_fail' : True, 'login_form' : audience_form()}
        return render(request, 'audience/audience_login.html', context)
    else:
        context = {'login_fail' : False, 'login_form' : audience_form()}
        return render(request, 'audience/audience_login.html')

# Audience Homepage after login
def audience_home(request):
    if request.method == "GET":
        username = request.session['username']
        return render(request, 'audience/audience_home.html', {'username' : username})
    
# Director Login
def director_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        check = check_director_credentials(username, password)
        if(check):
            request.session['username'] = username
            return render(request, 'director/director_home.html')
        context = {'login_fail' : True, 'login_form' : director_form()}
        return render(request, 'director/director_login.html', context)
    else:
        context = {'login_fail' : False, 'login_form' : director_form()}
        return render(request, 'director/director_login.html')

# Director Homepage after login
def director_home(request):
    if request.method == "GET":
        username = request.session['username']
        return render(request, 'director/director_home.html', {'username' : username})

# Database Manager Login
def manager_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        check = check_manager_credentials(username, password)
        if(check):
            request.session['username'] = username
            return render(request, 'manager/manager_home.html')
        context = {'login_fail' : True, 'login_form' : manager_form()}
        return render(request, 'manager/manager_login.html', context)
    else:
        context = {'login_fail' : False, 'login_form' : manager_form()}
        return render(request, 'manager/manager_login.html')

# Database Manager Homepage after login
def manager_home(request):
    if request.method == "GET":
        username = request.session['username']
        return render(request, 'manager/manager_home.html', {'username' : username})

# Deleting a director 
def delete_director(request):
    if request.method == "POST":
        username = request.POST.get("username")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM director WHERE username = %s", [username])
            row = cursor.fetchone()
            count = row[0]
            if count > 0:
                cursor.execute("DELETE FROM director WHERE username = %s", [username])
                context = {'delete_fail' : False}
                return render(request,'manager/delete_director.html', context)
            else:
                context = {'delete_fail' : True}
                return render(request,'manager/delete_director.html', context)
            
    if request.method == "GET":
        return render(request,'manager/delete_director.html')

# Deleting an audience 
def delete_audience(request):
    if request.method == "POST":
        username = request.POST.get("username")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM audience WHERE username = %s", [username])
            row = cursor.fetchone()
            count = row[0]
            if count > 0:
                cursor.execute("DELETE FROM audience WHERE username = %s", [username])
                context = {'delete_fail' : False}
                return render(request,'manager/delete_audience.html', context)
            else:
                context = {'delete_fail' : True}
                return render(request,'manager/delete_audience.html', context)
            
    if request.method == "GET":
        return render(request,'manager/delete_audience.html')

# Adding an audience 
def add_audience(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM audience WHERE username = %s", [username])
            row = cursor.fetchone()
            count = row[0]
            if count == 0 and username != "" and password != "":
                cursor.execute("INSERT INTO audience (username, password, name, surname) VALUES (%s, %s, %s, %s)", [username, password, name, surname])
                context = {'add_fail' : False}
                return render(request,'manager/add_audience.html', context)
            else:
                context = {'add_fail' : True}
                return render(request,'manager/add_audience.html', context)
            
    if request.method == "GET":
        return render(request,'manager/add_audience.html')

# Adding a director         
def add_director(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        nation = request.POST.get("nation")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM director WHERE username = %s", [username])
            row = cursor.fetchone()
            count = row[0]
            if count == 0 and username != "" and password != "" and nation != "":
                cursor.execute("INSERT INTO director (username, password, name, surname, nation) VALUES (%s, %s, %s, %s, %s)", [username, password, name, surname, nation])
                context = {'add_fail' : False}
                return render(request,'manager/add_director.html', context)
            else:
                context = {'add_fail' : True}
                return render(request,'manager/add_director.html', context)
            
    if request.method == "GET":
        return render(request,'manager/add_director.html')
    
# Updating platform of a director 
def update_platform(request):
    if request.method == "POST":
        username = request.POST.get("username")
        platform_id = request.POST.get("platform_id")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM director WHERE username = %s", [username])
            row = cursor.fetchone()
            count = row[0]
            if count > 0:
                cursor.execute("UPDATE director SET platform_id = %s WHERE username = %s", [platform_id, username])
                context = {'update_fail' : False}
                return render(request,'manager/update_platform.html', context)
            else:
                context = {'update_fail' : True}
                return render(request,'manager/update_platform.html', context)

    if request.method == "GET":
        return render(request,'manager/update_platform.html')

# Adding a movie
def add_movie(request):
    if request.method == "POST":
        username = request.session['username']
        movie_id = request.POST.get("movie_id")
        name = request.POST.get("name")
        duration = request.POST.get("duration")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM movie WHERE movie_id = %s", [movie_id])
            row = cursor.fetchone()
            count = row[0]
            if count == 0:
                cursor.execute("INSERT INTO movie (movie_id, movie_name, duration, director_username) VALUES (%s, %s, %s, %s)", [movie_id, name, duration, username])
                context = {'add_fail' : False}
                return render(request,'director/add_movie.html', context)
            else:
                context = {'add_fail' : True}
                return render(request,'director/add_movie.html', context)

    if request.method == "GET":
        return render(request,'director/add_movie.html')
    
# Adding predecessor to a movie
def add_predecessor(request):
    if request.method == "POST":
        movie_id1 = request.POST.get("movie_id1")
        movie_id2 = request.POST.get("movie_id2")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM movie WHERE movie_id IN (%s, %s)", [movie_id1, movie_id2])
            row = cursor.fetchone()
            count = row[0]
            if count == 2:
                cursor.execute("INSERT INTO predecessor (movie_id1, movie_id2) VALUES (%s, %s)", [movie_id1, movie_id2])
                context = {'add_fail' : False}
                return render(request,'director/add_predecessor.html', context)
            else:
                context = {'add_fail' : True}
                return render(request,'director/add_predecessor.html', context)

    if request.method == "GET":
        return render(request,'director/add_predecessor.html')
    
# Updating a movie name
def update_name(request):
    if request.method == "POST":
        username = request.session['username']
        movie_id = request.POST.get("movie_id")
        movie_name = request.POST.get("movie_name")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM movie WHERE movie_id = %s and director_username = %s", [movie_id, username])
            row = cursor.fetchone()
            count = row[0]
            if count > 0:
                cursor.execute("UPDATE movie SET movie_name = %s WHERE movie_id = %s", [movie_name, movie_id])
                context = {'update_fail' : False}
                return render(request,'director/update_name.html', context)
            else:
                context = {'update_fail' : True}
                return render(request,'director/update_name.html', context)

    if request.method == "GET":
        return render(request,'director/update_name.html')
    
# View Directors
def view_directors(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT username, name, surname, nation, platform_id FROM director")
            directors_data = cursor.fetchall()
            context = {'directors_data': directors_data}
            return render(request,'manager/view_directors.html', context)

# View Ratings
def view_ratings(request):
    if request.method == "POST":
        username = request.POST.get("username")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM audience WHERE username = %s", [username])
            row = cursor.fetchone()
            count = row[0]
            if count > 0:
                cursor.execute("SELECT movie.movie_id, movie_name, rating FROM rating INNER JOIN movie ON rating.movie_id = movie.movie_id WHERE username = %s", [username])
                rating_data = cursor.fetchall()
                context = {'view_fail': False, 'rating_data': rating_data}
                return render(request,'manager/view_ratings.html', context)
            else:
                context = {'view_fail': True}
                return render(request,'manager/view_ratings.html', context)
    if request.method == "GET":
        return render(request,'manager/view_ratings.html')
    
# View Movies
def view_movies(request):
    if request.method == "POST":
        username = request.POST.get("username")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM director WHERE username = %s", [username])
            row = cursor.fetchone()
            count = row[0]
            if count > 0:
                cursor.execute("SELECT movie_id, movie_name FROM movie WHERE director_username = %s", [username])
                movie_data = cursor.fetchall()
                context = {'view_fail': False, 'movie_data': movie_data}
                return render(request,'manager/view_movies.html', context)
            else:
                context = {'view_fail': True}
                return render(request,'manager/view_movies.html', context)
    if request.method == "GET":
        return render(request,'manager/view_movies.html')

# View average rating of a movie
def view_average_rating(request):
    if request.method == "POST":
        movie_id = request.POST.get("movie_id")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM movie WHERE movie_id = %s", [movie_id])
            row = cursor.fetchone()
            count = row[0]
            if count > 0:
                cursor.execute("SELECT average_rating FROM movie WHERE movie_id = %s", [movie_id])
                rating_data = cursor.fetchall()
                context = {'view_fail': False, 'rating_data': rating_data}
                return render(request,'manager/view_average_rating.html', context)
            else:
                context = {'view_fail': True}
                return render(request,'manager/view_average_rating.html', context)
    if request.method == "GET":
        return render(request,'manager/view_average_rating.html')
    
# View Directed Movies
def view_directed_movies(request):
    if request.method == "GET":
        username = request.session['username']
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM director WHERE username = %s", [username])
            row = cursor.fetchone()
            count = row[0]
            if count > 0:
                cursor.execute("SELECT movie_id, movie_name FROM movie WHERE director_username = %s ORDER BY movie_id", [username])
                movie_data = cursor.fetchall()
                updated_movie_data = []
                for data in movie_data:
                    cursor.execute("SELECT GROUP_CONCAT(movie_id2 SEPARATOR ', ') AS predecessors FROM predecessor WHERE movie_id1 = %s", [data[0]])
                    row = cursor.fetchone()
                    predecessors = row[0]
                    data += (predecessors,)
                    updated_movie_data.append(data)
                
                context = {'view_fail': False, 'movie_data': updated_movie_data}
                return render(request,'director/view_directed_movies.html', context)
            else:
                context = {'view_fail': True}
                return render(request,'director/view_directed_movies.html', context)
            
# View All Movies
def view_all_movies(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT movie_id, movie_name, surname, platform_name FROM movie INNER JOIN director ON director.username = movie.director_username INNER JOIN rating_platform ON rating_platform.platform_id = director.platform_id")
            movie_data = cursor.fetchall()
            updated_movie_data = []
            for data in movie_data:
                cursor.execute("SELECT GROUP_CONCAT(movie_id2 SEPARATOR ', ') AS predecessors FROM predecessor WHERE movie_id1 = %s", [data[0]])
                row = cursor.fetchone()
                predecessors = row[0]
                data += (predecessors,)
                updated_movie_data.append(data)
                
            context = {'view_fail': False, 'movie_data': updated_movie_data}
            return render(request,'audience/view_all_movies.html', context)

# Buy a Ticket
def buy_ticket(request):
    if request.method == "POST":
        username = request.session['username']
        session_id = request.POST.get("session_id")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM sessions WHERE session_id = %s", [session_id])
            row = cursor.fetchone()
            count = row[0]
            if count > 0:
                cursor.execute("SELECT movie_id FROM sessions WHERE session_id = %s", [session_id])
                row = cursor.fetchone()
                movie_id = row[0]

                cursor.execute("SELECT movie_id2 FROM predecessor INNER JOIN movie ON movie.movie_id = predecessor.movie_id2 WHERE movie_id1 = %s ORDER BY date", [movie_id])
                predecessor_data = cursor.fetchall()
            
                cursor.execute("SELECT movie_id FROM ticket INNER JOIN sessions ON ticket.session_id = session.session_id WHERE username = %s ORDER BY date", [username])
                watched_sessions = cursor.fetchall()

                predecessor_ids = [data[0] for data in predecessor_data]
                watched_session_ids = [data[0] for data in watched_sessions]

                len_a = len(predecessor_ids)
                len_b = len(watched_session_ids)

                i, j = 0, 0

                while i < len_a and j < len_b:
                    if predecessor_ids[i] == watched_session_ids[j]:
                        i += 1
                    j += 1

                if i == len_a:
                    cursor.execute("SELECT COUNT(*) FROM ticket WHERE session_id = %s", [session_id])
                    row = cursor.fetchone()
                    current = row[0]
                    cursor.execute("SELECT theatre_capacity FROM sessions INNER JOIN theatre ON sessions.theatre_id = theatre.theatre_id WHERE session_id = %s", [session_id])
                    row = cursor.fetchone()
                    capacity = row[0]

                    if capacity >= current:
                        cursor.execute("INSERT INTO ticket (username, session_id) VALUES (%s, %s)", [username, session_id])

                        context = {'purchase_fail': False}
                        return render(request,'audience/buy_ticket.html', context)
                    else:
                        context = {'purchase_fail': True}
                        return render(request,'audience/buy_ticket.html', context)
  
                else:
                    context = {'purchase_fail': True}
                    return render(request,'audience/buy_ticket.html', context)

            else:
                context = {'purchase_fail': True}
                return render(request,'audience/buy_ticket.html', context)
            
    if request.method == "GET":
        return render(request,'audience/buy_ticket.html')


# Bought Tickets
def bought_tickets(request):
    if request.method == "GET":
        username = request.session['username']
        with connection.cursor() as cursor:
            cursor.execute("SELECT movie.movie_id, movie.movie_name, session_id, rating, movie.average_rating FROM sessions INNER JOIN movie ON sessions.movie_id = movie.movie_id INNER JOIN rating ON rating.movie_id = movie.movie_id WHERE username = %s",[username])
            movie_data = cursor.fetchall()
        
            context = {'view_fail': False, 'movie_data': movie_data}
            return render(request,'audience/bought_tickets.html', context)
        

# View Audience
def view_audience(request):
    if request.method == "POST":
        movie_id = request.POST.get("movie_id")
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM movie WHERE movie_id = %s", [movie_id])
            row = cursor.fetchone()
            count = row[0]
            if count > 0:
                cursor.execute("SELECT audience.username, audience.name, audience.surname FROM audience INNER JOIN ticket ON audience.username = ticket.username WHERE movie_id = %s", [movie_id])
                movie_data = cursor.fetchall()
                context = {'view_fail': False, 'movie_data': movie_data}
                return
            else:
                context = {'view_fail': True}
                return render(request,'audience/bought_tickets.html', context)

    if request.method == "GET":
        return render(request,'director/view_audience.html')
