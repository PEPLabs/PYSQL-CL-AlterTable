# Background

SQL sublanguage: DDL (Data Definition Language)

The ALTER keyword allows us to add / remove columns and constraints on an existing table.

- Adding a column: ALTER TABLE table_name ADD column_name data_type [constraint];
- Removing a column: ALTER TABLE table_name DROP column_name;

## Problem 1

Assume the following table already exists, but is missing a `lastname` column.

| id | firstname |
|----|-----------|
| 1 | Kevin |
| 2 | Brian |
| 3 | Charles |

Write a SQL statement in `problem1.sql` that adds a `lastname` column to the `site_user` table, of type
varchar(100).
