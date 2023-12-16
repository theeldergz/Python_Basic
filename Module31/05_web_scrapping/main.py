import re

# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
    print(re.findall(r'<h3>(.*)</h3>', text))
# По итогу вы так же получаете код сайта в виде одной строки
