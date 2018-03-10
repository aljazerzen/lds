from datetime import datetime
from string import Template
from time import sleep
import yaml

from steem import Steem

# Load config
import post_storage
import btc_price

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


def comment_batch(category, textTemplate):
    global s
    posts = s.get_posts(limit=10, sort="created", category=category)
    lastPost = post_storage.get(category)

    for post in posts:
        if (lastPost is not None) and (lastPost == post.identifier):
            break
        comment_post(post, textTemplate)

    post_storage.save(posts[0].identifier, category)
    print(f'batch \'{category}\' complete.')


lastCommented = None


def comment_post(post, text):
    global lastCommented

    if lastCommented is not None:
        toWait = 20.5 - (datetime.now() - lastCommented).seconds
        if toWait >= 0:
            print(f'    waiting for {toWait} seconds')
            sleep(toWait)

    print('  commenting on a post: ' + post.identifier)
    body = Template(text).substitute(btcPrice=btc_price.get())
    # print(body)

    post.reply(body, author=cfg['app']['account'])
    lastCommented = datetime.now()


while True:
    try:
        for category in cfg['app']['categories']:
            comment_batch(list(category.keys())[0], list(category.values())[0])
    except Exception as e:
        with open('error.log', 'a+') as f:
            f.write(f'\n[{datetime.now()}]:\n' + str(e) + str(e.args) + '\n')
            f.close()

    sleep(cfg['app']['sleepInterval'])
