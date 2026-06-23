from newspaper import Article


def fetch_article(url):

    try:

        article = Article(url)

        article.download()

        article.parse()

        return article

    except Exception as e:

        print(f"Error: {e}")

        return None