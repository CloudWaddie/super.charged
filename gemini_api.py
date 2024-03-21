#Load required modules
import google.generativeai as genai
import os
import PIL.Image

def textToText(prompt, key, stream=True):
    text = ""
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt, stream=stream)
    for chunk in response:
        text += chunk.text
    return text


#textToText("Write an essay on dogs")

def ImageToText(image, key):
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(img)
    return response.text

#img = PIL.Image.open("image.jpg")
#ImageToText(img)

def ImageAndTextToImage(prompt, img, key, stream=True):
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, img], stream=stream)
    response.resolve()
    return response.text

#ImageAndTextToImage("Write an essay on this", img)