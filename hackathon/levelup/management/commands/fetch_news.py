import requests
from django.core.management.base import BaseCommand
from levelup.models import NewsArticle
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch news articles and save to database'

    def handle(self, *args, **kwargs):
        api_key = 'YOUR_NEWS_API_KEY'
        url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2024-06-26&'
       'sortBy=popularity&'
       'apiKey=990ebb54198a49c0923eb18c9a9d2cdb')
        response = requests.get(url)
        articles = response.json().get('articles', [])
        for article in articles:
            NewsArticle.objects.create(
                title=article['title'],
                content=article['content'],
                published_at=datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            )
        self.stdout.write(self.style.SUCCESS('Successfully fetched news articles'))