#Клавиатура
import telebot

language_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
language_keyboard.row("RU", "EN")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Категории каналов', 'Добавить канал')


keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.add('Блоги', 'Юмор и развлечения', 'Бизнес и стартапы', 'Музыка','Новости и СМИ','Криптовалюты','Продажи','Здоровье и Спорт','Искусство и фото','Образование','Политика','Технологии','Путешествия','Маркетинг,PR,реклама','Видео и фильмы','Психология',
              'Мода и красота','Игры и приложения','Книги','Цитаты','Еда и кулинария','Позновательное','Авто','Экономика','Карьера','Лингвистика','Религия','Дизайн','Каталог каналов и ботов',
              'Telegram','Семья и дети','Медицина','Животные','Рукоделие','Лайфхаки','Каталоги стикеров','Для взрослых','Другое')
keyboard2.add('Назад', 'Вернуться в главное меню')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.add('1-500 под', '500-1k', '1k-5k', '5k-10k', '10k-20k',  '20k-50k','50k-100k','100k-500k','500k-1kk')
keyboard3.add('Назад', 'Вернуться в главное меню')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.add('Назад','Заказать')
keyboard4.add('Вернуться в главное меню')

keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.add('Назад','Как добавить бота')

keyboard10 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard10.add('Сhannel categories', 'Add channel')