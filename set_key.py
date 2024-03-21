import os

key = input("Please Enter API Key: ")
os.environ['GEMINI_API_KEY'] = key
print(os.getenv('GEMINI_API_KEY'))