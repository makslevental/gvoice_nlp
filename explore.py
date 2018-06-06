import json
from pprint import PrettyPrinter
from collections import Counter
from collections import Counter
import datetime
import re
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.plotly as py
import pandas as pd
import numpy as np
from os import path
from wordcloud import WordCloud

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=2)

messages = json.load(open('messages.json'))

text = ' '.join([msg['body'] for msg in filter(lambda x: x['name'] == 'Me', messages)])

text = text.lower().replace('!','').replace('.', '').replace(',','').replace('"','').replace("'",'').replace('?','')

# f = open('wordcount.txt', 'w')
# words = list(Counter(text.split()).items())
# words = [(x[0], x[1], len(x[0])) for x in words]
#
# words.sort(key=lambda x: (x[1], x[2]))
# words = list(reversed(words))
#
# for word, count, _word_len in words:
#         f.write(f'{word}:  {count}  {count/len(words)}\n')
#     f.close()

conversations = json.load(open('conversations.json'))


messages = json.load(open('messages.json'))
# for msg in messages:
#     # msg['time'] = datetime.datetime.strptime(re.sub(r'(.*):(\d\d)', r'\1\2', msg['time']),'%Y-%m-%dT%H:%M:%S.%f%z')
#     if msg['name'] in disambiguated_people:
#         msg['name'] = disambiguated_people[msg['name']]
#
# # for convo in conversations:
# #     disambiguated_people.extend([m['name'] for m in convo])
# #     names = {m['name'] for m in convo}
# #     other_person = (names - {'Me'})
# #     if other_person and other_person.pop() == '+13528713503':
# #         for m in convo:
# #             print(m['name'], m['body'])
# #     #     other_person = other_person.pop()
# #     #     # if any(filter(lambda x: '+' in x, names)) and not disambiguated_people.get(other_person):
# #     #     #     for m in convo:
# #     #     #         print(f"{m['name']} : {m['body']}")
# #     #     #     disambiguated_people[other_person] = input('who dis') or None
# #     #     if not ('+' in other_person or other_person.isnumeric()):
# #     #         disambiguated_people.append(other_person)
# #     # print('\n\n')
# # # pp.pprint(Counter(disambiguated_people))
#
# df = pd.DataFrame({'date': [re.sub(r'(.*):(\d\d)', r'\1\2', msg['time']) for msg in messages], 'name': [msg['name'] for msg in messages]}, columns = ['date', 'name'])
# df['date'] = pd.to_datetime(df['date'])
# df.index = df['date']
# del df['date']
#
#
# freq = df.groupby([df.name.values])
# mins = {*list(freq.count()[freq.count()['name'] > 10].index.values)}
# freqs = {}
# for name, messagess in freq.groups.items():
#     if name and name[0].isalpha() and name != 'Me' and name in mins:
#         freqs[name] = messagess.groupby(messagess.date)
#         for day, messages in freqs[name].items():
#             count = len(messages)
#             freqs[name][day] = count
#
#
# data = [go.Scatter(x=list(ya.keys()), y=list(ya.values()), name=name) for name, ya in freqs.items()]
# #
# layout = go.Layout(
#     title='text messages/day',
#     yaxis=dict(title='total received'),
# )
#
# fig = go.Figure(data=data, layout=layout)
# plot(fig)







disambiguated_people = {
    '+19545409952':  'jill',
    '+13526823409':  'ya',
    '+19172929059':  'han',
    '+15617150483':  'jen',
    '+13218727435':  'jacque',
    '+16462904401':  'nazik',
    '+16035826882':  'jacque',
    '+13235596611':  'jessica',
    '+12095055288':  'jacque',
    '+17172019081':  'patricia',
    '+13058247478':  'martha',
    '+15412855635':  'ryan peacecorps',
    '+13478794082':  'maria stock',
    '+15623158139':  'nancy peacecorps',
    '+12537972406':  'joe peacecorps',
    '+19173654176':  'mike apt',
    '+19548957747':  'kristina',
    '+15614205508':  'steve cise',
    '+19048661971':  'Matt Hoza',
    '+13523010080':  'okcupidgirl',
    '+12392502914':  'tom',
    '+13213017431':  'jacque',
    '+19546967307':  'daniel torres',
    '+18636603498':  'ashley matt',
    '+14065454961':  'google',
    '+19542608055':  'sean goldberg',
    '+19176795295':  'okcupidgirl',
    '+19179691597':  'okcupidgirl',
    '+16514109447':  'dylan peacecorps',
    '+16467457631':  'minyong',
    '+16465351232':  'okcupidgirl',
    '+14156466173':  'okcupidgirl',
    '+19543195993':  'chase',
    '+18135417281':  'okcupidgirl',
    '+13522134904':  'okcupidgirl',
    '+16463592738':  'emiapt',
    '+13528880611':  'evan',
    '+13525141607':  'okcupidgirl',
    '+12487622364':  'okcupidgirl',
    '+17864175641':  'random',
    '+14752828549':  'airbnb',
    '+16095401622':  'paul ubm',
    '+18635134362':  'okcupidgirl',
    '+17173503968':  'okcupidgirl',
    '+19178703370':  'okcupidgirl',
    '+16035331858':  'random',
    '+13104630427':  'aubrey peacecorps',
    '+13523395822':  'liz peacecorps',
    '+18632246511':  'kb',
    '+13476563510':  'franklin ssf',
    '+19199482524':  'lyft',
    '+19167151296':  'okcupidgirl',
    '+16267570674':  'okcupidgirl',
    '+18628120840':  'nicthinknum',
    '+19543053098':  'random',
    '+17863512746':  'random',
    '+17725389252':  '625apt',
    '+12394385394':  '625apt',
    '+15022655814':  'spam',
    '+13527276877':  'okcupidgirl',
    '+12013063029':  'random',
    '+13014378006':  'okcupidgirl',
    '+18503220146':  'lara calloway',
    '+15104686736':  'okcupidgirl',
    '+13058426880':  'greg fradlis',
    '+14123774379':  'okcupidgirl',
    '+16106086759':  'okcupidgirl',
    '+13522343908':  'spam',
    '+13529788981':  'okcupidgirl',
    '+19178183023':  'random',
    '+17186073570':  'random',
    '+18507284464':  'amor',
    '+15616014142':  'okcupidgirl',
    '+13473612229':  'random',
    '+16074263624':  'random',
    '+16013073134':  '625apt',
    '+18508662585':  'random',
    '+13522819991':  'random',
    '+13522146499':  'okcupidgirl',
    '+13522625752':  'groupchat',
    '+13472321607':  'random',
    '+14342480457':  'random',
    '+19012371551':  'phoebe?',
    '+15627737370':  'random',
    '+12482256819':  'kim',
    '+19195939455':  'okcupidgirl',
    '+17573199059':  'justinmarin',
    '+19043330825':  'joshalex',
    '+15182535184':  'random',
    '+13057767611':  'random',
    '+18133644836':  'Matt Hoza',
    '+19048661084':  'random',
    '+13522627264':  'group',
    '+13474708996':  'random',
    '+16504585286':  'airbnb',
    '+17184080754':  'okcupidgirl',
    '+16464603088':  'amanda pohen',
    '+19542749699':  'david',
    '+13525194994':  'liz peacecorps',
    '+19548035874':  'random',
    '+13215057777':  'random'
}