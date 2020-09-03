# DEMO

```
I'm using DRF Token implementation because of the speed. 

SQLLite is used as a database. In case that you want something else 
(like Postgres) I can change really fast.

I'm shiping sqllite database with predefined admin user.
Admin username: jovan
Admin password: jovan123  

There are 6 routes:

/user/create/ - Used for user creation. If everything is fine, you will get a Token. 
Default role for a user is a Writer.

/user/login/ - Used to login

/article/ - Returns a paginated list of articles

/article/create/ - Creates article. Only for admin users

/article/assign/{article_id}/ - Writer is assigning article to himself

/article/review/{article_id}/ - Writer is setting google doc url and status to In Review

/article/approve/{article_id}/ - Editor is approving article

```


