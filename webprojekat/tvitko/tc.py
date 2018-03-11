
import twitter




def podaci (tagovi, broj_tvitova):
    api = twitter.Api(consumer_key='kvwpPKVH9fZcZdwzPwbVBT3eL',
                      consumer_secret='1HOZHUjvvkYRtl0nzMIJlUQuj28qW0qwSHZC8vXvAJ2QcMsTlf',
                      access_token_key='972467752739966976-ChxzdGY5KnfGao4j8uxVt41Bcg2TsfZ',
                      access_token_secret='0B0k8i9CNrbtEoaDQt11rYKiDvQGEHGGrzPVzjjguxniw')

    print(api.VerifyCredentials())
    upit = api.GetSearch(tagovi, lang='en', result_type='recent', count=broj_tvitova, max_id='')
    tvitovi = []
    for tweet in upit:
        # tvitovi += [tweet.text, tweet.hashtags]
        tvitovi += [{'text': tweet.text, 'hastags': tweet.hashtags}]
        print(tweet.id, tweet.text, tweet.hashtags)
    return tvitovi



