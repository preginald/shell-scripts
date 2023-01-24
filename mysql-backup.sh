#!/bin/bash

# Prompt for database name
read -p "Enter the name of the database to export: " db_name

# Prompt for output file name
read -p "Enter the name of the output file: " output_file

# Prompt for username
read -p "Enter the MySQL username: " mysql_user

# Prompt for password
read -s -p "Enter the MySQL password: " mysql_password
echo

# Export the database using mysqldump
mysqldump -u $mysql_user -p$mysql_password $db_name > $output_file

# Confirm export was successful
if [ $? -eq 0 ]; then
  echo "Database export successful. Output file: $output_file"
else
  echo "Error exporting database. Please check the entered parameters and try again."
fi