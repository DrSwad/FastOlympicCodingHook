# FastOlympicCodingHook
Problem test-case parser for sublime text from various online judges. Depends on [Competitive Companion](https://github.com/jmerle/competitive-companion) and [FastOlympicCoding](https://github.com/Jatana/FastOlympicCoding).

<u><b>Setup</b></u>

- Make sure you have `python3`, [FastOlympicCoding](https://github.com/Jatana/FastOlympicCoding) and [Competitive Companion](https://github.com/jmerle/competitive-companion) installed.
- Add `12345` in the list of ports of competitive-companion browser extension.
- Clone the [repository](https://github.com/DrSchwad/FastOlympicCodingHook) inside your Sublime Text Packages folder and rename the cloned folder to `FastOlympicCodingHook`. You can do a quick google search to locate that folder for your particular OS or you can click the "Browse Packages" option in Sublime Text (if you find it) and the folder will open itself.
- Configure the relative directory and file suffix for test cases files in the FastOlympicCoding settings (`FastOlympicCoding.sublime-settings`). <b>After making changes to this file, remember to restart Sublime Text to ensure that this plugin fetches the latest configuration.</b>. You can also keep the default values (`"tests_relative_dir": ""`) while ensuring that `"tests_file_suffix"` is not empty to prevent overwriting your code file.

<u><b>Usage</b></u>

1. Navigate to the file that you'll solve the problem in. Then right click anywhere in the file. You should find an option named `Listen to Competitive Companion`. Click on it.
2. In the browser, navigate to the problem page and click on the competitive-companion extension's `green plus icon`.

The problem's test cases and correct answers will now be parsed and stored in `tests_relative_dir` within the parent directory of your code file, using the filename `tests_file_suffix` appended to your code file name. You might not immediately see the change in test cases inside sublime text. But if you run your code using FastOlympicCoding plugin (`ctrl+B`), then it'll you show those updated test cases and run your code against them.

To see a walkthrough of the setup process, you can watch this video:

[![Setup walkthrough](https://img.youtube.com/vi/68dm0bLwcsY/hqdefault.jpg)](https://youtu.be/68dm0bLwcsY)
