from bs4 import BeautifulSoup
import requests
import random


def scrap_articles():
    response = requests.get(f"https://www.fandom.com/topics/movies")
    response_text = response.text

    soup = BeautifulSoup(response_text, "html.parser")

    topics = [topic.text.replace("\n", "") for topic in soup.select(".card__title-wrapper")]
    summaries = [summary.text for summary in soup.select(".card__summary")]
    topic_tags = [topic_tag.text.replace("\t", "").replace("\n", "") for topic_tag in soup.select(".topic-tags.is-desktop a")]
    new_topic_tags = [new_topic_tag.strip() for new_topic_tag in " ".join(topic_tags).split("Movies")][1:]
    links = [topic.get("href") for topic in soup.select(".card__title-wrapper")]

    article_data = {f"article{num + 1}": {"topic": topics[num], "summary": summaries[num], "genre": new_topic_tags[num], "link": links[num]} for num in range(len(topics))}
    return article_data


def get_random_article():
    rand_key = random.choice([f"article{num}" for num in range(1, 101)])
    movie_article = scrap_articles()[rand_key]
    return movie_article


print("Fandom movie article:\n")
article = get_random_article()
for k, v in article.items():
    print(f"{k.title()}: {v}")


