import requests


def load_input():
    f = open("input.txt")
    content = f.readlines()
    f.close()
    return content


def call_api(content):
    content = [w.replace("\n", "") for w in content]
    for id in content:
        resp = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")
        if check_condition(resp.text):
            print(resp.text)
            save_output(format_record(id, resp.text))


def check_condition(response):
    condition = "qui"
    return condition in response


def save_output(record):
    f = open("output.txt", "a+")
    f.write(f"{record}\n")


def format_record(id, resp):
    return str(id) + " | " + resp.replace("\n", "")


def clear_output_file():
    open('output.txt', 'w').close()


def dummy_test_input():
    f = open('input.txt', 'w')
    for i in range(150):
        f.write(f"{i}\n")


if __name__ == '__main__':
    dummy_test_input()
    clear_output_file()
    content = load_input()
    call_api(content)
