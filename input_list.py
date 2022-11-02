# Разделение ввода пользователя на список

import re

def UserInputSplit(userInput):  
    return re.split(r'\s*([-+\*\/\^\(\)\=])\s*', userInput) 