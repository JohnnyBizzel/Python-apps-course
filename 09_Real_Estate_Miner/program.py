import csv
import os
import statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('---------------------------------')
    print('  REAL ESTATE DATA MINING APP')
    print('---------------------------------')
    print()


def get_data_file():
    # get base folder for the selected data file
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv' )


# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         # read header first
#         header = fin.readline().strip()
#         print('found header: ' + header)
#
#         # loop over rest of data in file
#         lines = []
#         for line in fin:
#             # strip() removes the \n char of the CSV file
#             line_data = line.strip().split(',')
#             # #clunky way of reading the data:
#             # #bed_count = line_data[4]
#             lines.append(line_data)
#
#         print(lines[:6])


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        # header = fin.readline().strip()
        # print(header)
        # reader = csv.reader(fin)
        # # reader = csv.reader(fin, delimiter=',') <- optional change delimiter
        # for row in reader:
        #     print(row)
        #     beds = row[4]

        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            # print(type(row), row)
            # # test for presence of key in dict
            # if 'beds' in row:
            #     print("Bed count: {}".format(row['beds']))
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


# def get_price(p):
#     return p.price


def query_data(data):
    # ## if data sorted by price:
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)

    # MOST EXPENSIVE HOUSE
    expensive = data[-1]
    print('Highest price ${:,} with {} beds & {} bathrooms'.format(expensive.price, expensive.beds, expensive.baths))

    # LEASE EXPENSIVE HOUSE
    cheapest = data[0]
    print('Lowest price ${:,} with {} beds & {} bathrooms'.format(cheapest.price, cheapest.beds, cheapest.baths))

    # AVERAGE HOUSE PRICE
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)
    prices = [
        # projection or items
        # (p.price, p.beds, p.city)
        p.price
        # the set to process
        for p in data
    ]
    ave_cost = statistics.mean(prices)
    print("The average house price was ${:,}".format(int(ave_cost)))

    # AVERAGE PRICE OF 2 BED HOUSE
    # prices = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    # two_bed_homes = [
    #     p
    #     for p in data
    #     if p.beds == 2  # test (where clause)
    # ]

    # Generator expressions do not need to look through the whole collections
    two_bed_homes = (
        p
        for p in data
        if p.beds == 2  # test (where clause)
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)

    ave_cost = statistics.mean([p.price for p in homes])
    ave_bathooms = statistics.mean((p.baths for p in homes))
    ave_sqft = statistics.mean((p.sq__ft for p in homes))

    print('Average 2 bedroom house was ${:,}, baths={:.3}, sq ft={:,}'
          .format(int(ave_cost), float(ave_bathooms), round(ave_sqft, 1)))


if __name__ == '__main__':
    main()
