# Creates data base called database.db

import user, story

user.createTable()
story.createTable()

user.register('clara', 'pass', '???', '???')
user.register('alex', 'pss0', '???', '???')
user.register('235160223', 'asdf', '???', '???')
user.register('290895069', 'qwdfawefweer', '???', '???')

story.updateStory('title', 'clara', 'once upon a time')
story.updateStory('title', 'jiajie', 'there was a family')
story.updateStory('title1', 'alex', 'The sky was blue,')
story.updateStory('title', 'william', 'that lived in America.')
story.updateStory('title1', 'ur mom', 'which disgusts me')
