Repository: **minecraft-python**  
short URL: [tinyurl.com/github-andr](https://tinyurl.com/github-andr)

# Подготовка компьютера к программированию на Python 3 в Minecraft

## Создание учетной записи на компьютере

Если у вас еще есть учетная запись с правами **администратора**, она на **английском языке** и не содержит **пробелов**, то можете переходить к Установке программного обеспечения.

*Инструкция для `Windows 10`*

1. Входим под учетной записью с правами администратора
2. Запускаем проводник и на **Мой компьютер** кликаем правой клавишей мыши - **Управление**
3. Слева выбираем **Локальные пользователи** - **пользователи**
  * Справа в пустом месте правой клавишей мыши **Новый пользователь**
  * Имя пользователя на английском языке без пробелов, например **developer**
  * Задаем пароль и подтверждаем его
  * Убираем галочку **Требовать смены пароля**
  * Ставим галочку ***Срок действия пароля не ограничен* 
  * Нажимаем **Создать**
4. Заходим в свойства пользователя двойным кликом по имени пользователя или правой клавишей мыши и свойства
  * Переходим во вкладку **Членство в группах**
  * Нажимаем **Добавлить**
  * Снизу слева **Дополнительно**
  * Справа по центру **Поиск**
  * В нижней части окна находим и выбираем **Администраторы**
  * Нажимаем **ОК** и в следующем окне **ОК**
  * Видим в верхней части окна член групп: **Администраторы** и **Пользователи**
  * Нажимаем на **Пользователи** и снизу слева **Удалить** и **ОК**
5. Выходим из текущей учетной записи или перезагружаем компьютер
6. Входим под только что созданной учетной записью (**programmer**)


## Устанавливаем необходиомое программное обеспечение:

1. Устанавливаем [Java 8](https://java.com/en/download/windows_manual.jsp)
2. Устанавливаем [Python 3.9.x](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe) + ставим галочку **add Path**!
3. Устанавливаем редактор кода [vscode](https://code.visualstudio.com/docs/setup/windows)
4. Скачиваем Minecraft сервер. [Ссылка на архив](https://tinyurl.com/minesrv)
  * Распаковываем архив в Документы
5. Устанавливаем ([TLauncher](https://tlauncher.org/))
6. Перезагружаем компьютер


## Запускаем сервер Minecraft и подключаемся к нему

1. Запускаем **TLauncher**
2. Выбираем имя пользователя в Майнкрафт, например **gamer**
3. В TLauncher выбираем версию Minecraft **1.12.2**
4. Нажимаем **Установить**
5. После установки запускаем игру
6. Запускаем **Проводник** и переходим к распакованному коду в папке **Документы**
7. В папке **PythonMinecraft** запускаем сервер Maincraft выполнив файл **ServerStart.bat**
8. После появления сообщения **Done** в черном окне переходим в игру Minecraft
  * Выбираем **Сетевая игра**
  * **Подключиться к серверу**
  * Адрес сервера пишем: **localhost** и жмем **ОК**
  * Должно появиться сообщение об успешном подключении в Minecraft и в черном окне


## Первый код на Python в Minecraft

1. Запускаем **Visual Studio Code** (vscode)
2. Нажимаем **File** - **Open Folder** (файл - открыть папку)
3. Переходим в **Документы** - папку **PythonMinecraft** - **code** - **!MyCode** и нажимаем **ОК**
4. `! На данный момент уже должен быть запущен сервер Манкрафт и в игре вы должны быть подключены к этому серверу`
5. Слева выбирайте файл **firstCode.py** - откроется код на Python справа
6. Снизу справа vscode предложит установить расширение для Python - Устанавливайте!
  * Расширение для Python можно установить из левой панели в vscode
  * Нажмите на **квадратики *(Extensions)** в левой части окна vscode
  * Наберите **python** в открывшейся строке поиска
  * Установите **Python** IntelliSense от Microsoft кнопкой **Install**
7. Перейдите в окно кода **firstCode.py** и нажмите сверху **Run** - **Start Debugging**
  * Если ошибка mcpi, то в терминале выполняем:
  * `pip install mcpi`
  * Запускаем еще раз скрипт (**F5**)
8. Должны увидеть координаты игрока из Майнкрафт в терминале и чате игры


## При возникновении ошибок

Если у вас возникли проблемы, то перейдите в файл [**troubleshooting.md**](troubleshooting.md).  
Здесь собраны возможные решения при возникновении ошибок.  
**Файл будет пополняться по мере нахождения новых.**
