# Log-Analysis-Udacity-Project

I learned how to build a reporting tool that prints out reports (in plain text) based on the data in the database. Interacted with a live database both from the command line and from the python code. This project is a part of the Udacity's Full Stack Web Developer Nanodegree.

## Required Libraries and Dependencies
The project code requires the following software:

- Python 3.7.2
- psycopg2 2.7.6 
- PostgreSQL 11
 

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
5. Download the `newsdata.sql` database file [here](https://www.dropbox.com/s/2g0si3zlylowwb9/newsdata.sql?dl=0) and move it to the folder you've selected. 

## How to run the project
Open the text-based interface for your operating system (e.g. the terminal window in Linux, the command prompt in Windows) and navigate to the project directory. Once the VM has been installed, run `vagrant up` to start the machine.
Then run `vagrant ssh` to log in. (The SSH session can be terminated with CTRL+D.)

## Populate the database
You can use the following command:
`psql -d news -f newsdata.sql` to load the data and create the tables.



## How to run the report
- Ensure you have the 'news' database in your current working directory.
- In your Terminal, run psql news to access the database.
- Create the following views.

### For *Top Three Articles*:
```sh
CREATE VIEW article_views AS SELECT substring(path, 10) AS articles, count(*) AS views
    FROM log
    WHERE status = '200 OK' AND path LIKE '%/article/%'
    GROUP BY articles
    ORDER BY views desc;
```    
### For *Most Popular Authors*:
 ```sh
 CREATE VIEW author_views AS SELECT articles.author, article_views.views
    FROM articles, article_views
    WHERE articles.slug = article_views.articles;
```
### For *Days Where Errors Exceeded 1% of Total Views*:
```sh
 CREATE VIEW request_errors AS SELECT date(time) AS date, count(*) AS errors
    FROM log
    WHERE status LIKE '%404%'
    GROUP BY date
    ORDER BY errors desc;
```
```sh
 CREATE VIEW total_requests AS SELECT date(time) AS date, count(*) AS requests
    FROM log
    GROUP BY date
    ORDER BY requests desc;
```
```sh
 CREATE VIEW request_error_rate AS SELECT total_requests.date, request_errors.errors/total_requests.requests::float * 100 AS error_rate
    FROM total_requests, request_errors
    WHERE total_requests.date = request_errors.date;
```
- Exit `psql` by Ctrl+D.
- Run: `python3 newsdata.py` to run the reporting tool.
- You should see the following output:
Top Three Articles by Page View

Candidate is jerk, alleges rival - 338647
Bears love berries, alleges bear - 253801
Bad things gone, say good people - 170098

Most Popular Authors Based on Total Article Views

Ursula La Multa - 507594
Rudolf von Treppenwitz - 423457
Anonymous Contributor - 170098
Markoff Chaney - 84557

Days Where Errors Exceeded 1% of Total Views

2016-07-17 - 2.2626862468
