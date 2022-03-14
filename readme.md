# Personal Blog
#### By Melody Chepkorir
## Table of Content
+ [Description](#description)
+ [Installation Requirement](#Installation)
+ [Behaviour Driven Development](#Behaviour-Driven-Development)
+ [Technology Used](#technology-used)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

****
## Description
Application that displays a random quote, it alos allow one to post a blog concerning something the user can delete a blog or a comment they find insulting. they can alson view thiei posts on profile page.

## Live link
https://my-personalblog.herokuapp.com/
## Installation
### Requirements
* python3.8
* pip 
### Installation process
* Open terminal
* run `git clone https://github.com/melodytowett/personal-blog.git`

### Dependancy Installation process
```
$ pip install -r requirements.txt

```

### Running the Application
To view the website run the command
```
$ chmod a+x start.sh
$ ./start.sh

```
To run the tests run the command
```
$ python3.8 manage.py test

```
## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Displays page | User logs in or signup| user can now add,view,comment on posts. can also view randm qute|
| Comment on post | user comments on any post| comments are appended |
|delete a post|User can delete on a post or comment they find no good| comment is deleted
|View profile| user can view profile and what they have posted|profile contain you profile pic and comments
| User logs out  | user can choose to logout once done | user loged out|


****


## Licence
MIT License

Copyright (c) 2022 Melody Towett

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


****


## Aythors Infor:
Email melodytowett.student@moringaschool.com