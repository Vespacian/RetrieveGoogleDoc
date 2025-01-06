import requests

def decode_message(url):
    response = requests.get(url)
    if response.status_code == 200:
        raw = response.text
        # print(raw)
        lines = raw.splitlines()
        print(lines[1])
    else:
        print("Failed to fetch the document.")
    
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