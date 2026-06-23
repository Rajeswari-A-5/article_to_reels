from flask import Flask, render_template, request

from modules.fetch_article import fetch_article
from modules.summarizer import summarize_text
from modules.title_generator import generate_title
from modules.translator import translate_text
from modules.voice_generator import create_voice
from modules.video_creator import create_video
from modules.keyword_extractor import extract_keywords

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    title = ""

    ai_title = ""

    summary_text = ""

    translation = ""

    audio_file = ""

    video_file = ""

    if request.method == "POST":

        url = request.form["url"]

        language = request.form["language"]

        article = fetch_article(url)

        if article:

            summary = summarize_text(
                article.text,
                sentences=5
            )

            summary_text = "\n".join(summary)

            keywords = extract_keywords(

                summary_text

            )

            print(keywords)

            ai_title = generate_title(
                summary_text
            )

            translation = translate_text(
                summary_text,
                language
            )

            title = article.title

            audio_file = create_voice(
                summary_text,
                "static/summary.mp3"
           )

            print("Audio created")

            video_file = create_video(
                ai_title,
                summary_text,
                audio_file
            )

            print("Video created")

    return render_template(

        "index.html",

        title=title,

        ai_title=ai_title,

        summary=summary_text,

        translation=translation,

        audio_file=audio_file,

        video_file=video_file

    )


if __name__ == "__main__":

    app.run(debug=True)