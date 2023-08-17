import requests
import json
import csv
import time

BASE_URL = "http://api.stackexchange.com/2.3/search/advanced?pagesize=100&order=desc&sort=votes&answers=1&site=stackoverflow"

def get_url_for_search(position=None, keyword=None, tag=None, type='text'):
    if type == 'text' and position and keyword:
        return f"{BASE_URL}&{position}={keyword}"
    elif type == 'tag' and tag:
        return f"{BASE_URL}&tagged={tag}"
    return None

def fetch_data_from_stack_overflow(url):
    response = requests.get(url)
    data = json.loads(response.text)
    return data["items"]

def filter_and_format_data(items, question_list):
    results = []
    for post in items:
        question_id = post["question_id"]
        if question_id not in question_list and post["is_answered"]:
            question_list.append(question_id)
            created_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(post["creation_date"]))
            last_activity_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(post["last_activity_date"]))
            results.append([question_id, post["link"], post["tags"], post["title"], created_time, last_activity_time])
    return results

def main():
    question_list = []
    all_data = []

    tag_list = ["tensorflow-federated", "federated-learning", "pysyft"]
    for tag in tag_list:
        url = get_url_for_search(tag=tag, type='tag')
        if url:
            items = fetch_data_from_stack_overflow(url)
            all_data.extend(filter_and_format_data(items, question_list))

    search_keywords = ["tensorflow_federated", "tensorflow+federated", "syft", "PySyft", "flwr", "fedlearner", "federated+learning", "paddle_fl", "PaddleFL", "fedavg"]
    for keyword in search_keywords:
        for position in ["title", "body"]:
            url = get_url_for_search(position=position, keyword=keyword)
            if url:
                items = fetch_data_from_stack_overflow(url)
                all_data.extend(filter_and_format_data(items, question_list))

    with open('data/SO/init.csv', 'w', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['id', 'url', 'label', 'title', 'created_time', 'last_activity_date'])
        writer.writerows(all_data)
    print(f"All number of questions: {len(all_data)}")

if __name__ == "__main__":
    main()
