if __name__ == '__main__':

    with open('trigrams.txt') as f:
        lines = f.readlines()
        n_to_the = 0
        n_to_the_other = 0
        n_to_the_wrong = 0
        n_tokens = len(lines)
        for line in lines:
            line = line.strip()
            n_to_the += line.startswith('to the ')
            n_to_the_other += line == 'to the other'
            n_to_the_wrong += line == 'to the wrong'

        print(f'to the: {n_to_the}')
        print(f'to the other: {n_to_the_other}')
        print(f'to the wrong: {n_to_the_wrong}')
        print(f'total: {n_tokens}')
        print(f'p(other | to the): {n_to_the_other / n_to_the * 100}')
        print(f'p(wrong | to the): {n_to_the_wrong / n_to_the * 100}')
        print(n_to_the_wrong / n_to_the)

