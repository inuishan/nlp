from flask import Flask
from flask import request
import ner
import json

app = Flask(__name__)

from youtube_transcript_api import YouTubeTranscriptApi


def unify_labels(tokens):
    for token in tokens:
        entity = token['entity']
        if "PER" in entity:
            token['entity'] = "PER"
        if "ORG" in entity:
            token['entity'] = "ORG"
        if "LOC" in entity:
            token['entity'] = "LOC"


def merge_tokens(tokens, text):
    unify_labels(tokens)
    rv = []

    last_token_added = tokens[0]
    rv.append(last_token_added)

    for i in range(1, len(tokens)):
        token_in_question = tokens[i]
        if (last_token_added['entity'] == token_in_question['entity'] and last_token_added['end'] == token_in_question[
            'start']):
            last_token_added['end'] = token_in_question['end']
        else:
            last_token_added = token_in_question
            rv.append(token_in_question)
    for token in rv:
        token['word'] = text[token['start']: token['end']]
    return rv


@app.route('/ner/')
def hello_world():
    text = request.args.get('text')
    tokens = ner.extract_token(text)
    for token in tokens:
        del (token['score'])
    if len(tokens) != 0:
        merged = merge_tokens(tokens, text)
    else:
        merged = []
    return json.dumps(merged)

@app.route('/yt/')
def yt():
    video_id = request.args.get('video_id')

    # print(transcript)
    transcript_list, unretrievable_videos = YouTubeTranscriptApi.get_transcripts([video_id], continue_after_error=True)

    srt = transcript_list.get(video_id)

    text_list = []
    for i in srt:
        text_list.append(i['text'])

    text = ' '.join(text_list)
    return text


if __name__ == '__main__':
    app.run()
