import concurrent.futures
# import urllib.request
import requests

# list of jobs
URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    # with urllib.request.urlopen(url, timeout=timeout) as conn:
    #     return conn.read()
    return requests.get(url).text

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))

# Results at End: use executor.map and use results
# Results as you goo: use executor.submit and iter on futures.as_completed
# Jobs dep graph
    # (A,B,C)->D->E: submit(A,B,C) and futures.wait(futures_jobs, ALL_COMPLETED) to comb_res
    # and then submit(D, comb_res)
    # D.add_done_callback(E)
# Multiple chained jobs. A1->A2.. B1->B2..
    # submit(a) from A1, B1, C1..
    # futures.as_completed() submit(a) from A2, B2, C2
# Do work until any one succeed
    # submit(a) from A1, B1, C1..
    # done, not_done = futures.wait(jobs, return_when=FIRST_COMPLED)
    # cancel all in not_done