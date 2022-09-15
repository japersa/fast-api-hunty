# fast-api-hunty

#### Description:

fast-api-hunty is an api designed to query job vacancies and users in a test database. This was developed as a technical test for the company Hunty.

- Retrive all the users, companies, skills or vacancies
- Retrive specific users, companies, skills or vacancies
- Retrive specific users, companies, skills or vacancies

#### Entity relationship model:

<img src="https://github.com/japersa/fast-api-hunty/blob/9592bcedd8024cc5077c148efce6192cf698c166/model.png" />

#### Installation:

- Clone this repository: `git@github.com:japersa/fast-api-hunty.git"`
- Access fast-api-hunty: `cd fast-api-hunty`
- install dependencies: `poetry install --no-dev --no-root`
- Activate local server: `uvicorn main:app --reload `
- Open the web app in a browser: `http://127.0.0.1:8000/`

#### Build docker:

- `docker build -t fast-api-hunty .`
- `docker run -it fast-api-hunty`

#### Documentation:

- Open the web app in a browser: `http://127.0.0.1:8000/docs` Or `http://127.0.0.1:8000/redoc`

#### Heroku deploy:

- Open the web app in a browser: `https://fast-api-hunty.herokuapp.com/`

#### Run test:

- `poetry run pytest`
