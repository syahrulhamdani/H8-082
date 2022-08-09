def compute_factorial(n):
    "Compute factorial of n (n!)"
    result = 1
    i = 1

    while i <= n:
        result = result * i
        i = i + 1

    print("{}! = {}".format(n, result))
    return result


def repeat_all_words(*words, n_repeat=5):
    print("Repeat all words", n_repeat, "times!")
    repeated = []
    for word in words:
        print(word * n_repeat)
        repeated.append(word * n_repeat)
    return repeated


def repeat_words(word, n_repeat=3):
    print("Repeat", n_repeat, "times!")
    print(word * n_repeat)
    return word * n_repeat


course_name = "Hacktiv8 - PTP Python for Data Science"
num_students = 10