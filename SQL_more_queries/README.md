# [SQL - More queries](https://intranet.hbtn.io/projects/2129)

## [0. My privileges!](0-privileges.sql)
Script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the current MySQL `localhost` server.

## [1. Root user](1-create_user.sql)
Script that creates the `user_0d_1` on the current MySQL `localhost` server, with password `user_0d_1_pwd`, and gives it all privileges.

## [2. Read user](2-create_read_user.sql)
Script that creates the `hbtn_0d_2` database, and the `user_0d_2` on the current MySQL `localhost` server, with password `user_0d_2_pwd`, and gives it `SELECT` (read) privileges on the new database.
