#!/usr/bin/env python3
"""Create a reporting tool that prints out reports."""
import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def popularArticles():
    """Prints a list of the 3 most popular articles of all time."""
    pg = connect()
    c = pg.cursor()
    c.execute("SELECT articles.title, article_views.views "
              "FROM articles, article_views "
              "WHERE articles.slug = article_views.articles LIMIT 3;")
    articles = c.fetchall()
    pg.close()
    for i in articles:
        print("%s - %s" % (i[0], i[1]))


def popularAuthors():
    """Prints a list of the most popular authors of all time."""
    pg = connect()
    c = pg.cursor()
    c.execute("SELECT authors.name, SUM(author_views.views) AS views "
              "FROM authors, author_views "
              "WHERE authors.id = author_views.author "
              "GROUP BY authors.name "
              "ORDER BY views DESC;")
    authors = c.fetchall()
    pg.close()
    for i in authors:
        print("%s - %s" % (i[0], i[1]))


def errors():
    """Prints the number of players currently registered."""
    pg = connect()
    c = pg.cursor()
    c.execute("SELECT date, error_rate "
              "FROM request_error_rate "
              "WHERE error_rate >= 1;")
    errorList = c.fetchall()
    pg.close()
    for i in errorList:
        print("%s - %s" % (i[0], i[1]))


print("Top Three Articles by Page View")
print("")
popularArticles()
print("")
print("Most Popular Authors Based on Total Article Views")
print("")
popularAuthors()
print("")
print("Days Where Errors Exceeded 1% of Total Views")
print("")
errors()
