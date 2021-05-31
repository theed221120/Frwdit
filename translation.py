import os
from config import Config

class Translation(object):
  START_TXT = """<b>ഹലോ🙃 {}!!</b>
<i>Only one thing counts in this life – get them to sign on the line that is dotted 😁😁 I'm Simple Auto file Forward Bot
This Bot forward all files to One Public channel to Your Personal channel
More details /help</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>Follow These Steps!!</b>
<b>• Currectly fill your Heroku Config vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>
<b>• Then give admin permission in your personal telegram channel</b>
<b>• Then send any message In your personal telegram channel</b>
<b>• Then use /run command in your bot നിനക്ക് പറ്റുമോ എന്ന് ചുമ്മാ നോക്ക് 😉</b>

<b><u>Available Command</b></u>

* /start - <b>ബോട്ടിന് ജീവൻ ഉണ്ടോ എന്ന് നോക്കാന്‍</b>
* /help - <b>നിനക്ക് വല്ല സംശയവും ഉണ്ടെങ്കില്‍ നോക്കാന്‍</b>
* /run - <b>start forward</b>
* /about - <b>ഞാൻ ആരാണ് എന്താണ് എന്ന് അറിയാൻ</b>"""
  ABOUT_TXT = """<b><u>My Info</b></u>

<b>Name :</b> <code>File Forward SOMAN</code>
<b>Credit :</b> <code>@hsk_the_editor</code>
<b>Language :</b> <code>Python3</code>
<b>Lybrary :</b> <code>Pyrogram v1.2.9</code>
<b>Server :</b> <code>Heroku</code>
<b>Build :</b><code>V0.1</code>"""
