import asyncio
import edge_tts


def create_voice(text, output_file):

    async def generate():

        communicate = edge_tts.Communicate(

            text,

            voice="en-US-AvaMultilingualNeural",

            rate="+20%"

        )

        await communicate.save(output_file)

    asyncio.run(generate())

    return output_file