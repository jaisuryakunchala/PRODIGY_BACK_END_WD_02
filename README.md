users_fastapi/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│
└──.env
└──requiremnts.txt
└── users.db   ← auto-created

above is the directory 
run command in folder terminal " uvicorn app.main:app --reload "
it run on " http://127.0.0.1:8000/docs  "
you can see the posted data on " http://127.0.0.1:8000/users "
