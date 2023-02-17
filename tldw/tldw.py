#!/usr/bin/env python3
import os
import sys
import openai
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def main():
    if len(sys.argv) < 2:
        print("Usage: tldw.py <youtube url>")
        sys.exit(1)

    url = sys.argv[1]

    transcript = YouTubeTranscriptApi.get_transcript(url)
    formatter = TextFormatter()
    subtitle = formatter.format_transcript(transcript, languages=['en'])
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{subtitle}\n\nOne paragraph summary and description of the content. Topics needs to be discussed in details \n\n",
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )

    print("tl;dw", response.choices[0].text)
