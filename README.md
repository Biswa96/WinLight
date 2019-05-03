# WinLight

Download Windows 10 Spotlight Lock screen images anywhere

# How to use

Clone this git repository with `git clone https://github.com/Biswa96/WinLight`.
If you want to download the images in a different folder copy the script in it.
Run any one of the scripts as following:

* Python script: Install requests module with `python -m pip install requests`.
Run the script with double click or use `python WinLight.py`.

* Shell script: Install `wget` in your system. Fox example, in Debian and
its family run `apt install wget`. Make the shell script
executable with `chmod +x WinLight.sh`. Then run the script with
double click or use `./WinLight.sh` command in your preferred shell.

There will be some JPEG images after success. Images will be in pair of landscape
and portrait mode. Run the script multiple times to gather more images.

# How this works

Both script work as following:

* Download the `cache.json` file with some magic.
* Edit it for further use.
* Download the images.
* Delete small blank files (less than 2 KB).

To see `cache.json` file, open it in Firefox which highlights it syntactically.
For Chromium and its derivatives, use any JSON viewer or formatter extensions.

# Insight

Interested in what happens behind the scene? See [Developers](Developers.md) page.

# Caveats

The python script fails in Python3 in Windows due to Unicode encoding in JSON file.
Linux Distributions do not have this issue. Use Python2 in Windows.
Any suggestions are welcome.

# License

WinLight is licensed under the GNU General Public License v3. A full
copy of the license is provided in [LICENSE](LICENSE).

    WinLight -- Download Windows 10 Spotlight Lock screen images anywhere
    Copyright (C) 2019 Biswapriyo Nath

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
