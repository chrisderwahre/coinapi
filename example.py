import coinapi
import time

coinapi.coinapi.addUser("user")
time.sleep(2)
coinapi.coinapi.addCoin("user", "20")
time.sleep(2)
coinapi.coinapi.removeCoin("user", "10")
time.sleep(2)
coinapi.coinapi.getCoins("user")
time.sleep(2)
coinapi.coinapi.removeUser("user")
