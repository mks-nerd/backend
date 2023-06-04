from tests import client

payload: dict = {
    "name": "professional",
    "menu": [
        {"name": "Home", "endpoint": "/home"},
        {"name": "Learn", "endpoint": "/learn"},
        {"name": "Task", "endpoint": "/task"},
        {"name": "Upload To SQL", "endpoint": "/upload_to_sql"},
        {"name": "About", "endpoint": "/about"},
        {"name": "Login", "endpoint": "/login"},
        {"name": "Logout", "endpoint": "/logout"},
    ],
    "about": """Hi This is Mohan Sahu,\n
    I'm a Data Analyst by profession and 
    I mostly work with Python, Pandas, 
    Numpy, SQL, Excel & Power Query. I'm 
    also learning Web Development and 
    using Flask & PostgreSQL in backend 
    and JavaScript, HTML & CSS in frontend. 
    This webiste is an example of my journey 
    to Web Deveopment.""",
    "skills": [
        "Python",
        "Flask",
        "Numpy",
        "Pandas",
        "Sql",
        "PostgreSQL",
        "MySQL",
        "SqLite",
        "JavaScript",
        "Apps Script",
        "JQuery",
        "Excel",
        "Power Query",
        "Periscope",
        "Redash",
        "Ubuntu",
        "Crystal Report",
        "Nano",
        "Web Hosting",
    ],
    "hobbies": [
        "Playing Chess & Sudoku",
        "Programming",
        "Cooking",
        "Biking",
        "Learning Things related to Space & Tech",
    ],
}


def test_add_home():
    response = client.post(
        "/home/add_home",
        json=payload,
    )
    assert response.status_code == 200
    assert response.json() == payload


def test_get_home():
    response = client.get(
        "/home/get_home",
        params={"home_name": "professional"},
    )
    assert response.status_code == 200
    assert response.json() == [payload]


def test_delete_home():
    response = client.post(
        "/home/delete_home",
    )
    assert response.status_code == 200
    assert response.json() == "success"
