#django 
from django.http import HttpResponse

#utilities
from datetime import datetime
import json

def hello_world(request):
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  return HttpResponse('oh, hi! current server time is {now}'.format(now=str(now)))

def sort_integers(request):
  # import pdb; pdb.set_trace()
  numbers = request.GET['numbers']
  numbers= numbers.split(',')
  numbers = [int(i) for i in numbers]
  sorted_int = sorted(numbers)
  # return HttpResponse(numbers)
  
  data = {
    'satatus': 'ok',
    'numbers': sorted_int,
    'message': 'Integers sorted successfully'
  }
  return HttpResponse(
    json.dumps(data, indent=4),
    content_type='application/json')

def say_hi(request, name, age):
  if age < 12:
    message='Sorry {}, you are not allowed here'.format(name)
  else:
    message='Hellos, {}, welcome to platzigram'.format(name)
  
  return HttpResponse(message)