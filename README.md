# CONTENTS OF THIS FILE
## Introduction
Requirements
Next steps
INTRODUCTION
This project consists of a home page ('/'), a new page ('/new_page') and an administration page ('/administration'). From home page, customers are redirected to the new page, where they can post complains and choose the date and time of callback.They cannot chose a date on Saturdays and Sundays. They have no links redirecting them to the administration page.

Administration page displays customers' posts (sorting them by the date posted), has options of editing those posts, as well as hiding them from the list of outstanding callbacks (they are not deleted from the database).

## REQUIREMENTS
This project was done in web framework Flask, written in Python, using Visual Studio code. 1) Install additional packages with command: pip install -r requirements.txt. 2) command: flask run This project requires the following modules, which are not included in flask: flask_sqlalchemy, flask_wtf, flask_moment, flask_bootstrap, wtforms

## NEXT STEPS
1) Improving the design of the home page 2) Making the option of scheduling callback on Saturdays 3) Creating a table for the administration page, which would be sortable by different columns 4) Adding flash messages 5) Refactoring code, so that the code is separated into several scripts 6) API and unit testing
