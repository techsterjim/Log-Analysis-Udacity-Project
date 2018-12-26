# Log-Analysis-Udacity-Project

Learned how to build a reporting tool that prints out reports (in plain text) based on the data in the database. Interacted with a live database both from the command line and from the python code. This project is a part of the Udacity's Full Stack Web Developer Nanodegree.

Technologies used
1. PostgreSQL
2. Writing Python code with DB-API
3. Linux-based virtual machine (VM) Vagrant

Project Requirements
Reporting tool should answer the following questions:

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?
Project follows good SQL coding practices: Each question should be answered with a single database query.
The code is error free and conforms to the PEP8 style recommendations.
The code presents its output in clearly formatted plain text.
System setup and how to view this project
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.

Download Vagrant and install.
Download Virtual Box and install.
Clone this repository to a directory of your choice.
Download the newsdata.sql (extract from newsdata.zip (not provided here though)) and newsdata.py files from the respository and move them to your vagrant directory within your VM.
Run these commands from the terminal in the folder where your vagrant is installed in:
vagrant up to start up the VM.
vagrant ssh to log into the VM.
cd /vagrant to change to your vagrant directory.
psql -d news -f newsdata.sql to load the data and create the tables.
python3 newsdata.py to run the reporting tool.
