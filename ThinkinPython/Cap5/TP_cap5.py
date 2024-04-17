import time

#esempio sull'utilità della ricorsione
def contoallarovescia(secondi):
    if secondi <= 0:
        print('Via!')
    else:
        time.sleep(1)
        print(secondi)
        contoallarovescia(secondi-1)

contoallarovescia(5)