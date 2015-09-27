# api_jack
A simple API to list users in system

Developed using Python, Django, DRF and MySQL as Database

#List all users

curl --user remis:remis http://127.0.0.1:8000/users/

#GET a user by any field

curl --user remis:remis http://127.0.0.1:8000/users/?job=tester

#GET status system 

curl --user remis:remis http://127.0.0.1:8000/sys_status

#List files in a given folder 

curl --user remis:remis http://127.0.0.1:8000/files/?fpath=c:\lab
