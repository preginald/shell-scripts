#!/bin/bash

# Ask the user how many files to create
read -p "Enter the number of files to create: " num_files

# Ask the user for words to be included in the file names
read -p "Enter words to be included in the file names (separated by spaces): " words

# Ask the user for the different file extensions
read -p "Enter the different file extensions (separated by spaces): " extensions

# Split the words and extensions into arrays
IFS=' ' read -r -a word_array <<< "$words"
IFS=' ' read -r -a extension_array <<< "$extensions"

# Loop through the number of files to create
for (( i=1; i<=$num_files; i++ ))
do
  # Choose a random word from the word array
  rand_word=${word_array[$RANDOM % ${#word_array[@]}]}

  # Choose a random extension from the extension array
  rand_extension=${extension_array[$RANDOM % ${#extension_array[@]}]}

  # Create the file with the random word and extension
  touch "$rand_word.$rand_extension"
  echo "File $rand_word.$rand_extension created"
done
