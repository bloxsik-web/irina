import os

def instance():
    if not os.path.exists("runtime"):
        os.makedirs("runtime")
    os.chdir("runtime")