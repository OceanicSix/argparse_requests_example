import json

import requests
from bs4 import BeautifulSoup
import argparse

def get_html(url,proxies=None):
    if proxies:
        try:
            input_list=proxies.split(":")
            proxies={input_list[0]:proxies}
        except:
            print("Invalid proxy syntax")
            exit(-1)

    session = requests.session()
    response = session.get(url, proxies=proxies)
    if response:
        return response.text

def get_link(html):
    soup_obj=BeautifulSoup(html,'html.parser')
    link_dict = {"a": [], "link": [], "iframe": [], "script": [], "img": []}
    for tag in soup_obj.find_all(["a", "link", "iframe", "script", "img"]):
        if tag.has_attr("href"):
            link = tag["href"]
            if link and link[0] != "#" and link[0] != "?" and link not in link_dict[tag.name]:
                 link_dict[tag.name].append(link)

        elif tag.has_attr("src"):
            src = tag["src"]
            if src and src not in link_dict[tag.name]:
                link_dict[tag.name].append(src)
    return link_dict


def recursive(url, base_url,
              record=[]):  # using record to pass data along with the recursion----record all visited link
    print("current url to request is ", url)
    print("visit record is ", record)
    links = get_link(get_html(url))
    href_links = links["a"]
    print("request links are", href_links)

    for link in href_links:
        if link == "/":
            continue

        # for link like "/static"
        if link[0] == "/":
            if base_url + link.lstrip("/") not in record:
                record.append(base_url + link.lstrip(
                    "/"))  # get rid of leftside of "/", so won't form link like example.com//static/
                recursive(base_url + link.lstrip("/"), base_url, record)
            else:
                continue

        # for normal link like index.html
        elif link[-1] != "/" and url + link not in record:
            record.append(url + link)
            print("appended link is ", link)
            recursive(url, base_url, record)

        # for the link like static/
        if link[-1] == "/" and url + link not in record:
            record.append(url + link)
            recursive(url + link, base_url, record)  # change the request url to /static/




def main():
    url=args.url
    html=get_html(url,args.proxy)
    links=get_link(html)

    print(json.dumps(links,indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A web crawler")

    parser.add_argument("-u", "--url", help="URL of the target website", required=True)
    parser.add_argument("-x", "--proxy",
                        help="Specify a proxy in the format of Protocol://IP:Port such as http://127.0.0.1:8080")

    args = parser.parse_args()
    main()
    #print('-'*50)
    #recursive("http://www.pentest.com:49153/web/", "http://www.pentest.com:49153/web/")