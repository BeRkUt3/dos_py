import requests

target = input("Target's URL: ")
count = input('How many requests (number or inf): ')

try:
    count = int(count)
    for _ in range(count):
        try:
            r = requests.get(target)
            print(r.status_code)
        except requests.exceptions.MissingSchema:
            print('Uncorrect URL')
            exit()
    print('COMPLETE')
except ValueError:
    while True:
        try:
            r = requests.get(target)
            print(r.status_code)
        except requests.exceptions.MissingSchema:
            print('Uncorrect URL')
            exit()