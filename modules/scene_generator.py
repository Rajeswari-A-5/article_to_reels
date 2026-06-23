def create_scenes(summary):

    words = summary.split()

    scenes = []

    chunk_size = 8

    for i in range(0, len(words), chunk_size):

        chunk = words[i:i+chunk_size]

        scenes.append(

            " ".join(chunk)

        )

    return scenes