from notion.client import NotionClient
from notion.block import TextBlock, SubheaderBlock

import writeas

def w2n(url, id):
# Setting up Notion client
# Put in your token here
    token = ""
    client = NotionClient(token_v2=token)

# Setting up Write.as client
    c = writeas.client()

# Get Notion page url
    page = client.get_block(url)

# Get Write.as post
    post = c.retrievePost(id)
    body = post['body']
    title = post ['title']


# Adds the Write.as post title to Notion page
    if title != '':
        page.children.add_new(SubheaderBlock, title=title)


# Add the Write.as post body to the Notion page by adding a new block
    new = page.children.add_new(TextBlock, title=body)

    return new
