import csv
import re
from github import Github
from tqdm import tqdm


BUG_LIST = ["bug"]
PULL_BUG_LIST = ["cla: yes", "cla: no"]
BUG_WORDS = ["fix", "broken", "solve", "problem", "bug", "defect", "error", "incorrect", "unsuccessful", "wrong", "fault", "fail", "crash", "nan", "inf"]
FL_LIST = ["OpenMined/PySyft", "FederatedAI/FATE", "tensorflow/federated", "mher/flower", "PaddlePaddle/PaddleFL", "bytedance/fedlearner"]


def is_match(list_a, list_b):
    for word_a in list_a:
        for word_b in list_b:
            result = re.match(word_a, word_b)
            if result:
                return True
    return False


def fetch_issues_and_prs(fl, g):
    issue_num, pull_num = 0, 0
    repo = g.get_repo(fl)
    issues = repo.get_issues(state="closed")
    
    with open(f'data/{fl.split("/")[1]}/issues_init.csv', 'w', encoding="utf-8", newline='') as f_issue, \
         open(f'data/{fl.split("/")[1]}/PRs_init.csv', 'w', encoding="utf-8", newline='') as f_pull:
        writer_issue = csv.writer(f_issue, delimiter='\t')
        writer_pull = csv.writer(f_pull, delimiter='\t')
        writer_issue.writerow(['url', 'label', 'title', 'all_text', 'comments', 'created_time', 'updated_time', 'closed_time'])
        writer_pull.writerow(['url', 'label', 'title', 'all_text', 'comments', 'merged', 'created_time', 'updated_time', 'closed_time'])

        for _, issuepull in zip(tqdm(range(issues.totalCount)), issues):
            if issuepull.comments >= 1:
                if not issuepull.pull_request:
                    is_issue = True
                else:
                    issuepull = repo.get_pull(issuepull.number)
                    is_issue = False
                
                html_url = issuepull.html_url
                title = issuepull.title
                body = issuepull.body or ''
                comments_text = ''.join([comment.body for comment in issuepull.get_comments()])
                all_text = title + body + comments_text
                search_text_list = [word.lower() for word in title.split(" ")]
                label_list = [str(label).split(":")[-1].strip().lower() for label in issuepull.labels]

                if is_issue and (is_match(BUG_LIST, label_list) or (not label_list and is_match(BUG_WORDS, search_text_list))):
                    writer_issue.writerow([html_url, label_list, title, all_text, issuepull.comments, issuepull.created_at, issuepull.updated_at, issuepull.closed_at])
                    issue_num += 1
                elif not is_issue and (is_match(BUG_LIST, label_list) or (is_match(PULL_BUG_LIST, label_list) or not label_list) and is_match(BUG_WORDS, search_text_list)):
                    writer_pull.writerow([html_url, label_list, title, all_text, issuepull.comments, issuepull.merged, issuepull.created_at, issuepull.updated_at, issuepull.closed_at])
                    pull_num += 1

    return issue_num, pull_num


def main(token):
    g = Github(token)
    sum_issue, sum_pull = 0, 0
    
    for fl in FL_LIST:
        try:
            issue_num, pull_num = fetch_issues_and_prs(fl, g)
            print(f"{fl}: issue: {issue_num} pull: {pull_num}")
            sum_issue += issue_num
            sum_pull += pull_num
        except Exception as e:
            print(f"Error processing {fl}: {e}")
    
    print(f"Sum of Issues: {sum_issue}. Pull: {sum_pull}")


if __name__ == "__main__":
    token = ""
    main(token)
