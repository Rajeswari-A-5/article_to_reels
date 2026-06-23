from moviepy import (
    AudioFileClip,
    ImageClip,
    TextClip,
    CompositeVideoClip,
    vfx,
    concatenate_videoclips
)

from modules.image_fetcher import fetch_image


def create_video(title, summary, audio_file):

    WIDTH = 1080
    HEIGHT = 1920

    audio = AudioFileClip(audio_file)

    duration = audio.duration

    scenes = summary.split(".")

    scenes = [s.strip() for s in scenes if s.strip()]

    if not scenes:

        scenes = [summary]

    scene_duration = duration / len(scenes)

    clips = []

    image_path = fetch_image(title)

    for scene in scenes:

        bg = ImageClip(image_path)

        bg = bg.with_duration(scene_duration)

        text = TextClip(

            text=scene,

            font_size=70,

            color="white",

            method="caption",

            text_align="center",

            size=(900, 700)

        )

        text = text.with_duration(scene_duration)

        # Center alignment

        text = text.with_position(

            lambda t:(

                "center",

                1500-(t*80)

            )

        )

        text = text.with_effects(

            [vfx.FadeIn(0.5)]

        )

        clip = CompositeVideoClip(

            [bg, text],

            size=(WIDTH, HEIGHT)

        )

        clips.append(clip)

    final_video = concatenate_videoclips(

        clips,

        method="compose"

    )

    final_video = final_video.with_audio(audio)

    output_file = "static/summary_video.mp4"

    final_video.write_videofile(

        output_file,

        fps=30

    )

    return output_file