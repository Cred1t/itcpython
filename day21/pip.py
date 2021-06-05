
import termcolor

termcolor.cprint(
    'Hacking',
    'red',
    attrs = ['concealed']
)

text = '{} + {} = {}'.format(10, 10, 10 + 10)

termcolor.cprint(text, 'red', attrs = ['concealed'])