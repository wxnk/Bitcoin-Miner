import time, secrets
from random import randint
from colorama import Fore

passive_mode = input("Enable AFK Mode? (Y / N)")

continuing = True
btcval = 54232.12

if passive_mode == "y" or passive_mode == "Y":

  while(continuing):
    
    time.sleep(.01)
    ranInt = randint(0, 1000)

    if(ranInt <= 1):
      randomBTC = randint(1,100)/100
      print(f'{Fore.WHITE} [-] {secrets.token_hex(30)} {Fore.GREEN} | {str(randomBTC)} BTC | ( $ {round(btcval * randomBTC, 2)} )')
    
    else:
      print(f'{Fore.WHITE} [-] {secrets.token_hex(30)} {Fore.RED} | 0.00 BTC | ( $0.00 )')

else:
  while(continuing):
    
    time.sleep(.01)
    ranInt = randint(0, 1000)

    if(ranInt <= 1):
      randomBTC = randint(1,100)/100
      print(f'{Fore.WHITE} [-] {secrets.token_hex(30)} {Fore.GREEN} | {str(randomBTC)} BTC | ( $ {round(btcval * randomBTC, 2)} )')

      continuing = False
    
    else:
      print(f'{Fore.WHITE} [-] {secrets.token_hex(30)} {Fore.RED} | 0.00 BTC | ( $0.00 )')
