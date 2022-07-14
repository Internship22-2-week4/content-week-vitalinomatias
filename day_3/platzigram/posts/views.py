from django.shortcuts import render

# from django.http import HttpResponse // se quita por el momento ya no se utilizara

from datetime import datetime

# Create your views here.

now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

posts = [
  {
    'title': 'Mont Blac',
    'user': {
       'name': 'yesica corte',
       'picture': 'https://i.picsum.photos/id/1027/60/60.jpg?hmac=NKZ0Vfbc1l_5mdJsZpOIQ0iRjvpE24KmZiI5l2ZUiaE'
      },
    'timestamp': now,
    'photo': 'https://i.picsum.photos/id/136/200/200.jpg?hmac=m5kYXq4zQR742H2cLvYw6nX1cJ65qKBb-kY84CbGCaQ'
  },
  {
    'title': 'via lactea',
    'user': {
       'name': 'vitalino',
       'picture': 'https://i.picsum.photos/id/1027/60/60.jpg?hmac=NKZ0Vfbc1l_5mdJsZpOIQ0iRjvpE24KmZiI5l2ZUiaE'
      },
    'timestamp': now,
    'photo': 'https://i.picsum.photos/id/136/200/200.jpg?hmac=m5kYXq4zQR742H2cLvYw6nX1cJ65qKBb-kY84CbGCaQ'
  },
  {
    'title': 'nuevo auditorio',
    'user': {
       'name': 'leonel matias',
       'picture': 'https://i.picsum.photos/id/1027/60/60.jpg?hmac=NKZ0Vfbc1l_5mdJsZpOIQ0iRjvpE24KmZiI5l2ZUiaE'
      },
    'timestamp': now,
    'photo': 'https://i.picsum.photos/id/136/200/200.jpg?hmac=m5kYXq4zQR742H2cLvYw6nX1cJ65qKBb-kY84CbGCaQ'
  }
]

def list_posts(request):
  return render(request, 'feed.html', {'posts': posts})
  # content = []
  # for post in posts:
  #   content.append("""
  #                  <p><strong>{name}</strong></p>
  #                  <p><small>{user} - <i>{timestamp}</i></small></p>
  #                  <figure><image src="{picture}"/></figure>
  #                  """.format(**post))
  # return HttpResponse('<br>'.join(content))