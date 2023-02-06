
from booking.booking import Booking

# inst = Booking()
# inst.land_first_page()

try:
    with Booking(teardown=False) as bot:
        
        bot.land_first_page()
        # bot.change_currency(currency='USD')
        bot.selecet_place_to_go('New York')
        bot.select_date(check_in_date='2023-02-13',
                        Check_out_date='2023-03-01')

        bot.select_adults(10)
        bot.click_search()
        bot.apply_filtration()
        # print(len(bot.report_results()))
        # bot.refresh()
        bot.report_results()



except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please ass to PATH your Selenium Drivers \n'
            'Windows: \n'
            '   set PATH=%PATH%;C:path-to-your-folder\n \n'
            'Linux: \n'
            '   PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise


