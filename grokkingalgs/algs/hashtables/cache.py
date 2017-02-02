cache = dict()

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        return "add to cach and return"

print(get_page('df'))