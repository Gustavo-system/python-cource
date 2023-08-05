import re

req = re.compile(r'ab', re.IGNORECASE)

print(req.search('elabacometodonumerico'))
print(req.search('elabacometodonumerico').group())