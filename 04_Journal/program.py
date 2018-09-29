import journal
# from journal import load, save (less obvious where it comes from)
# from journal import * (ambiguous)


def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------------')
    print('      JOURNAL APP')
    print('------------------------')


def run_event_loop():
    print('What do you want to do with your journal')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)  # new list()

    while cmd != 'x' and cmd:   # cmd (not empty) returns true

        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Finished for now.')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries...')
    # reverse order so shows newest first
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text)


if __name__ == '__main__':
    main()
