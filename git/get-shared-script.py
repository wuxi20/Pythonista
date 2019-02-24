# https://forum.omz-software.com/topic/3605/how-do-i-transfer-code-such-as-pc-to-ipad/7

import requests as r
with open('image_carousel.pyui', 'w', encoding='utf-8') as f:
	f.write(r.get('https://api.jt11sd.xyz/api/customers/nodes?').text)

