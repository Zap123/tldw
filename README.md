# TL;DW - Too Long; Didn't Watch

TLDW is a tool that uses the OpenAI library to generate summaries of YouTube videos. It provides a quick and efficient way to get the main points of a video without having to watch the entire thing. With TLDW, you can save time and get the information you need.

## Usage

To generate a summary of a YouTube video, simply pass the video ID as an argument to the tldw command. The output will be a concise summary of the video's main points, generated by the OpenAI library.

usage: tl;dw [-h] [--question question] video id

The modifier question can be used to perform queries against the video's content.

OPENAI_API_KEY env variable must be set with the Openai key

## Example

- tldw QGdbs2S2YHk

tl;dw In this video, the speaker discusses how to learn more efficiently and avoid burnout. They suggest five steps for successful learning: changing the environment, focusing on different tasks, getting enough sleep, task switching, and maintaining motivation and discipline. They recommend traveling if possible and doing exercise as a way to change focus, sleeping earlier and waking up without an alarm, clustering tasks into bigger time buckets and having a routine with sleep, and setting a schedule and relying both on motivation and discipline.

- tldw --question "What are the five steps for successful learning?" QGdbs2S2YHk

1. Change: Find ways to vary your work and focus. Try traveling, working from home, going to a local cafe or library for a change of scenery, and doing sports or hobbies.
2. Learning Energy Bar: Be mindful of how much mental energy you have each day and prioritize what you need to learn. Start with the most important tasks first before looking at social media or watching TV.
3. Sleep: Get at least eight hours of sleep per night and try to wake up without an alarm. Have a routine with your sleep and go to bed earlier.
4. Task Switching: Minimize task switching and cluster tasks into bigger time buckets. Focus on one task at a time and do it regularly at a set time.
5. Motivation & Discipline: Rely on both motivation and discipline. When motivation fails, rely on discipline by having a schedule and trying your best even when you're not motivated or inspired.

## Limits

This is just an experiment, it doesn't work with videos that have very long subtitles. Further investigation will be required to overcome token limitations
