from requests import get, post, delete

# Testing GET
print(get('http://localhost:5000/api/news').json())
# Отдаст все новости

print(get('http://localhost:5000/api/news/1').json())
# Отдаст новость с id = 1

print(get('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

print(get('http://localhost:5000/api/news/q').json())
# отработает @app.errorhandler(404)

# Testing POST

print(post('http://localhost:5000/api/news').json())
# Зайдем в create_news и после отработает @app.errorhandler(400)

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())
# Отработает return jsonify({'error': 'Bad request'}) из if в create_news

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())

# Testing DELETE
print(delete('http://localhost:5000/api/news/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/news/1').json())
# Удалит запись с id=1, если она есть


print(delete('http://localhost:5000/api/news/q').json())
# отработает @app.errorhandler(404)
