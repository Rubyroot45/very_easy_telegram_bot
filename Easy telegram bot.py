import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = 'Your_token'

logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Мокап данных музеев (в реальном боте данные могут быть из базы данных или API)
museums_data = {
    "museum1": {
        "title": "Курганский областной художественный музей",
        "image_url": "https://static.vmuzey.com/museum/986179288167946/7579e17f44136fa3-w295-h165.jpg",
        "description": "Курганский областной художественный музей им. Г.А. Травникова открыт в 1982 году. В 2020 году музею присвоено имя Народного художника России, Почетного гражданина Курганской области Германа Алексеевича Травникова.В музейных фондах хранятся более 10 тысяч произведений живописи, графики, скульптуры, декоративно-прикладного искусства, иконописи, рукописных и старопечатных книг. Это образцы классического отечественного искусства с начала ХХ века до первых десятилетий ХХI века, в том числе произведения авторов бывших республик СССР. Раздел религиозного искусства включает в себя экспонаты XVIII – начала XX веков. В коллекциях русской оригинальной и печатной графики хранятся произведения XIX – начала XX столетий. Примерно треть собрания представляет искусство художников Курганской области.",
        "phone_number": "https://go.2gis.com/iojvt",
        "events_url": "https://vmuzey.com/museum/kurganskiy-oblastnoy-hudozhestvennyy-muzey"
    },
    "museum2": {
        "title": "Курганский областной краеведческий музей",
        "image_url": "https://static.vmuzey.com/museum/351652944401644/cdc0ff0f44136fa3-w295-h165.jpg",
        "description": "Курганский областной краеведческий музей основан 10 ноября 1951 года. Это дата открытия первой экспозиции. В течение сорока лет музей располагался в здании Александро-Невской церкви, с 1991 года по настоящее время он занимает здание бывшего Дома политпросвещения. В 2011 году для посетителей вновь открылся планетарий, который появился в Кургане в 1957 году.Музей насчитывает около 200 тысяч экспонатов, 40 музейных коллекций. Это самое крупное в регионе хранилище историко-культурных и естественно-научных коллекций.В настоящее время в музее работают постоянные экспозиции отделов истории и природы, проводятся тематические выставки. Наряду с традиционными формами работы, сотрудники музея активно практикуют интерактивные и комбинированные экскурсии с мастер-классами и элементами театрализации, квест-экскурсии, а также виртуальные выставки.",
        "phone_number": "https://go.2gis.com/do17y",
        "events_url": "https://vmuzey.com/museum/kurganskiy-oblastnoy-kraevedcheskiy-muzey"
    },
        "museum3": {
        "title": "Дом-музей декабристов",
        "image_url": "https://static.vmuzey.com/museum/807903302672765/c37515a544136fa3-w295-h165.jpg",
        "description": "Дом-музей декабристов открылся в Кургане 10 декабря 1975 года. Здание музея – объект культурного наследия федерального значения. В 1833-1837 гг. в этом доме жил декабрист М.М. Нарышкин со своей семьей. После подавления восстания на Сенатской площади он был осужден на каторжные работы, а в марте 1833 года с женой Елизаветой Петровной, разделившей его участь, прибыл на поселение в Курган. Дом, в котором поселилась семья, был одним из самых больших и богатых домов уездного города. Здесь собирались ссыльные декабристы, проходили дружеские встречи, музыкальные вечера. В музее собраны материалы о 13 декабристах, находившихся на поселении в Кургане с 1830 по 1857 гг. Его экспозиция содержит более 600 подлинных предметов дворянского быта XIX века. По письмам Е.П. Нарышкиной воссозданы интерьеры столовой, гостиной, кабинета хозяина и комнаты хозяйки дома.",
        "phone_number": "https://go.2gis.com/w4e4d",
        "events_url": "https://vmuzey.com/museum/dom-muzey-dekabristov"
    },
        "museum4": {
        "title": "Дом-музей В.К.Кюхельбекера",
        "image_url": "https://static.vmuzey.com/museum/569812934960524/3dffe43a44136fa3-w295-h165.jpg",
        "description": "Дом-музей В.К. Кюхельбекера в Кургане был открыт 13 декабря 2005 года. Это единственный в России музей, посвященный памяти декабриста, поэта, лицейского друга А.С. Пушкина. Здание музея – точная копия дома, где Вильгельм Карлович Кюхельбекер (1797 – 1846 гг.) с семьей проживал в курганской ссылке с сентября 1845 по март 1846 года.Экспозиция музея рассказывает о семье, детстве, лицейских годах Кюхельбекера, его участии в событиях 14 декабря 1825 года, пребывании в крепостях Прибалтики и Сибири, раскрывает ранее неизвестные факты из жизни декабриста и его семьи.В мемориальном музее восстановлены исторические интерьеры гостиной, кабинета, кухни-столовой, создающие атмосферу присутствия поэта и декабриста Кюхельбекера. Большой интерес представляют подлинные предметы того периода: кресло-гондола в стиле «ампир», кабинетный фонарь из молочного стекла «ампли» с ручной росписью, дорожный сундук-кофр и многое другое.",
        "phone_number": "https://go.2gis.com/yzofq",
        "events_url": "https://vmuzey.com/museum/dom-muzey-v-k-kyuhelbekera"
    },
        "museum5": {
        "title": "Музей истории города Кургана",
        "image_url": "https://static.vmuzey.com/museum/965089338312597/a8fb3e3244136fa3-w295-h165.jpg",
        "description": "Музей истории города открылся в Кургане 18 мая 2006 года, в особняке, ранее принадлежавшему купцу  первой гильдии Семёну Ивановичу Березину, а затем его сыну Фёдору.Здание музея с прилегающей территорией – объект культурного наследия регионального значения. Вместе с надворными постройками оно представляет собой образец городской усадьбы второй половины XIX века,построенной в стиле русского классицизма. В начале ХХ века усадьба Березиных была куплена городом под окружное казначейство.В экспозиции музея представлены этапы развития г. Кургана, начиная с его основания в 1679 году как слободы Царёво городище до 1917 года. Отдельные комплексы посвящены купеческим семьям, основавшим крупные промышленные и торговые предприятия. Важное место в экспозиции музея отводится истории народного образования, здравоохранения, городской культуры.Экспозиция содержит более 450 предметов XIX - начала ХХ веков. Воссозданы фрагменты подлинных интерьеров гостиной, кабинета купца, комнаты гувернантки.",
        "phone_number": "https://go.2gis.com/atykf",
        "events_url": "https://vmuzey.com/museum/muzey-istorii-goroda-kurgana"
    },
        "museum6": {
        "title": "Дом-музей Т.С.Мальцева",
        "image_url": "https://api.vmuzey.com/static/frame/museum/908005794637986/d63d31d8ea158472-w295-h165.jpg",
        "description": "Дом-музей Т. С. Мальцева открылся 3 августа 2000 года. Он посвящен жизни и деятельности выдающего российского полевода, селекционера и новатора сельского хозяйства, дважды Героя Социалистического Труда, почетного гражданина России Терентия Семеновича Мальцева (1895–1994). Открытие музея было приурочено к 50-летию Шадринской сельскохозяйственной опытной станции при колхозе «Заветы Ленина», которую более 40 лет возглавлял этот знаменитый деятель сельского хозяйства.Музей расположен в усадьбе, где в 1962–1994 годах Терентий Семенович жил и работал. Основная экспозиция размещена в бревенчатом доме, она включает интерьеры кухни, гостиной, кабинета и библиотеки. Большинство представленных экспонатов – это личные вещи Т. С. Мальцева – книги, мебель, бытовая утварь, одежда, а также памятные сувениры, подаренные ему от трудовых коллективов, школьников и различных организаций.",
        "phone_number": "https://go.2gis.com/1nf8w",
        "events_url": "https://vmuzey.com/museum/dom-muzey-t-s-malceva"
    },
    
}

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Приветствуем вас, друзья! Добро пожаловать в бота Курганского областного музейного объединения.С помощью бота вы можете купить билет и построить маршрут до каждого из наших музеев!")
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = []
    for key, value in museums_data.items():
        buttons.append(InlineKeyboardButton(value['title'], callback_data=key))
    keyboard.add(*buttons)
    await message.answer("! Выберите музей:", reply_markup=keyboard)

# Обработчик для выбора музея
@dp.callback_query_handler(lambda query: query.data in museums_data.keys())
async def process_museum(query: types.CallbackQuery):
    museum_id = query.data
    museum = museums_data[museum_id]
    keyboard = InlineKeyboardMarkup(row_width=3)
    buttons = [
        InlineKeyboardButton("Назад", callback_data="back"),
        InlineKeyboardButton("Как добраться?", url=museum['phone_number']),
        InlineKeyboardButton("Мероприятия", url=museum['events_url'])
    ]
    keyboard.add(*buttons)
    await bot.send_photo(query.from_user.id, museum['image_url'], caption=museum['description'], reply_markup=keyboard)

# Обработчик для кнопки "Назад"
@dp.callback_query_handler(lambda query: query.data == "back")
async def process_back(query: types.CallbackQuery):
    await query.message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
