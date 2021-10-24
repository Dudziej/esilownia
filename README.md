# E-siłownia
(description of our project...)

## Getting started:

Create virtual environment: 
```python -m venv venv```

Install requirements.txt: 
```python -m pip install -r requirements.txt```

## Start backend:

Activate virtual environment in /esilownia: 
```source venv/bin/activate```
and in venv:
```python3 manage.py runserver```

## Start frontend:

Install node packages in /esilownia/frontend/esilownia:
```npm install```

Start react-app in /esilownia/frontend/esilownia:
```npm start```

## Updating

Update requirements.txt:
```python -m pip freeze > requirements.txt```

### Notes

Generate tokens for all users
```for user in User.objects.all(): Token.objects.get_or_create(user=user)```
