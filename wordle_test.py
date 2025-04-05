import random
def idk(file_path):
  with open(file_path) as f:
    words = [line.strip() for line in f]
    return words
    
def khôngbiếtđặttênlàj(guess, guesses):
  return len(guess) == 5 and guess in guesses 

def kanyewest_trippin_frfr(guess, word):
  str = ""

  for i in range(5):
    if guess[i] == word[i]:
      str += "\033[32m" + guess[i]
    else:
      if guess[i] in word:
        str += "\033[33m" + guess[i]
      else:
        str += "\033[0m" + guess[i]
  return str + "\033[0m"
      
      
  

def wordle(guesses, answers):
  print("m có 6 cơ hội để đoán 1 từ tiếng anh gồm 5 chữ cái.")
  đáp_án = random.choice(answers)
  số_lượt = 1
  sl_gioihan = 6
  while số_lượt <= sl_gioihan:
    guess = input("Lượt đoán #" + str(số_lượt) + ": ").lower()
    if not khôngbiếtđặttênlàj(guess, guesses):
      print("Không hợp lệ, try again nibba")
      continue
    if guess == đáp_án:
      print("VICTORY!!! UR TRULY THE STORM THAT IS APPROACHING !!! YOU GUESSED THE WORD: ", đáp_án)
      break
    số_lượt += 1
    feedback = kanyewest_trippin_frfr(guess, đáp_án)
    print(feedback)
  if số_lượt > sl_gioihan:
    print("GAME OVER! (skill issue). Đáp án là: ", đáp_án)
    
    

guesses = idk("guesses.txt")
answers = idk("answers.txt")
wordle(guesses, answers)
input("\nNhấn Enter để thoát...")

