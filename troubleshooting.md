# 

## ИСПРАВЛЯЕМ ОШИБКУ - MINECRAFT GLFW ERROR 65542 WGL: THE DRIVER DOES NOT APPEAR TO SUPPORT OPENGL TLAUNCHER

1. Закройте TLauncher.
2. Скачиваем [OpenGL driver](http://www.mediafire.com/file/dy6c3nromnwpmpa/Minecraft_OpenGL.zip/file)
3. Нажмите кнопку "Загрузить".
4. Откройте расположение загруженного файла.
5. Извлеките загруженный файл.
6. Откройте извлеченную папку.
7. Если ваша ОС 32-битная, откройте 32-битную папку ИЛИ Если ваша ОС 64-битная, откройте 64-битную папку
8. Скопируйте opengl32.dll
9. В папку на C: Диске: `c:\Program Files\Java\jre...\bin\`
10. Вставьте файл
11. Запустите TLauncher и из него Minecraft





  * Запускаем сервер
  * Проверка версии (Запкскаем в терминале vscode)
    * `python`
    * Должны увидеть `Python 3.9.x ...`
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
