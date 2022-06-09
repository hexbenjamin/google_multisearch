# multi_search.py
multi_search is a **command line tool** for assembling search engine links, specifically with the intention of searching multiple specific domains at once.

***

**This is my first semi-serious development project, and even then it was mostly intended for practice.** If you have advice or ideas to contribute after peeking at the code, please feel free to create a pull request &/or reach out. I think, at minimum, this could become somewhat useful to some folks. Contact information is at the end of this file

> Development is only the most recent addition to a long list of hobbies for me, one of which is 3D printing. Some services ([yeggi](https://www.yeggi.com/) comes to mind) already exist to index results across multiple community repositories of 3D models for printing, but I wanted a little more than that. The list of indexed services is fixed, and sometimes I'd like to crawl multiple sites for something that *isn't* a .stl file. Hence, multi_search!

### Feature overview
#### Current features:
* Constructs + opens a Google (only Google, for now) search link from a typed query and list of URLs.
* Accepts scope list via one-entry-per-line text file

##### Planned upgrades
* Improved scope loading (program-selectable preset scope lists)
* Executable files
* More search engines?
* GUI (depending on further research)

***

### Usage
This script requires **no additional packages**. An executable version is planned, but I frankly haven't learned how to do it just yet, so for now...

1. Make sure you have Python 3 installed, and download or clone this repository into a folder of your choosing.
2. Edit (or create) the *scope.txt* file in the "src" folder, alongside *multi_search.py*. Enter one target site per line, separated only with a line break.
3. Assuming Windows is your OS *(although this **should** work fine on other platforms)*, open a Command Prompt and navigate to the "src" folder from earlier.
4. Run the following command to invoke the multi_search program. The command line will prompt you further.  
`python multi_search.py`

> **Remember**  that you should *rarely* need a more specific URL than 'https://www.web.site/'. The search engine will look for results on all the subpages either way. The tool is currently only configured to parse ":" and "/" characters for the time being, so longer-form links with other special characters may cause errors.

***

## Contact
Benjamin Adase / "Hex Benjamin"  
email: <bnjmnadase@gmail.com>  
discord: [@hex benjamin#1738](https://discord.com/users/215846135649140747)  
website: soon

***

*README was last updated on 06/08/2022.*