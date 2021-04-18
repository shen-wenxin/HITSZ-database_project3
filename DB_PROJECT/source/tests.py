# from django.test import TestCase
import json
# # Create your tests here.
x= ["王泓鹏","张晓峰"]
after_json = json.dumps(x)
print(type(json.loads(after_json)))
