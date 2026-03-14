# from playwright.sync_api import sync_playwright
# import random

# PROXY_USERNAME = "api5e199d7fe393aaf2"
# PROXY_PASSWORD = "RNW78Fm5"
# PROXY_HOST = "us.res.proxy-seller.com"
# PORTS = list(range(10001, 10020))


# def search_jobs(keyword):

#     jobs = []

#     port = random.choice(PORTS)

#     proxy_config = {
#         "server": f"http://{PROXY_HOST}:{port}",
#         "username": PROXY_USERNAME,
#         "password": PROXY_PASSWORD
#     }

#     url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location=India&sortBy=DD"

#     with sync_playwright() as p:

#         browser = p.chromium.launch(
#             headless=True,
#             proxy=proxy_config
#         )

#         context = browser.new_context()
#         page = context.new_page()

#         page.goto(url, timeout=60000)

#         page.wait_for_timeout(5000)

#         cards = page.query_selector_all(".base-search-card")

#         for c in cards[:20]:

#             title_el = c.query_selector(".base-search-card__title")
#             company_el = c.query_selector(".base-search-card__subtitle")
#             link_el = c.query_selector("a.base-card__full-link")
#             location_el = c.query_selector(".job-search-card__location")
#             date_el = c.query_selector("time")

#             job_url = link_el.get_attribute("href") if link_el else ""

#             title = title_el.inner_text().strip() if title_el else ""
#             company = company_el.inner_text().strip() if company_el else ""
#             location = location_el.inner_text().strip() if location_el else ""
#             date_posted = date_el.get_attribute("datetime") if date_el else ""

#             # open job page to get description
#             about = ""

#             if job_url:
#                 job_page = context.new_page()
#                 try:
#                     job_page.goto(job_url, timeout=30000)
#                     job_page.wait_for_timeout(3000)

#                     desc = job_page.query_selector(".show-more-less-html__markup")

#                     if desc:
#                         about = desc.inner_text()[:400]

#                 except:
#                     about = ""

#                 job_page.close()

#             job_type = "Unknown"

#             if "remote" in location.lower():
#                 job_type = "Remote"
#             elif "hybrid" in location.lower():
#                 job_type = "Hybrid"
#             else:
#                 job_type = "On-site"

#             jobs.append({
#                 "title": title,
#                 "company": company,
#                 "location": location,
#                 "date_posted": date_posted,
#                 "job_type": job_type,
#                 "url": job_url,
#                 "about": about
#             })

#         browser.close()

#     return jobs






from playwright.sync_api import sync_playwright
import random

PROXY_USERNAME = "api5e199d7fe393aaf2"
PROXY_PASSWORD = "RNW78Fm5"
PROXY_HOST = "us.res.proxy-seller.com"
PORTS = list(range(10001, 10020))


def search_jobs(keyword):

    jobs = []

    port = random.choice(PORTS)

    proxy_config = {
        "server": f"http://{PROXY_HOST}:{port}",
        "username": PROXY_USERNAME,
        "password": PROXY_PASSWORD
    }

    # last 24 hours filter
    url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location=India&sortBy=DD&f_TPR=r86400"

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            proxy=proxy_config
        )

        context = browser.new_context()

        page = context.new_page()

        page.goto(url, timeout=60000)

        # scroll to load more jobs
        for _ in range(5):
            page.mouse.wheel(0, 3000)
            page.wait_for_timeout(1000)

        cards = page.query_selector_all(".base-search-card")

        for c in cards[:20]:

            title_el = c.query_selector(".base-search-card__title")
            company_el = c.query_selector(".base-search-card__subtitle")
            link_el = c.query_selector("a.base-card__full-link")
            location_el = c.query_selector(".job-search-card__location")
            date_el = c.query_selector("time")

            title = title_el.inner_text().strip() if title_el else ""
            company = company_el.inner_text().strip() if company_el else ""
            location = location_el.inner_text().strip() if location_el else ""
            job_url = link_el.get_attribute("href") if link_el else ""

            date_posted = ""

            if date_el:
                date_posted = date_el.inner_text().strip()

            # detect job type
            job_type = "On-site"

            loc_lower = location.lower()

            if "remote" in loc_lower:
                job_type = "Remote"
            elif "hybrid" in loc_lower:
                job_type = "Hybrid"

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "date_posted": date_posted,
                "job_type": job_type,
                "url": job_url,
                "about": f"{title} role at {company} located in {location}"
            })

        browser.close()

    return jobs