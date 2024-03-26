-- Converts Field name in Table first_table from Database hbtn_0c_0 to UTF8.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER
SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256)
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
