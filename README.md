# WikiCow
**Clara Mohri, William Lu, Alexander Liu, Jiajie Mai**

## Things we still have to do: 
1. Check if a user has already contributed to a story.
2. Activate ability to contribute to a story.

## Description:
WikiCow has created a collaborative story telling website. On the website, users can create new stories, or contribute to old ones. When contributing to old stories, the user can only see the most recent contribution. Once they contribute, then they will be able to view the entire story. 

## User Instructions to Access the Website: 
1. Clone our repo: 
``` 
$ git clone git@github.com:WilliamLu0211/WikiCow.git 
```
2. Change directory in your newly-cloned repo:
```
$ cd WikiCow
```
3. Run the file db_builder.py:
```
$ python db_builder.py
```
4. Activate your virtual environment: 
If your virtual environment exists in your home directory, then: 
```
$ . ~/<venv>/bin/activate
```
5. Run app.py: 
```
$ python app.py
```
6. Your console will tell you where the app is running. Open this IP address to access the website.

## Website Usage: 
- If you do not have an account, then create one by clicking the "Sign Up" button. 
You'll be asked to create a username and password. There is also a security question/answer to fill out, for security reasons.
- Once you have an account, then you can log in.
- Behold the a **landing page**:
  Here you'll see... 
  -  a list of stories that you can contribute to. As such, you'll only get to see the most recent contribution until you    contribute to the story
  - stories that you have already contributed to. As such, you get to view the entire story. You can also no longer contribute to these stories.
  - a "new story" button: You can create a new story too if you'd like.
  - a "logout" button: So you can log out when you're done using the website.

## How We Store Data:
Data is stored in a SQLite3 database, which is created upon running ```db_builder.py```. 

We have two tables in this database. 

One table stores user informations. It looks like this: 

| Username |  Password |  Security question | Security answer |
|----------|-----------|--------------------|-----------------|
|          |           |                    |                 |

Another table stores story contribution information. It looks like this: 

| Story | Contributor | Timestamp | Contribution |
|-|-|-|-|
|||||

## Formatting our Website:
Our templates directory within our repo stores templates for the website. These templates allow us to show relevant and customized information to users. 

## Libraries We Used:
- flask:
  - Flask, render_template, request, session, url_for, redirect functions for app functionality.
- sqlite3:
  - to connect the database to our app.
- os: 
  - to create a random secret key for user sessions
- datetime:
  - to access the current time in format: yyyy-mm-dd hh:mm:ss


 
