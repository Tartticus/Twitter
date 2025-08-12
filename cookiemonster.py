# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 17:06:09 2025

@author: matth
"""

from selenium import webdriver
import pickle
import time

# ---------- STEP 1: LOGIN & SAVE COOKIES ----------
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

# Give yourself time to log in manually
time.sleep(40)  # Adjust this so you have time to log in

# Save cookies to a file
pickle.dump(driver.get_cookies(), open("twitter_cookies.pkl", "wb"))
driver.quit()

# ---------- STEP 2: LOAD COOKIES & REUSE SESSION ----------
driver = webdriver.Chrome()
driver.get("https://twitter.com/")

# Load cookies from file
for cookie in pickle.load(open("twitter_cookies.pkl", "rb")):
    driver.add_cookie(cookie)

# Refresh to apply cookies
driver.refresh()

time.sleep(5)
print("Logged in without typing credentials again!")
