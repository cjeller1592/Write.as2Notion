# Write.as2Notion

This is boilerplate code that allows you to send over Write.as posts to a Notion page.

## Getting Started

1) Clone the repo and download the dependencies.

```
pip install -r requirements.txt
```

2) Log into your Notion account and go into the cookies under 'www.notion.so'. Find 'token_v2', copy the content, and paste it into the token variable.

3) Now you can get to work! 

## What You Need

- Url of the Notion page you want to send the Write.as post to (ex: https://www.notion.so/Test-Page-e8bf914efe91492dbbb8ecae363f3b83)

- The id of the Write.as post you want to make into a Notion page (ex: v88k50vi62va8fyp)

## Putting It Together

```
>>> url = 'https://www.notion.so/Test-Page-e8bf914efe91492dbbb8ecae363f3b83'
>>> id = 'v88k50vi62va8fyp'
>>> h2a(url, id)
>>><TextBlock (id='dff359a0-c2c5-4191-b412-3ec231dbd24a', title='There is another aspect of Isaac Newton calling his notebook a waste book that I forgot to mention...'
```

Feel free to use in the console or to import into a project. Big thanks to Write.as and [notion-py](https://github.com/jamalex/notion-py)!
