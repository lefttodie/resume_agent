import json


def save_jobs(jobs):

    with open("latest_jobs.txt", "w", encoding="utf-8") as f:

        for i, job in enumerate(jobs, 1):

            f.write(f"Job {i}\n")
            f.write(f"Title : {job['title']}\n")
            f.write(f"URL   : {job['url']}\n")
            f.write(f"About : {job['about']}\n")
            f.write("-" * 50 + "\n")

    with open("latest_jobs.json", "w") as f:
        json.dump(jobs, f, indent=4)

    print("Jobs saved to latest_jobs.txt and latest_jobs.json")