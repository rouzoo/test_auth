This is simple social authentification with Google and Github account.

Run: 
1. pip install -r requirements.txt
2. add your auth tokens in /testauth/tokens.py
3. make migrations:
		python manage.py makemigrations googleauth
		python manage.py migrate
4. run app : python manage.py runserver
