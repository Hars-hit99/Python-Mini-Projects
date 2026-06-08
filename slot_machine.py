import random
import time

def spin_row():
  symbols = ['🍒','🍉','🍌','🔔','⭐']
  return [random.choice(symbols) for symbol in range(3)]


def print_row(result):
  for symbol in result:
    time.sleep(1)
    print(symbol, end= " | ")

def get_payout(bet, row):
  if row[0] == row [1] and row[1] == row[2]:
    time.sleep(0.5)
    print("Congratulations!! You Won")
    if row[0] == '🍒':
      return bet * 2
    elif row[0] == '🍉':
      return bet * 3
    elif row[0] == '🍌':
      return bet * 4
    elif row[0] == '🔔':
      return bet * 5
    elif row[0] == '⭐':
      return bet * 10
    else:
      return 0
  else:
    time.sleep(0.5)
    print("Sorry!! you lost")
    return 0

def main():
  print("***************************")
  print("  Welcome to Python Slots  ") 
  print(" Symbols: 🍒 🍉 🍌 🔔 ⭐ ")
  print("***************************")
  balance = 100
  print("***************************")
  while balance > 0:
    bet = input("Enter your bet: ")
    print("***************************")
    
    if not bet.isdigit():
      print("Enter a Valid number")
      print("***************************")
      continue

    bet = int(bet)

    if bet <= 0:
      print("Bet should be greater than 0")
      print("***************************")
      continue

    if bet > balance:
      print("Bet should not be greater than balance")
      print("***************************")
      continue

    balance -= bet
    result = spin_row()

    print("---SPINNING---")
    print("**************")
    print_row(result)
    print("\n**************")

    balance = balance + get_payout(bet, result)
    
    print("***************************")
    time.sleep(0.5)
    print("Balance left: ₹",balance)
    print("***************************")
    time.sleep(0.5)

    play_again = input("Do you want to bet again?(Y/N): ").upper()
    print("***************************")

    if play_again != 'Y':
      break
  time.sleep(0.5)
  print(f"You are leving with ₹{balance}")
  time.sleep(0.5)
  print("Thank You for playing")
  print("***************************")

if __name__ == '__main__':
  main()