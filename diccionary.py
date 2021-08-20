def run():
    my_dictionary = {
        'key1': 1,
        'key2': 2,
        'key3': 3,
    }

    # print(my_dictionary['key1'])
    # print(my_dictionary['key2'])
    # print(my_dictionary['key3'])

    population_countries = {
        'Taiwan': 23603000,
        'Israer': 9051000,
        'Colombia': 50374000
    }

    # print(population_countries['Bolivia'])

    # for pais in population_countries.keys():
    #     print(pais)

    # for pais in population_countries.values():
    #     print(pais)

    for country, population in population_countries.items():
        print(country + ' tiene ' + str(population) + ' population')


if __name__ == '__main__':
    run()