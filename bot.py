import telebot
from telebot import types

donates = {
    'centaur': '''Полу-кони, полу-люди. <u>Кентавр</u>ы - дикий народ, обитающий в лесах,
как следствие - являются прекрасными охотниками, крайне суеверны.''',
    'griffin': '''Тело льва, крылья, голова и когти орла - всё это делает <u>Грифон</u>а
смертоносным и бесстрашным хищником, обитающим в горах.''',
    'chimera': '''Ужасное и беспощадное чудовище, порожденное Тифоном и Ехидной,
львиная голова, туловище козы, хвост в виде змеи. Огнедышащая
<u>Химера</u> была последним, что увидели многие путники.''',
    'pegasus': '''Прекрасный сияюще-белый конь с колоссально мощными крыльями.
<u>Пегас</u> - идеальное сочетание ослепительной красоты и огромной силы.''',
    'minotaur': '''Ярость в его глазах не потухла, даже после смерти.
Его неутолимый голод погубил множество невинных душ,
растерзанных в недрах Критского лабиринта. <u>Минотавр</u> - жестокое 
порождение самой смерти.''',
    'basilisk': '''Огромный змей с бритвенно острыми клыками, взглядом, настолько
устрашающим, что те кто его испытали, уже не могут ничего поведать.
Само название "<u>Василиск</u>" внушает ужас в сердца могучих держав.''',
    'cerberus': '''Трехглавый пес, достойный в одиночку охранять выход в царство
бога смерти. Его желание растерзать любого, кто посегнет на
выход из этого темного мира сочетается с игривым нравом и
стальной верностью своему господину. <u>Цербер</u> стал причиной
смерти многих отчаянных глупцов, зашедших на его территорию.''',
    'hydra': '''Множество голов лишало героев надежды на победу в поединке,
регенеративные способности сводили с ума великих алхимиков.
Почти бессмертный и непобедимый монстр,
терроризировавший Лерну. <u>Гидра</u> - символ выносливости,
стойкости и адаптации.''',
    'hercules': '''Бесстрашный герой, полубог, сын Зевса. Великий воин, обученный
лучшими: Хироном, Автоликом, Эвритом, Кастором. <u>Геракл</u> - 
рожденный в Фивах спаситель человечества от гнета ужасных
чудовищ.''',
    'titan': '''Орудующие грубой силой, не ведующие разума и меры
разрушители миров. Их не смогла покорить даже сама природа.
Многие величайшие империи ждал скоропостижный закат
по их воле. <u>Титан</u>ы - сгустки чистой злобы и могущества,
способные составить конкуренцию самим богам.''',
    'hephaestus': '''Искусный кузнец, покровитель изобретений, строитель прекрасного
пристанища богов. Мастер на все руки, изготовивший молнии Зевса.
Хранитель огня, сброшенный с Олимпа за помощь своей матери - Гере.
Сын верховного бога, главного в большой тройке. Повелитель
непотухаемой ярости и гнева вулканов - <u>Гефест</u>.''',
    'kronos': '''Его кровожадность не имела границ. Он был порождением злобы
и жестокости. Растерзанный на кусочки, сброшенный в Тартар,
бессмертный титан. Вопрос его освобождения - дело времени.
Он будет ждать вечность, но когда дождется, когда этот
момент настанет, боги падут, золотой век возобновится.
Это будет знаменовать конец всему человечеству. Люди будут обречены
на вечные муки. И даже после смерти измученные души не смогут
упокоиться. Будут лишь титаны, <u>Кронос</u>, и вечная тьма...''',
    'hades': '''Могущественное порождение тьмы, хранитель душ грешников и
праведников. Ему подчинены все порождения мира мертвых.
При одном лишь желании способный поднять бесчисленную
непокоримую армию измученных душ, жаждущих крови. А
отказавшихся подчиняться стирающий бесжалостно, даже не
моргнув. Хранитель Тартара - глубочайшей бездны вечных
мук и страданий. Бог темного мира, куда зайти
легко, но вернуться можно только по воле его царя - <u>Аид</u>а,
одного из Большой Тройки.''',
    'poseidon': '''Покровитель морей и океанов, бескрайних пристанищ ужасных
монстров, обитающих в пучинах, куда не попадает свет, и
удивительных прекрасных созданий, радующих глаз. Отец
ужасающей Харибды - водного монстра, топившего
проплывающие корабли. Вспыльчивый колоссальный повелитель
циклопов, создатель волн и течений. Его гнев был страшен.
<u>Посейдон</u> - бог водных глубин, один из Большой Тройки.''',
    'zeus': '''Глава большой тройки, свергнувший Кроноса и давший людям надежду
на светлое будущее. Его воля - закон. Гордый и непокоримый
бессмертный сын богини земли. Создатель молний и покровитель штормов.
Он не терпит неподчинения, и не станет мелочиться, по шелчку пальцев
покарает всё человечество и обречёт его на вечные страдания. <u>Зевс</u>у
подконтрольно всё воздушное пространство.''',
    'olympian': '''Превзошедший бессмертных богов... <u>Человек</u>...''',
}

bot = telebot.TeleBot('6858717966:AAH1T1oIQ_tQSkiPtD7jwUuBaaVPdxO-1jY')  # bot token


@bot.message_handler(commands=['start'])
def start(input_message):  # input message contains all available data about user and message
    first_name, second_name = '', ''
    if input_message.from_user.first_name:
        first_name = input_message.from_user.first_name
    if input_message.from_user.last_name:
        second_name = input_message.from_user.last_name
    bot.send_message(input_message.chat.id, f"""
Здравствуйте, <b>{str(' '.join([first_name, second_name]).strip())}</b>!
Посмотреть список команд можно по нажатию кнопки 'Меню'
    """, parse_mode='html')  # send message function


@bot.message_handler(commands=['donate'])
def show_donates(input_message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    centaur = types.KeyboardButton('Кентавр')
    griffin = types.KeyboardButton('Грифон')
    chimera = types.KeyboardButton('Химера')
    pegasus = types.KeyboardButton('Пегас')
    minotaur = types.KeyboardButton('Минотавр')
    basilisk = types.KeyboardButton('Василиск')
    cerberus = types.KeyboardButton('Цербер')
    hydra = types.KeyboardButton('Гидра')
    hercules = types.KeyboardButton('Геракл')
    titan = types.KeyboardButton('Титан')
    hephaestus = types.KeyboardButton('Гефест')
    kronos = types.KeyboardButton('Кронос')
    hades = types.KeyboardButton('Аид')
    poseidon = types.KeyboardButton('Посейдон')
    zeus = types.KeyboardButton('Зевс')
    olympian = types.KeyboardButton('Олимпиец')
    markup.add(
        centaur,
        griffin,
        chimera,
        pegasus,
        minotaur,
        basilisk,
        cerberus,
        hydra,
        hercules,
        titan,
        hephaestus,
        kronos,
        hades,
        poseidon,
        zeus,
        olympian
    )
    bot.send_message(input_message.chat.id, text="Список донатов", reply_markup=markup)

    @bot.message_handler()
    def message_catch(input_message):
        match input_message.text:
            case 'Кентавр':
                bot.send_message(input_message.chat.id, f"<b>{donates['centaur']}</b>", parse_mode='html')
            case 'Грифон':
                bot.send_message(input_message.chat.id, f"<b>{donates['griffin']}</b>", parse_mode='html')
            case 'Химера':
                bot.send_message(input_message.chat.id, f"<b>{donates['chimera']}</b>", parse_mode='html')
            case 'Пегас':
                bot.send_message(input_message.chat.id, f"<b>{donates['pegasus']}</b>", parse_mode='html')
            case 'Минотавр':
                bot.send_message(input_message.chat.id, f"<b>{donates['minotaur']}</b>", parse_mode='html')
            case 'Василиск':
                bot.send_message(input_message.chat.id, f"<b>{donates['basilisk']}</b>", parse_mode='html')
            case 'Цербер':
                bot.send_message(input_message.chat.id, f"<b>{donates['cerberus']}</b>", parse_mode='html')
            case 'Гидра':
                bot.send_message(input_message.chat.id, f"<b>{donates['hydra']}</b>", parse_mode='html')
            case 'Геракл':
                bot.send_message(input_message.chat.id, f"<b>{donates['hercules']}</b>", parse_mode='html')
            case 'Титан':
                bot.send_message(input_message.chat.id, f"<b>{donates['titan']}</b>", parse_mode='html')
            case 'Гефест':
                bot.send_message(input_message.chat.id, f"<b>{donates['hephaestus']}</b>", parse_mode='html')
            case 'Кронос':
                bot.send_message(input_message.chat.id, f"<b>{donates['kronos']}</b>", parse_mode='html')
            case 'Аид':
                bot.send_message(input_message.chat.id, f"<b>{donates['hades']}</b>", parse_mode='html')
            case 'Посейдон':
                bot.send_message(input_message.chat.id, f"<b>{donates['poseidon']}</b>", parse_mode='html')
            case 'Зевс':
                bot.send_message(input_message.chat.id, f"<b>{donates['zeus']}</b>", parse_mode='html')
            case 'Олимпиец':
                bot.send_message(input_message.chat.id, f"<b>{donates['olympian']}</b>", parse_mode='html')


@bot.message_handler(commands=['website'])
def new_markup(input_message):
    markup = types.InlineKeyboardMarkup()
    website_link = types.InlineKeyboardButton(text='САЙТ', url='http://127.0.0.1:8080')
    markup.add(website_link)
    bot.send_message(input_message.chat.id, 'Пожалуйста, посетите наш сайт.', reply_markup=markup)


bot.polling(none_stop=True)  # constant bot running

