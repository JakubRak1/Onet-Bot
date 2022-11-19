from onetbot.onet import Onet

with Onet() as bot:
    try:
        bot.load_first_page()
        bot.accept_cookies()
        bot.go_to_login_section()
        bot.refresh()
        bot.log_in_account(login=input('Bot login to onet.pl account: \n'), password=input('Bot password to onet.pl '
                                                                                           'account: \n'))
        bot.refresh()
        bot.create_new_message_and_send(address=input('Address where to send message: \n'),
                                        topic_with_message=input('Topic along with message: \n'))
    except Exception as e:
        if 'in PATH' in str(e):
            print('Some error has accrued, please add path to your selenium drivers \n'
                  'You can do this by "set PATH=%PATH%;C:rest-of-path"')
        else:
            raise
