import random
import string
response = 'n'
print('Please enter your phone number')
while response != 'y':
  def msg_gen(chars=string.digits):
    return '\'+' + str(random.randint(1,1000)) + ' (' + ''.join(random.choice(chars) for _ in range(3)) + ')' + ''.join(random.choice(chars) for _ in range(3)) + '-' + ''.join(random.choice(chars) for _ in range(4)) +'\''
  print(msg_gen())
  temp = input('Is this your phone number?')
  if temp == 'y' or temp == 'Y' or temp == 'yes' or temp == 'Yes' or temp == 'YES':
    response = 'y'
    flag = False
  elif temp == 'n' or temp == 'N' or temp == 'No' or temp == 'no' or temp == 'NO':
            response = 'n'
  else:
    if temp != 'y' and temp != 'n' :
      print('I\'m sorry. I didn\'t understand that. Please try again.\n')

print('Ending now')
