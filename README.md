Repository: minecraft-python  
short URL: tinyurl.com/github-andr

# Установка ПО

Устанавливаем необходиомое программное обеспечение

1. Устанавливаем [Java 17](https://www.java.com/en/download/manual.jsp)
2. Устанавливаем Minecraft с помощью ([TLauncher](https://tlauncher.org/))
    * run OptFine 1.12.2
3. Устанавливаем [Python 3.9.13](https://www.python.org/downloads/windows/) + ставим галочку **add Path**!
  * Устанавливаем модуль `mcpi` через pip
    * `pip install mcpi`
4. Устанавливаем редактор кода [vscode](https://code.visualstudio.com/docs/setup/windows)
5. Edge change language
  * Open Microsoft Edge.
  * Click the Settings and more (three-dotted) button.
  * Select the Settings option.
  * Click on Languages.
  * Click the Add languages button.
7. [Edge + google translate extension](https://microsoftedge.microsoft.com/addons/detail/google-translate-in-right/fcoongackakfdmiincikmjgkedcgjkdp)

* install server YouTube video [How to: Set up a 1.18.1+ Spigot/Bukkit Minecraft Server](https://www.youtube.com/watch?v=BqWWXHPO_2U&ab_channel=TroubleChute)
  * [installation](https://www.spigotmc.org/wiki/spigot-installation/)

## Create server build

```cmd
# build.bat
# Build Spigot server for Minecraft
# https://www.spigotmc.org/wiki/buildtools/#latest
@echo off
IF NOT EXIST BuildTools (
    mkdir BuildTools
)
cd BuildTools
curl -z BuildTools.jar -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
java -Xmx1000
M -jar BuildTools.jar --rev 1.18 --compile craftbukkit
pause
```

## Start server Minecraft

```cmd
# start.bat
@echo off
java -Xmx1512M -jar spigot.jar nogui
pause
```
