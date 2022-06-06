# Исправление ошибок

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



## ModuleNotFoundError - No module named `mcpi`

  * Запускаем сервер
  * Проверка версии (Запкскаем в терминале vscode)
    * `python`
    * Должны увидеть `Python 3.9.x ...`
  * Устанавливаем модуль `mcpi` через pip
    * `pip install mcpi`
  * Если ошибка при установке - переустановите [Python](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe) - При установке поставьте галочку **add PATH!**
