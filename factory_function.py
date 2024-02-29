def fetch_factory(url): # Enclosed function
    if url.startswith("http:"):
        def fetch_page():   # Inner-function / Nested-function
            print("Fetching a page using HTTP protocol!")
    elif url.startswith("https:"):
        def fetch_page():
            print("Fetching a page using HTTPS protocol!")
    elif url.startswith("ftp:"):
        def fetch_page():
            print("Downloading a file using FTP protocol!")
    else:
        def fetch_page():
            print("Cannot understand this protocol!")

    return fetch_page

fn1 = fetch_factory("http://slashprog.com/")
fn2 = fetch_factory("https://python.org/")
fn3 = fetch_factory("ftp://ftp.gnu.org/")

fn1()
fn2()
fn3()
