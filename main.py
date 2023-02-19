import gettext

# Set up localization support for English
# gettext.bindtextdomain('myapp', 'locale/en/LC_MESSAGES')
gettext.bindtextdomain('myapp', 'locale/en')
gettext.textdomain('myapp')

# Get the translation for the phrase "name"
name_translation = gettext.gettext('name')

# Get the translation for the phrase "number of dollars"
money_translation = gettext.gettext('number of dollars')

# Get the translation for the phrase "satiety"
satiety_translation = gettext.gettext('satiety')

# Get the translation for the phrase "level"
level_translation = gettext.gettext('level')

# Get the translation for the phrase "love"
love_translation = gettext.gettext('love')
print(money_translation)  # should print "groši"
# print(money_translation)
