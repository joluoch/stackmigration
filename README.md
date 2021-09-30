# stackmigration
In this repo we are going to perform some automation and migrations of a datawarehose. migration will happen as a continuation form last weeks project : https://github.com/joluoch/datawarehouse

# migration form - to 
1. from myslq to postgresql 
2. from redash to superset

# definations 
 postgresql - It is a powerful, open-source Object-relational database system. It provides good performance with low maintenance efforts because of its high stability.

 superset - Superset is fast, lightweight, intuitive, and loaded with options that make it easy for users of all skill sets to explore and visualize their data, from simple line charts to highly detailed geospatial charts.

# approach 
 1. we will write a script that will migrate data from mysql to postgreql automatically 
 2. then we will usr dbt to make models that will be visualized on superset
 3. we will set up superset and visualize.

 # resources 
 https://www.postgresqltutorial.com/postgresql-python/create-tables/
 https://superset.apache.org/docs/installation/installing-superset-from-scratch
 https://lab.alitrack.com/blog/install-apache-superset-on-windows-10-without-admin-rights/
