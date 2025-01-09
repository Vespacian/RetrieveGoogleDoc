import requests

def decode_message(url):
    r = requests.get(url)
    if r.status_code == 200:
        text = r.text
        # print(raw)
        lines = text.splitlines()
        # print(lines[0])
        print(r.cookies)
        print(r.history)
    else:
        print("Can't access doc :(")
    
    # parse url
    # rows = max(url.x)
    # cols = max(url.y)
    # grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # for row in url:
    #     grid[row.x][row.y] = row.character
    
    # # process data
    # message = ""
    # for row in grid:
    #     for col in row:
    #         message[row][col] = grid[row][col]
            
    # # print
    # if message == "":
    #     raise NotImplementedError("Empty message! Should parse URL before printing message!")
    # else: 
    #     print(message)

url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
decode_message(url)