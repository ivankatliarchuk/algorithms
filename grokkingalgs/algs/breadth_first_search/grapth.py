graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

print("Resulted graph {0}.".format(graph))

from collections import deque

search_queue = deque()
# add all the neigbours to the search
search_queue += graph['you']

print("Current first level neigbours {0}".format(search_queue))


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    search_seller(search_queue)

def search_seller(search_queue):
    # REVIEW -- swap with hashtable
    searched = set()
    # while the queue isn't empty
    while search_queue:
        # grabs the first person off the queue
        person = search_queue.popleft()
        if not person in searched:
            print("Name {}".format(person.capitalize()))
            # checks whether the person is a mango seller
            if person_is_seller(person):
                # Yes, they're mango seller
                print("{0} is MANGO seller".format(person).capitalize())
                return True
            else:
                # no, they aren't . Add all of this person's friends to the search queue
                search_queue += graph[person]
                # marks this person as searched
                searched.add(person)
    # if you reached here, no one in the queue was a mango seller
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search('you')
