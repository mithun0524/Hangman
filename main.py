import random

import art
import words

print(art.logo)
end_of_game = False
word_list = words.word_list
chosen_word = random.choice(word_list)

lives = 6

display = []
for _i in range(len(chosen_word)):
  display.append('_')

print(' '.join(display), "\n")
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for letter in range(len(chosen_word)):
    if chosen_word[letter] == guess:
      display[letter] = guess
  print(' '.join(display))
  if guess not in chosen_word:  
    lives -= 1
    print(art.stages[lives])
    if lives == 0:
      print("You Lose.")
      end_of_game = True
      
  if "_" not in display:
    end_of_game = True
    print("You Win!")
