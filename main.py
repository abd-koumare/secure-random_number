from randnum import generate_random_num_str


if __name__ == '__main__':
    rand_number = generate_random_num_str()
    print(f'{rand_number} default length: {len(rand_number)}')

    for x in range(10, 20):
        rand_number = generate_random_num_str(x)
        print(f'{rand_number} length: {len(rand_number)}')
