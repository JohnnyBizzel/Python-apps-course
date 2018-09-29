import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Err: Sorry we can't search that location")
        return

    text = get_search_text_from_user()
    if not text:
        print("Err: Sorry we can't search for nothing")
        return

    results = search_folders(folder, text)
    match_count = 0
    for m in results:
        match_count += 1
        # print(match)
        print('--------- MATCH -------------')
        print('file: ' + m.file)
        print('line: {}'.format(m.line))
        print('match: ' + m.text.strip())
        print()

    print('Found {:,} matches.'.format(match_count))


def print_header():
    print('-----------------------------')
    print('      FILE SEARCHER')
    print('-----------------------------')
    print()


def get_folder_from_user():
    folder = input('What folder do you want to search?')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]?')
    return text.lower()


def search_folders(folder, text):
    items = os.listdir(folder)
    # all_matches = []

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            # ## use recursion to search folders
            # matches = search_folders(full_item, text)
            # all_matches.extend(matches)
            yield from search_folders(full_item, text)
        else:
            # matches = search_file(full_item, text)
            # ## push items onto the collection:
            # all_matches.extend(matches)
            yield from search_file(full_item, text)

    # return all_matches


def search_file(filename, search_text):
    # matches = []
    with open(filename, 'r', encoding='utf-8') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                # matches.append(m)
                yield m

    #   return matches


if __name__ == '__main__':
    main()
