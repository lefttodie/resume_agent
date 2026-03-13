import random
from playwright.sync_api import sync_playwright


# ===================== PROXY CONFIG =====================

PROXY_USERNAME = "api5e199d7fe393aaf2"
PROXY_PASSWORD = "RNW78Fm5"
PROXY_HOST = "us.res.proxy-seller.com"

PORTS = list(range(10001, 10020))


def get_proxy():

    port = random.choice(PORTS)

    proxy_url = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{port}"

    return {
        "server": f"http://{PROXY_HOST}:{port}",
        "username": PROXY_USERNAME,
        "password": PROXY_PASSWORD
    }


def search_jobs(keyword):

    jobs = []

    proxy = get_proxy()

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            proxy=proxy
        )

        page = browser.new_page()

        query = f"{keyword} jobs India"

        url = f"https://www.google.com/search?q={query}"

        page.goto(url)

        page.wait_for_timeout(4000)

        results = page.query_selector_all("h3")

        for r in results[:20]:

            title = r.inner_text()

            jobs.append(title)

        browser.close()

    return jobs