# Creates data base called database.db

import user, story

user.createTable()
story.createTable()

user.register('clara', 'pass', '???', '???')
user.register('alex', 'pss0', '???', '???')
user.register('235160223', 'asdf', '???', '???')
user.register('290895069', 'qwdfawefweer', '???', '???')

story.updateStory('Nice story', 'clara', 'Once upon a time')
story.updateStory('Nice story', 'jiajie', 'there was a family')
story.updateStory('title1', 'alex', 'The sky was blue,')
story.updateStory('Nice story', 'william', 'that lived in America.')
story.updateStory('title1', 'clara', 'like a crystal')
