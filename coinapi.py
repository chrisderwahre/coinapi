#####Welcome to the Coin-api by ChrisderWahre#####

import shutil
import os
import time
import discord

pathToUser = "" ##If empty, it will be in the installation path of the api.##
pathToUserCache = "" ##If empty, it will be in the installation path of the api.##

defaultCoins = "100"

class coinapi:
    
    def addCoin(user, coins):       ##Add's Coins to user.##
        try:
            shutil.move(pathToUser + user + ".txt", pathToUserCache + user + "_cache.txt")

            source = open(pathToUserCache + user + "_cache.txt", "r")
            destination = open(pathToUser + user + ".txt", "w")
            for line in source:
                a = str(line)
                b = str(coins)
                d = int(a) + int(b)
                destination.write(str(d))

            destination.close()
            source.close()
            time.sleep(1)
            os.remove(pathToUserCache + user + "_cache.txt")
        except:
            print("Error!")
    
    def removeCoin(user, coins):       ##Removes Coins from user.##
        try:           
            shutil.move(pathToUser + user + ".txt", pathToUserCache + user + "_cache.txt")

            source = open(pathToUserCache + user + "_cache.txt", "r")
            destination = open(pathToUser + user + ".txt", "w")
            for line in source:
                a = str(line)
                b = str(coins)
                d = int(a) - int(b)
                destination.write(str(d))

            destination.close()
            source.close()
            time.sleep(1)
            os.remove(pathToUserCache + user + "_cache.txt")
        
        except:
            print("Error!")
            
    def getCoins(user):     ##Get the Coins from a user.##
        try:
            with open(pathToUser + user + ".txt") as f:
                return '\n'.join(line for line in f)
        except:
            return "Error!"

    def addUser(user):      ##Add's user to your database.##
        try:
            with open(pathToUser + user + ".txt", "a") as userFile:
                userFile.write(defaultCoins)
                userFile.close
        except:
            print("Error!")

    def removeUser(user):       ##Removes a user from your database.##
        try:
            os.remove(pathToUser + user + ".txt")
        except:
            print("Error!")
            
    def setCoins(user, coins):  ##Sets the user coins.##
        try:
            coinapi.removeCoin(user, coinapi.getCoins(user))
            coinapi.addCoin(user, coins)
        except:
            print("Error!")
            
    def resetCoins(user):   ##Resets the coins of the user.##
        try:
            coinapi.setCoins(user, defaultCoins)
        except:
            print("Error!")
                
