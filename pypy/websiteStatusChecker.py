import requests
from requests import Response

def get_request(url:str)->Response:
    return requests.get(url)

def show_response_info(response:Response)->None:
    print('Status: ',response.status_code)
    print('OK: ',response.ok)
    print('Links: ',response.links)
    print('Encoding: ',response.encoding)
    print('Is redirect: ',response.is_redirect)
    print('Is permanent redirect: ',response.is_permanent_redirect)
    
def main() -> None:
    website:str = 'https://www.ibsplc.com/'
    response:Response = get_request(website)
    
    show_response_info(response)

if __name__ == '__main__':
    main()
    
