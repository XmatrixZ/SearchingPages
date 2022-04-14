import ast
import os
import WebpageSort
path = "C:/Users/SHIVANSH DHONDIYAL/PycharmProjects/SearchEngine/" #--> where dictionary data is stored

os.chdir(path)

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

def print_related_pages(webpages):
    for i in range(len(webpages['link'])):
        print(webpages['link'][i], end=" ")
        print(webpages['significance'][i])

if __name__ == '__main__':
    test_dict = {'All': 1, 'have': 2, 'good': 3, 'food': 4}
    check = True
    file = open(path+"dictionarydata.txt","r")
    content = file.read()
    dictionary = ast.literal_eval(content)
    file.close()

    while check:
        search = input("Enter string to find similar data: ")
        # Finding all the words that have a substring that was inputed by the search
        query = dict(filter(lambda item: search in item,dictionary.items()))
        if query == {}:
            print("The word cannot be found!!")
        # Sorting the ans of the query based on significance using Combination of  Merge sort and Insertion sort
        for key in query:
            for webpages in query.values():
                print()
                print(key)
                WebpageSort.WebpagesSort(webpages['link'], webpages['significance'], 0, len(webpages['significance']) - 1)
                print()
                print_related_pages(webpages)
        # print(str(query))
        execute = input("Do You wish to Try again(yes/no): ")
        check = execute == "yes" and True or False




