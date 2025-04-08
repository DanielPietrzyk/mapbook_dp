users = [
    {"name": "Daniel", "location": "Łódź", "posts": 500},
    {"name": "Michał", "location": "Krasnystaw", "posts": 400},
    {"name": "Ksavier", "location": "Grudziądz", "posts": 300},
    {"name": "Damian", "location": "Kraków", "posts": 200},

]

for user in users:
    print(f"Twój znajomy {user['name']} z {user['location']}, opublikował {user['posts']} postów ")
