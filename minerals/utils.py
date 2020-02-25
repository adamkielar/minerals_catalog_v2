def random_mineral_footer(random_mineral):

    for data in random_mineral:
        for key, value in data.items():
            if key == 'id':
                random_pk = int(value)
                return random_pk
