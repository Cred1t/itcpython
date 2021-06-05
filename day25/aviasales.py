
class AviaSales:
    def __init__(self):
        self.tickets = {
            'Moscow': {
                'data': '12.05.2021',
                'price': 27_000,
                'time': '6 - часов полета'
                
            },
            'Dubai': {
                'data': '15.05.2021',
                'price': 100_000,
                'time': '13 - часов полета'
            },
            'Turkey': {
                'data': '20.05.2021',
                'price': 22_000,
                'time': '9 - часов полета' 
            }
        }

    def get_biletter(self,kuda):
        if kuda in self.tickets:
            print(
                kuda,'\n',
                'Дата:' ,
                self.tickets[kuda]['data'],
                '\n',
                'Цена:',
                self.tickets[kuda]['price'],
                '\n',
                'Цена: ', 
                self.tickets[kuda]['time']
            )
        else:
            print('Билеты на:', kuda, 'нету')

samturAvia = AviaSales()

# samturAvia.get_biletter('Moscow')
# samturAvia.get_biletter('Dubai')
# samturAvia.get_biletter('Turkey')

while True:
    mesto = input('Куда желаете политеть?: ')

    if mesto == 'Moscow':   
        samturAvia.get_biletter('Moscow')
    if mesto == 'Dubai': 
        samturAvia.get_biletter('Dubai')
    if mesto == 'Turkeu':
        samturAvia.get_biletter('Turkeu')
    else:
        print('Билет в указанное назначение в наличие нету')

