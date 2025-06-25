# [SQL - Introduction](https://intranet.hbtn.io/projects/2128)

## [0. List databases](0-list_databases.sql)
Script that lists all databases of the current MySQL server.

## [1. Create a database](1-create_database_if_missing.sql)
Script that creates the database `hbtn_0c_0` in the current MySQL server. Avoided using the `SELECT` or `SHOW` statements.

## [2. Delete a database](2-remove_database.sql)
Script that deletes the database `hbtn_0c_0` in the current MySQL server. Avoided using the `SELECT` or `SHOW` statements.

## [3. List tables](3-list_tables.sql)
Script that lists all the tables of the passed database in the current MySQL server.

## [4. First table](4-first_table.sql)
Script that creates the table `first_table` in the current database in the current MySQL server. Avoided using the `SELECT` or `SHOW` statements.

## [5. Full description](5-full_table.sql)
Script that prints the description of the table `first_table` from the database `hbtn_0c_0` in the current MySQL server. Avoided using the `DESCRIBE` or `EXPLAIN` statements.

## [6. List all in table](6-list_values.sql)
Script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in the current MySQL server.

## [7. First add](7-insert_value.sql)
Script that inserts the following row in the table `first_table` from the database `hbtn_0c_0` in the current MySQL server:
| `id` | `name` |
| ---- | ------ |
| 89 | `Best School` |

## [8. Count 89](8-count_89.sql)
Script that displays the number of records with `id` equaling `89` in the table `first_table` from the database `hbtn_0c_0` in the current MySQL server.

## [9. Full creation](9-full_creation.sql)
Script that creates a table `second_table` in the database `hbtn_0c_0` in the current MySQL server, with the same model, plus a `score` column. Also creates rows :
| `id` | `name` | `score` |
| - | - | - |
| 1 | `John` | 10 |
| 2 | `Alex` | 3 |
| 3 | `Bob` | 14 |
| 4 | `George` | 8 |

## [10. List by best](10-top_score.sql)
Script that lists all records of the table `second_table` in the database `hbtn_0c_0` in the current MySQL server, displaying the score and the name, ordering them in descending order (from highest to lowest score).

## [11. Select the best](11-best_score.sql)
Script that lists all records with a score higher than or equaling 10 in the table `second_table` in the database `hbtn_0c_0` in the current MySQL server, displaying the score and the name, ordering them in descending order (from highest to lowest score).

## [12. Cheating is bad](12-no_cheating.sql)
Script that replaces Bob's score into 10 (because he cheated), in the table `second_table` in the database `hbtn_0c_0` in the current MySQL server.

Before:
| `id` | `name` | `score` |
| - | - | - |
| 3 | `Bob` | 14 |

After:
| `id` | `name` | `score` |
| - | - | - |
| 3 | `Bob` | 10 |

## [13. Score too low](13-change_class.sql)
Script that removes every row with a score under (or equal to) 5 (terribly failed the test), in the table `second_table` in the database `hbtn_0c_0` in the current MySQL server.
