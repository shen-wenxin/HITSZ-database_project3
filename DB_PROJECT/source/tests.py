# from django.test import TestCase
import json
# # Create your tests here.
x = ",,,,course1"
print(x.split(','))
y = x.split(',')
for i in y:
    if i == "":
        y.remove(i)

print(y)
