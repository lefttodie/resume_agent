from agents.job_agent import run_agent
from utils.save_jobs import save_jobs


def main():

    resume_path = "data/Aman Singh Resume.pdf"

    jobs = run_agent(resume_path)

    print("\nLatest Jobs Found:\n")

    for j in jobs:
        print(j["title"])

    save_jobs(jobs)


if __name__ == "__main__":
    main()