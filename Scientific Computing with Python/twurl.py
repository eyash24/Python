import urllib.request, urllib.error, urllib.parse
import hidden
import oauth

def augmentt(url,parameter):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, token=token, http_method='GET', http_url=url, parameters=parameter)
    oauth_request.sign_request(oauth.OAuthSignatureMethid_HMAC_SHAI(), consumer, token)
    return oauth_request.to_url()
    