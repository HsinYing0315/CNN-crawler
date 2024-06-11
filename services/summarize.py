from openai import OpenAI
from services.crawler import fetch_article

client = OpenAI()

def summarize(url):
    article = fetch_article(url)
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a critic who is familiar with tech and good at summarizing. I would like you to analyze the provided news article and create a bullet-point summary for me."},
            {"role": "user", "content": article['paragraph']},
        ]
    )
    article.update({"summary": completion.choices[0].message.content})
    return article