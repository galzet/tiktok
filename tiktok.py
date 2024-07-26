import requests
URL = 'https://vt.tiktok.com/ZSYvwj1uj'
USER_AGENT = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}


def get_redirect_url(url):
    session = requests.Session()
    return session.get(url, headers=USER_AGENT).url


def get_embed_video(url):
    request_url = f'https://www.tiktok.com/oembed?url={url}'
    res = requests.get(request_url).json()
    if 'code' in res:
        return 'error'
    return res['html']


if __name__ == '__main__':
    print(get_embed_video(URL))
