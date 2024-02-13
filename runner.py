# This is my test project form skills demonstration
import webbrowser

from main import Main
from Auth.auth import Authorization
from ContactUs.contactUs import ContactForm
from multiprocessing import Pool
from multiprocessing import Process
import constants as const


def execute_tasks(_):
    try:

        with Main() as bot:
            bot.land_first_page()
            bot.apply_registration()
            bot.apply_contactus()
            bot.close()
            bot.quit()
            input("Press Enter to finish...")

    except Exception as e:
        if 'in PATH' in str(e):
            print(
                'You are trying to run the bot from command line \n'
                'Please add to PATH your Selenium Drivers \n'
                'Windows: \n'
                '    set PATH=%PATH%;C:path-to-your-folder \n \n'
                'Linux: \n'
                '    PATH=$PATH:/path/toy-our/folder/ \n'
            )
        else:
            raise


if __name__ == '__main__':
    process_count = 3
    p = Pool(processes=process_count)
    p.map(execute_tasks, const.BASE_URL)

    # try:
    # with Main() as bot:
    #    bot.land_first_page()
    #     bot.apply_registration()
    #      bot.apply_contactus()
    #       input("Press Enter to finish...")