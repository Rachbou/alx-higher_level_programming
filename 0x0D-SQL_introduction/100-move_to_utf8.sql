-- Converts Field name in Table first_table from Database hbtn_0c_0 to UTF8.
USE hbtn_0c_0 ALTER TABLE first_table MODIFY name
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
