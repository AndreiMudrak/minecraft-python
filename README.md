Repository: minecraft-python  
short URL: tinyurl.com/github-andr

# Установка ПО

Устанавливаем необходиомое программное обеспечение

1. Устанавливаем [Java 8](https://www.java.com/ru/download/manual.jsp)
2. Устанавливаем [Java 17](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) Windows x64 msi [Installer](https://download.oracle.com/java/17/archive/jdk-17.0.3.1_windows-x64_bin.msi)
3. Устанавливаем ([TLauncher](https://tlauncher.org/))
  * Через TLauncher устанавливаем Minecraft версию OptFine 1.18.2
4. Устанавливаем редактор кода [vscode](https://code.visualstudio.com/docs/setup/windows)
5. Устанавливаем [Python 3.10.x](https://www.python.org/downloads/windows/) + ставим галочку **add Path**!
  * Устанавливаем модуль `mcpi` через pip
  * `pip install mcpi`
6. Скачиваем 
  * [Ссылка на архив]()
  * Распаковываем архив в рабочую папку
  * Запускаем сервер
7. или билдим сервер Minecraft
  * Изменяем server.properties
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
