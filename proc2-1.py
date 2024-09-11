from epics import camonitor, camonitor_clear
import telebot

bot = telebot.TeleBot('...')


def notify(pvname, value, **_):
    bot.send_message('...', f"`{pvname}` is now set to `{value}`;", 'MarkdownV2')


print('init done')
try:
    print('monitor start')
    camonitor('t1:aval', callback=notify)
    bot.polling()
finally:
    camonitor_clear('t1:aval')
    bot.stop_bot()
    print('monitor clear, exiting')

print('END')
