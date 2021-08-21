import datetime



def get_entry():

    global deposit
    global entry_source

    entry_type = input('====Specify the type of entry:==== \n1. Money\n2. Other(detail)\n -->')
    if entry_type == '1':
        deposit = input('Amount in MAD: ')
        entry_source = input('Description of the source of the money(max. 250 characters): ')

    elif entry_type == '2':
        deposit = input('Precise what has been acquired(max. 250 characters): ')
        entry_source = input('Explain from where it came(e.g donation/purchase):')

    else:
        print('Please choose either 1 or 2.')
    
    return deposit, entry_source


def withdraw():
    
    global out
    global withdrawal_reason

    withdraw_type = input('====Specify the type of withdrawal:==== \n1. Money\n2. Other(detail)\n -->')
    if withdraw_type == '1':
        out = input('Amount in MAD: ')
        withdrawal_reason = input('Explain the reason(max. 250 characters): ')

    elif withdraw_type == '2':
        out = input('Code of the deposit to withdraw: ')
        withdrawal_reason = input('Explain the reason(max. 250 characters): ')
    
    else:
        print('Please choose either 1 or 2.')

    return out, withdrawal_reason


def run():
    while True:
        action = input('Choose an action: \n1. Deposit\n2. Withdraw\n3. Quit\n -->')
        if action == '1':
            get_entry()
            data = f'{datetime.datetime.now()} | {deposit} | 0 | {entry_source} \n'
            with open('logs.txt', 'a+') as log:
                log.write(data)
        elif action == '2':
            withdraw()
            data = f'{datetime.datetime.now()} | 0 | {out} | {withdrawal_reason} \n'
            with open('logs.txt', 'a+') as log:
                log.write(data)

        elif action == '3':
            break

        else:
            print('check')
            print('Please choose 1 or 2.')
    

if __name__ == '__main__':
    run()

    


