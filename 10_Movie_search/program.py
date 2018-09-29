import movies_svc
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print('----------------------------------')
    print('        MOVIE API SEARCH')
    print('----------------------------------')
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Movie search term (enter x to eXit):')
            if search != 'x':
                results = movies_svc.find_movies(search)
                print("Found {} movies for search '{}'".format(len(results), search))
                for m in results:
                    print("{} -- {}".format(m.year, m.title))
        except ValueError:
            print('Search term is missing or invalid')
        except ConnectionError as ce:
            print('Failed to connect to API')
        except Exception as ex:
            print('Duh. Error somewhere: {}'.format(ex))

    print('>>> exiting')


if __name__ == '__main__':
    main()
