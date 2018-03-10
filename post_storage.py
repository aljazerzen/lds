import yaml

storage = None


def get(category):
    global storage

    if storage is None:
        try:
            with open("post.storage.yml", 'r') as ymlfile:
                storage = yaml.load(ymlfile)
                ymlfile.close()
        except FileNotFoundError:
            return None

    try:
        return storage[category]
    except:
        return None


def save(post, category):
    global storage

    if storage is None:
        storage = {}

    storage[category] = post

    with open("post.storage.yml", 'w') as ymlfile:
        yaml.dump(storage, ymlfile)
        ymlfile.close()
