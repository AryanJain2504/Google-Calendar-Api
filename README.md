# Google-Calendar-Api

## Steps to run the project:

1. After cloning, make sure you have virtualenv installed. Then run the following command:

```
python3 -m venv myenv   
```
Activate the virtualenv:

```
source myenv/bin/activate

2. Cd into the folder: 
``` 
cd calendarApi/ 
```

3. Install all packages using: 
``` 
pip install -r requirements.txt 
```

4. Perform all migrations: 
``` 
python3 manage.py migrate
```

5. Run server: 
``` 
python3 manage.py runserver 8080
```

