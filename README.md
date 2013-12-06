familiar
========

Steps....

1) get virtual server and host and stuff
-done

2) get some form of shitty html/css up to work with.
-done

3) create the forms for login and register and needed js
-done

4) Handle registering
    a) get form submitting post to the same page (main)
    b) set up sqlite3
    c) layout database for Christmas list only at first. 
           User table -> username(primary key)
                         password(encrypted)
                         email(optional)
           gift table -> id(primary key)
                         title
                         description(optional)
           user/gift join table
    d) insert submitted data into db
    e) shoe some kind of message
           
