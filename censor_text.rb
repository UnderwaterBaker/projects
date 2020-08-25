puts "Please enter text to censor."
text = gets.chomp
puts "Please enter words to censor."
redact = gets.chomp

text.downcase! #downcases to aviod confusion with capitals and lower case letters
redact.downcase!#downcases to aviod confusion with capitals and lower case letters

redacts = redact.split(" ")#splits the string of words the user does not want in the output into seperate workable strings
words = text.split(" ")#Splits text input string into workable strings

censored_string = ""#blank variable to save the censored version of the words
words.each do |word|#repeats for each thing in words
  if redacts.include? word#goes through the words of words and checks if they are in the redacts list
    censored_string += "REDACTED "#changes the word to REDACTED if its in the redacts list then adds it to the variable censored_string
  else
    censored_string += word + " "#if the word is not found in the redacts list it is added to the censored_string variable without modification
  end
end

print censored_string

#I cant figure out how to make it so the censored_string has the same capitalization as the text input string without removing the downcase
#I cant figure out how to have it still censor words with a period at the end (like if I want to cendor "dog" the program with censor the "dog" in the string "I want a dog." because of the period)
