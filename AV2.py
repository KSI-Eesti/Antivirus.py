import os
import os.path
import numpy

def deep_scan():
  path = "/"
  rem = ""
  for dirpath, dirnames, fylenames in os.walk(path):
    for fyle in [f for f in fylenames]:
      virus_def = [".exe", ".bat", ".dll", ".msi", ".chm", ".hta", ".ws", ".hlp", ".txt"]
      for i in virus_def:
        if (fyle.endswith(i)):
          rem = input("found virus!! virus is called {}\nresolve? y/n".format(fyle))
          if ("y" in rem):
            os.remove("{}/{}".format(dirpath, fyle))
          else :
            print("Your files have been resolved ")


