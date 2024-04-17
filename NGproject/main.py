import eel
import os
dirname= os.path.dirname(__file__)
eel.init(os.path.join(dirname,"web"))
eel.start('index.html',port=8080)