
# Count the number of vowels and consonants


def vowel_count(sent):
    count = 0
    for i in sent:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            count = count + 1
    return count


def consonants_count(sent):
    count = 0
    for i in sent:
        if i.lower() in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
            count = count + 1
    return count


def number_count(sent):
    count = 0
    for i in sent:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            count = count + 1
    return count


def main(sent):
    v_count = vowel_count(sent)
    c_count = consonants_count(sent)
    n_count = number_count(sent)

    print("Vowels : ", v_count)
    print("Consonants : ", c_count)
    print("Numbers : ", n_count)


sent = input("Enter the sent: ")

main(sent)
