
user = {
    "name": "Gustavo",
    "age": 30,
    "is_active": True,
    "courses": ["Python", "JavaScript", "Django"],
    'settings': {
        'theme': 'dark',
        'notifications': True
    }
}

print(list(user.keys()))
print(list(user.values()))
print(list(user.items()))