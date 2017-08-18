*** Settings ***
Documentation   This is the test
Library     Browser.py

*** Test Cases ***
Browser test
    open chrome  http://www.google.com.ua
    close browser
*** Keywords ***
