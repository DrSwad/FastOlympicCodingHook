# FastOlympicCodingHook
Problem test-case parser for sublime text from various online judges. Depends on [Competitive Companion](https://github.com/jmerle/competitive-companion) and [FastOlympicCoding](https://github.com/Jatana/FastOlympicCoding).

<u><b>Setup</b></u>

- Make sure you have `python3`, [FastOlympicCoding](https://github.com/Jatana/FastOlympicCoding) and [Competitive Companion](https://github.com/jmerle/competitive-companion) installed.
- Add `12345` in the list of ports of competitive-companion browser extension.
- Clone the [repository](https://github.com/DrSchwad/FastOlympicCodingHook) inside your Sublime Text Packages folder and rename the cloned folder to `FastOlympicCodingHook`. You can do a quick google search to locate that folder for your particular OS or you can click the "Browse Packages" option in Sublime Text (if you find it) and the folder will open itself.
- Additional step for Windows users: Add the following line in the FastOlympicCoding settings file: ```"tests_file_suffix": "__tests"```.

<u><b>Usage</b></u>

1. Navigate to the file that you'll solve the problem in. Then right click anywhere in the file. You should find an option named `Listen to Competitive Companion`. Click on it.
2. In the browser, navigate to the problem page and click on the competitive-companion extension's `green plus icon`.

The problem test cases and correct answers would be parsed now and stored in a file named `your filename__tests` for Windows and `your filename:tests` for others. You might not immediately see the change in test cases inside sublime text. But if you run your code using FastOlympicCoding plugin (`ctrl+B`), then it'll you show those updated test cases and run your code against them.

To see a walkthrough of the setup process, you can watch this video:

[![Setup walkthrough](https://img.youtube.com/vi/68dm0bLwcsY/hqdefault.jpg)](https://youtu.be/68dm0bLwcsY)
