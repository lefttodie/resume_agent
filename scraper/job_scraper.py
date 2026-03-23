# from playwright.sync_api import sync_playwright
# import random
# import urllib.parse

# PROXY_USERNAME = "USE YOUR USERNAME"
# PROXY_PASSWORD = "USE YOUR PASSWORD"
# PROXY_HOST = "USE YOUR HOST NAME"
# PORTS = list(range(10001, 10120))


# # def search_jobs(keyword, website, job_type="job"):

# #     jobs = []

# #     if website != "linkedin":
# #         return []

# #     try:

# #         with sync_playwright() as p:

# #             port = random.choice(PORTS)

# #             proxy_config = {
# #                 "server": f"http://{PROXY_HOST}:{port}",
# #                 "username": PROXY_USERNAME,
# #                 "password": PROXY_PASSWORD
# #             }

# #             browser = p.chromium.launch(
# #                 headless=True,
# #                 proxy=proxy_config
# #             )

# #             encoded_keyword = urllib.parse.quote(keyword)

# #             url = (
# #                 f"https://www.linkedin.com/jobs/search/"
# #                 f"?keywords={encoded_keyword}"
# #                 f"&location=India"
# #                 f"&f_TPR=r3600"
# #                 f"&sortBy=DD"
# #             )

# #             print("Searching:", keyword)
# #             print("URL:", url)

# #             context = browser.new_context(
# #                 user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# #             )

# #             page = context.new_page()

# #             page.goto(url, timeout=60000)

# #             page.wait_for_timeout(5000)

# #             cards = page.query_selector_all("li")

# #             print("Cards found:", len(cards))

# #             for card in cards:

# #                 try:

# #                     title_el = card.query_selector("h3")
# #                     company_el = card.query_selector("h4")
# #                     location_el = card.query_selector(".job-search-card__location")
# #                     time_el = card.query_selector("time")
# #                     link_el = card.query_selector("a")

# #                     if not title_el:
# #                         continue

# #                     title = title_el.inner_text().strip()

# #                     company = ""
# #                     if company_el:
# #                         company = company_el.inner_text().strip()

# #                     location = ""
# #                     if location_el:
# #                         location = location_el.inner_text().strip()

# #                     date_posted = ""
# #                     if time_el:
# #                         date_posted = time_el.inner_text().strip()

# #                     url_link = ""
# #                     if link_el:
# #                         url_link = link_el.get_attribute("href")

# #                     job_type_value = "On-site"

# #                     about = f"{title} role at {company} located in {location}"

# #                     job = {
# #                         "source": "linkedin_job",
# #                         "title": title,
# #                         "company": company,
# #                         "location": location,
# #                         "date_posted": date_posted,
# #                         "job_type": job_type_value,
# #                         "url": url_link,
# #                         "about": about
# #                     }

# #                     jobs.append(job)

# #                 except:
# #                     continue

# #             browser.close()

# #     except Exception as e:

# #         print("Scraper error:", str(e))

# #     print("Jobs extracted:", len(jobs))

# #     return jobs


# def search_jobs(keyword, website, job_type="job"):

#     jobs = []

#     if website != "linkedin" or job_type != "job":
#         return []

#     try:
#         with sync_playwright() as p:

#             port = random.choice(PORTS)

#             proxy_config = {
#                 "server": f"http://{PROXY_HOST}:{port}",
#                 "username": PROXY_USERNAME,
#                 "password": PROXY_PASSWORD
#             }

#             browser = p.chromium.launch(headless=True, proxy=proxy_config)

#             context = browser.new_context(
#                 user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#             )

#             page = context.new_page()

#             url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location=India&f_TPR=r3600&sortBy=DD"

#             print("Searching:", keyword)
#             print("URL:", url)

#             page.goto(url, timeout=60000, wait_until="domcontentloaded")

#             for _ in range(5):
#                 page.mouse.wheel(0, 3000)
#                 page.wait_for_timeout(1000)

#             cards = page.query_selector_all(".base-search-card")

#             print("Cards found:", len(cards))

#             for c in cards[:20]:

#                 try:
#                     title_el = c.query_selector(".base-search-card__title")
#                     company_el = c.query_selector(".base-search-card__subtitle")
#                     location_el = c.query_selector(".job-search-card__location")
#                     link_el = c.query_selector("a.base-card__full-link")
#                     date_el = c.query_selector("time")

#                     title = title_el.inner_text().strip() if title_el else ""
#                     company = company_el.inner_text().strip() if company_el else ""
#                     location = location_el.inner_text().strip() if location_el else ""
#                     url = link_el.get_attribute("href") if link_el else ""
#                     date_posted = date_el.inner_text().strip() if date_el else ""

#                     job_type_val = "On-site"

#                     loc_lower = location.lower()

#                     if "remote" in loc_lower:
#                         job_type_val = "Remote"
#                     elif "hybrid" in loc_lower:
#                         job_type_val = "Hybrid"

#                     jobs.append({
#                         "source": "linkedin_job",
#                         "title": title,
#                         "company": company,
#                         "location": location,
#                         "date_posted": date_posted,
#                         "job_type": job_type_val,
#                         "url": url,
#                         "about": f"{title} role at {company} located in {location}"
#                     })

#                 except:
#                     continue

#             browser.close()

#     except Exception as e:
#         print("Scraper error:", str(e))

#     print("Jobs extracted:", len(jobs))

#     return jobs



from playwright.sync_api import sync_playwright
import random
import time

PROXY_USERNAME = "api5e199d7fe393aaf2"
PROXY_PASSWORD = "RNW78Fm5"
PROXY_HOST = "us.res.proxy-seller.com"
PORTS = list(range(10001, 10120))


def search_jobs(keyword, website, job_type="job"):

    jobs = []

    if website != "linkedin" or job_type != "job":
        return []

    retries = 3

    for attempt in range(retries):

        try:
            with sync_playwright() as p:

                port = random.choice(PORTS)

                proxy_config = {
                    "server": f"http://{PROXY_HOST}:{port}",
                    "username": PROXY_USERNAME,
                    "password": PROXY_PASSWORD
                }

                browser = p.chromium.launch(
                    headless=True,
                    proxy=proxy_config,
                    args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
                )

                context = browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                )

                page = context.new_page()

                url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location=India&f_TPR=r3600&sortBy=DD"

                print(f"\nAttempt {attempt+1} | Searching: {keyword}")
                print("URL:", url)

                page.goto(url, timeout=60000, wait_until="domcontentloaded")

                page.wait_for_timeout(4000)

                # Scroll to load jobs
                for _ in range(6):
                    page.mouse.wheel(0, 4000)
                    page.wait_for_timeout(1500)

                cards = page.query_selector_all(".base-search-card")

                print("Cards found:", len(cards))

                if len(cards) == 0:
                    browser.close()
                    time.sleep(2)
                    continue  # retry

                for c in cards[:20]:

                    try:
                        title_el = c.query_selector(".base-search-card__title")
                        company_el = c.query_selector(".base-search-card__subtitle")
                        location_el = c.query_selector(".job-search-card__location")
                        link_el = c.query_selector("a.base-card__full-link")
                        date_el = c.query_selector("time")

                        title = title_el.inner_text().strip() if title_el else ""
                        company = company_el.inner_text().strip() if company_el else ""
                        location = location_el.inner_text().strip() if location_el else ""
                        job_url = link_el.get_attribute("href") if link_el else ""
                        date_posted = date_el.inner_text().strip() if date_el else ""

                        job_type_val = "On-site"

                        loc_lower = location.lower()
                        if "remote" in loc_lower:
                            job_type_val = "Remote"
                        elif "hybrid" in loc_lower:
                            job_type_val = "Hybrid"

                        jobs.append({
                            "source": "linkedin_job",
                            "title": title,
                            "company": company,
                            "location": location,
                            "date_posted": date_posted,
                            "job_type": job_type_val,
                            "url": job_url,
                            "about": f"{title} role at {company} located in {location}"
                        })

                    except:
                        continue

                browser.close()

                if jobs:
                    break

        except Exception as e:
            print("Scraper error:", str(e))
            time.sleep(2)

    print("Jobs extracted:", len(jobs))
    return jobs