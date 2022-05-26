Repository: minecraft-python  
short URL: tinyurl.com/github-andr

# Подготовка компьютера к программированию на Python 3 в Minecraft

## Создание учетной записи на компьютере

Если у вас еще есть учетная запись с правами **администратора**, она на **английском языке** и не содержит **пробелов**, то можете переходить к Установке программного обеспечения.

*Инструкция для Windows 10*

1. Входим под учетной записью с правами администратора
2. Правой клавишей мыши нажимаем на **пуск** - **Управление компьютером**
3. Слева выбираем **Локальные пользователи** - **пользователи**
  * Справа в пустом месте правой клавишей мыши **Новый пользователь**
  * Имя пользователя на английском языке без пробелов, например **programmer**
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

1. Устанавливаем [Java 8](https://www.java.com/ru/download/manual.jsp)
2. Устанавливаем [Python 3.9.x](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe) + ставим галочку **add Path**!
3. Устанавливаем редактор кода [vscode](https://code.visualstudio.com/docs/setup/windows)
4. Скачиваем Minecraft сервер. [Ссылка на архив](https://tinyurl.com/mysrv)
  * Распаковываем архив в Документы
5. Устанавливаем ([TLauncher](https://tlauncher.org/))
6. Перезагружаем компьютер


## Запускаем сервер и пробуем первый код

  * Через TLauncher устанавливаем Minecraft версию OptFine 1.18.2


  * Запускаем сервер
  * Проверка версии (Запкскаем в терминале vscode)
    * `python`
    * Должны увидеть `Python 3.10.x ...`
  * Устанавливаем модуль `mcpi` через pip
    * `pip install mcpi`


7. или билдим сервер Minecraft
  * Изменяем server.properties (Error "Failed to verify username!") 
    * online-mode=true
  * Изменяем eula.txt
    * eula=true

8. Устанавливаем [git](https://git-scm.com/download/win)
9. Edge change language
  * Open Microsoft Edge.
  * Click the Settings and more (three-dotted) button.
  * Select the Settings option.
  * Click on Languages.
  * Click the Add languages button.
10. [Edge + google translate extension](https://microsoftedge.microsoft.com/addons/detail/google-translate-in-right/fcoongackakfdmiincikmjgkedcgjkdp)

* install server YouTube video [How to: Set up a 1.18.1+ Spigot/Bukkit Minecraft Server](https://www.youtube.com/watch?v=BqWWXHPO_2U&ab_channel=TroubleChute)
  * [installation](https://www.spigotmc.org/wiki/spigot-installation/)

## Create server build

```cmd
# build.bat
# Build Spigot server for Minecraft
# https://www.spigotmc.org/wiki/buildtools/#latest
@echo off
SET name=craftbukkit
SET ver=1.18
IF NOT EXIST BuildTools (
    mkdir BuildTools
)
cd BuildTools
curl -z BuildTools.jar -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
java -Xmx1000M -jar BuildTools.jar --rev %ver% --compile %name%
echo Build finished. Press any key for create start.bat for run Minecraft server.
pause
copy %name%-%ver%.jar ..
```

## Start server Minecraft

```cmd
# start.bat
@echo off
java -Xmx1512M -jar spigot.jar -nogui
pause
```
