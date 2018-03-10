from datetime import datetime
from string import Template
from time import sleep
import yaml

from steem import Steem

from btcPrice import getPrice

# Load config
with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# Setup steem
nodes = [
    'https://api.steemit.com',
    'https://steemd.steemitstage.com',
    'https://steemd.steemitdev.com',
    'https://steemd.privex.io',
    'https://gtg.steem.house:8090',
    'https://rpc.steemliberator.com',
    'https://steemd.minnowsupportproject.org',
    'https://rpc.buildteam.io',
    'https://steemd.pevo.science',
    'https://steemd.steemgigs.org',
]
s = Steem(nodes, False, )

def commentBatch():
    f = open('lastPost.txt', 'r')
    lastPost = f.read()
    f.close()

    global s
    posts = s.get_posts(limit=10, sort="created", category=cfg['app']['category'])

    for post in posts:
        if (lastPost is not None) and (lastPost == post.identifier):
            break
        commentPost(post)

    f = open('lastPost.txt', 'w')
    f.write(posts[0].identifier)
    f.close()
    print('batch complete.')


lastCommented = None


def commentPost(post):
    global lastCommented

    if lastCommented is not None:
        toWait = 20 - (datetime.now() - lastCommented).seconds
        if toWait >= 0:
            print(f'waiting for {toWait} seconds')
            sleep(toWait)

    print('commenting on a post: ' + post.identifier)
    body = Template(cfg['app']['replyBody']).substitute(btcPrice=getPrice())
    # print(body)

    post.reply(body, author=cfg['app']['account'])
    lastCommented = datetime.now()


while True:
    commentBatch()
    sleep(cfg['app']['sleepInterval'])
