# Log-Analysis-Udacity-Project

I learned how to build a reporting tool that prints out reports (in plain text) based on the data in the database. Interacted with a live database both from the command line and from the python code. This project is a part of the Udacity's Full Stack Web Developer Nanodegree.

## Required Libraries and Dependencies
The project code requires the following software:

*Python 3.7.2
*psycopg2 2.7.6
*PostgreSQL 11
You can run the project in a Vagrant managed virtual machine (VM) which includes all the required dependencies (see below to learn how to install the VM). 

## Project Requirements
Reporting tools should answer the following questions about a PostgreSQL database containing the logs of a fictional newspaper website:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


## Install the virtual machine
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.

1. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Download and install [Vagrant](https://www.vagrantup.com/downloads.html).
3. Select a folder on your PC from which you'd like to run the reporting tool.
4. Fork and clone this repository into the folder you've just selected.

## How to run the project:
1. vagrant up to start up the VM.
2. vagrant ssh to log into the VM.
3. cd /vagrant to change to your vagrant directory.
4. psql -d news -f newsdata.sql to load the data and create the tables.
5. create the views below
6. python3 newsdata.py to run the reporting tool.

Views Used

CREATE VIEW article_views AS SELECT substring(path, 10) AS articles, count(*) AS views
    FROM log
    WHERE status = '200 OK' AND path LIKE '%/article/%'
    GROUP BY articles
    ORDER BY views desc;
    
 CREATE VIEW author_views AS SELECT articles.author, article_views.views
    FROM articles, article_views
    WHERE articles.slug = article_views.articles;
    
 CREATE VIEW request_errors AS SELECT date(time) AS date, count(*) AS errors
    FROM log
    WHERE status LIKE '%404%'
    GROUP BY date
    ORDER BY errors desc;
    
 CREATE VIEW total_requests AS SELECT date(time) AS date, count(*) AS requests
    FROM log
    GROUP BY date
    ORDER BY requests desc;
    
 CREATE VIEW request_error_rate AS SELECT total_requests.date, request_errors.errors/total_requests.requests::float * 100 AS error_rate
    FROM total_requests, request_errors
    WHERE total_requests.date = request_errors.date;
