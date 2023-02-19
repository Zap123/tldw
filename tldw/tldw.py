#!/usr/bin/env python3
import os
import sys
import openai
import argparse
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# List of prompts for the commands
instructions = {
    "meaning": f"One paragraph summary in English and description of the content.Topics needs to be discussed in details",
    "query": "Answer according to content",
}


def build_prompt(instruction, context, input=""):
    prompt = f"{instruction}\n\ncontent:{context}\n\n" + input
    return prompt


def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    parser = argparse.ArgumentParser(
        prog='tl;dw',
        description="Too Long; Didn't Watch generate summaries from Youtube videos",
    )
    parser.add_argument('video_id', metavar='video id',
                        help='the Youtube video id')

    question_group = parser.add_argument_group('question')
    question_group.add_argument('--question', metavar='question',
                                help='A question to search in the video (e.g. how to learn faster?)')
    question_group.add_argument('--creative', metavar='creative', action=argparse.BooleanOptionalAction,
                                help='Answer even when the video do not address the topic', default=False)

    args = parser.parse_args()

    # Download the default Youtube subtitle
    transcript_list = YouTubeTranscriptApi.list_transcripts(args.video_id)
    transcript = next(iter(transcript_list)).fetch()
    formatter = TextFormatter()
    subtitle = formatter.format_transcript(transcript)

    # Set the default meaning prompt
    instruction = instructions["meaning"]
    prompt = build_prompt(instruction, subtitle)

    # Change the prompt to query to answer questions
    if args.question:
        instruction = instructions["query"]
        if not args.creative:
            instruction = instruction + ".Isn't in content?Not said"
        prompt = build_prompt(instruction, subtitle, args.question)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )

    answer = response.choices[0].text

    print(f"tl;dw {answer.strip()}")


if __name__ == "__main__":
    main()
