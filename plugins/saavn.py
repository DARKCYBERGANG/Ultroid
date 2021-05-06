# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}saavn <search query>`
   `search song on saavn`
"""

from . import *
from telethon.tl.types import DocumentAttributeAudio
import requests as r
from urllib.request import urlretrieve
import time

@ultroid_cmd(pattern='saavn ?(.*)')
async def siesace(e):
    song = e.pattern_match.group(1)
    if not song:
    	return await eod(e, '`Give me Something to Search')
    hmm = time.time()
    lol = await eor(e, "`...`")
    sung = song.replace(' ', '%20')
    url = f"https://jostapi.herokuapp.com/saavn?query={sung}"
    k = (r.get(url)).json()
    m = []
    for x in k:
        m.append({'title': x['song'], 'url': x['media_url'], 'img': x['image'], 'duration': x['duration'], 'singers': x['singers']})
    urlretrieve(m[0]['url'], m[0]['title']+".mp3")
    urlretrieve(m[0]['img'], m[0]['title']+".jpg")
    okk = await uploader(m[0]['title']+".mp3", m[0]['title']+".mp3", hmm, lol, "Uploading")
    await ultroid_bot.send_file(e.chat_id, okk,attributes=[DocumentAttributeAudio(duration=int(m[0]['duration']), title=m[0]['title'], performer=m[0]['singers'])], supports_streaming=True, voice_note=True, thumb=m[0]['title']+".jpg")
    await lol.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
