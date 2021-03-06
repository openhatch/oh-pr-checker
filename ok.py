import collections
import urllib2
import json


def get_data():
    r = urllib2.urlopen('https://api.github.com/repos/openhatch/oh-mainline/pulls?state=all&per_page=100').read()
    return json.loads(r)

def just_merged_pull_requests(response):
    return [x
       for x in response
       if x['merged_at']]

def filter_where_two_from_same_user(response):
    users_to_count = collections.defaultdict(int)
    for x in response:
        users_to_count[x['user']['login']] += 1
    return [user for user in users_to_count
            if users_to_count[user] >= 2]

users_already_added = set([
    'eeshangarg',
    'sunu',
    'onceuponatimeforever',
    'shaunagm',
    'cpallares',
    'natea',
    'brittag',
    'Aaron1011',
    'pythonian4000',
    'willingc',
    'younjin',
    'ehashman',
    'paulproteus',
])

def main():
    found_people_to_add = False

    r = get_data()
    people = filter_where_two_from_same_user(
        just_merged_pull_requests(r))
    for person in people:
        if person not in users_already_added:
            found_people_to_add = True
            print 'Maybe you should add', person
    return found_people_to_add


if __name__ == '__main__':
    import sys
    sys.exit(main())
