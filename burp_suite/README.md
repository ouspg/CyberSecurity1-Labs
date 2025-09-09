# SquadSync

SquadSync is an employee management system built using Flask, SQLAlchemy, Chart.js 4.4.1 and, Grid.js. 

## Modifications

The app has been modified in some places to add custom dynamic flags and challenge data for the CyberSecurity1 Course.

### Placeholder Flags and Challenges

Placeholder flags have been added in the `views.py`, `api.py` and `__init__.py` files for different challeneges. These flags are meant to be replaced by the flag generator and injector during lab setup.


### Employee Data

Some data has also been provisioned such as user `nicole` and `Manager` position during application startup in `__init__.py` in the `seed_users()` method.

### Challenges

This lab includes the following challenges and modifications made to accomodate for the challenges:

1. **Sitemap.xml:**

    A new route has been added `sitemap.xml` in `views.py` that renders the sitemap with a placeholder flag.

1. **Brute Force:**

    User `nicole` with easy to guess password seeded during application startup. Placeholder flag placed in user dashboard at route `<username>`, rendered in template.

1. **Decode:**

    During data seeding, a `Manager` data is seded with placeholder flag. This will be replaced by encoded flag by the flag generator app.

1. **Headers:**

    A custom header is sent in response by api `<username>/positions/data` in `api.py`.

## Setup and Installation 
Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip3 install -r requirements.txt
```

## Running the App
```bash
python run.py
```

## Viewing the App
Go to `http://127.0.0.1:5000`

## Database Diagram
![Database Diagram](/SquadSync%20Screenshots/databaseDiagram.png)

## Javascript Libraires Used
* [Chart.js](https://www.chartjs.org/docs/latest/)
* [Grid.js](https://gridjs.io/)
* [FullCalendar](https://fullcalendar.io/)

## ScreenShots

### Home Page
![Home Page](/SquadSync%20Screenshots/home%20page.png)

### Register Page
![Register Page](/SquadSync%20Screenshots/register.png)

### Dashboard
![Dashboard](/SquadSync%20Screenshots/dashboard.png)

### Employees Page
![Employees Page](/SquadSync%20Screenshots/employees.png)

### Calendar Page
![Calendar Page](/SquadSync%20Screenshots/calendar.png)

---

**Credits:** AaronSinn