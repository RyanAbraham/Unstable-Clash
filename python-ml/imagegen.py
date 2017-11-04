import deviantart
import random
import re
import config

# Connect API
da = deviantart.Api(config.client_id, config.client_secret)

def generate_image_url(cardname):
    deviations = []
    tag_ = ""
    for word in reversed(re.findall(r"[\w']+", cardname)):
        tags = da.search_tags(word)
        if(tags != []):
            tag_ = random.choice(tags)
    if(tag_ == ""):
        while(deviations == []):
            deviations = da.browse(endpoint='popular')
    else:
        deviations = da.browse(endpoint='tags', tag=tag_)

    image = random.choice(deviations['results'])
    return image.url
