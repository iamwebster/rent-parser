from fake_useragent import UserAgent

ua = UserAgent(platforms='pc')

headers = {
    'User-Agent': ua.random,
}
