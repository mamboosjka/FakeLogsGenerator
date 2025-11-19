import random
import datetime

users = [
    "SergeyD", "VladislavS", "DariaK", "EkaterinaG", "SvetlanaP", "VeronikaP"
]
ips = ["192.168.1.11", "192.168.1.14", "192.168.1.15", "192.168.1.16", "192.168.1.17", "192.168.1.19"]
methods = ["GET", "POST"]
endpoints = ["/profile", "/order", "/search", "/product", "/cart"]
codes = ["200", "302", "404", "500"]
referers = [
    "[https://google.com](https://google.com)",
    "[https://example.com/home](https://example.com/home)",
    "-",
    "[https://bing.com](https://bing.com)"
]
agents = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
]

messages = [
    '"Visited page"',
    '"Added product_id=101 qty=1"',
    '"Checkout"',
    '"Removed product_id=101"',
    '"Error loading page"'
]

def random_date():
    base = datetime.datetime(2025, 11, 13, random.randint(0,23), random.randint(0,59), random.randint(0,59))
    return base.strftime('%Y-%m-%dT%H:%M:%SZ')

def make_log_line():
    date = random_date()
    user = random.choice(users)
    ip = random.choice(ips)
    method = random.choice(methods)
    endpoint = random.choice(endpoints)
    code = random.choice(codes)
    referer = random.choice(referers)
    agent = random.choice(agents)
    msg = random.choice(messages)
    return f"{date} {user} {ip} {method} {endpoint} {code} {referer} {agent} {msg}"

with open("fake_logs.txt", "w", encoding="utf-8") as f:
    for _ in range(1000):
        f.write(make_log_line() + "\n")
