# Google-Calendar-Api

## Steps to run the project:

1. After cloning, make sure you have virtualenv installed. Then run the following command:

```
python3 -m venv myenv   
```
2. Activate the virtualenv:

```
source myenv/bin/activate
```

3. Install all packages using: 
``` 
pip install -r requirements.txt 
```

4. Cd into the folder: 
``` 
cd calendarApi/ 
```

5. Perform all migrations: 
``` 
python3 manage.py migrate
```

6. Run server: 
``` 
python3 manage.py runserver 8080
```

7. Open browser and go to the following url: http://127.0.0.1:8080/rest/v1/calendar/init

