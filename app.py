from agents.job_agent import run_agent


def main():

    resume_path = r"C:\Users\aman singh\Downloads\resume_agent\data\Aman Singh Resume.pdf"

    jobs = run_agent(resume_path)

    print("\nLatest Jobs Found:\n")

    for i, job in enumerate(jobs):
        print(f"{i+1}. {job}")


if __name__ == "__main__":
    main()