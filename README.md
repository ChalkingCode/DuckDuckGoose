# DuckDuckGoose
A super simple asset detection tool written in python using crt.sh and duckdb

## Features
- Search crt.sh endpoint.
- Output unique results for any given domain to a JSON file.
- Fetch certificate information by domain.

## Table of contents
* [Features](#features)
* [Setup](#setup)
* [HowTo](#howto)

## Features
- Search crt.sh endpoint.
- Output unique results for any given domain to a JSON file.
- Fetch certificate information by domain.

## Setup

### Prerequisites

#### Enviroment
1.) ensure you have python 3.x installed 

#### Clone repository 

        $ git clone https://github.com/ChalkingCode/DuckDuckGoose.git
        $ cd DuckDuckGoose


#### Install Packages on env
        
        duckdb
	requests
        tld

	# This only needs to be ran once per env 
	$ pip install -r requirements.txt

## HowTo

How to run the script that will search and grab your data  

```	
$ python duckduckgoose.py
----------------------------------------------
|                                             |
|                                             |
|                                             |
|              DUCK, DUCK, GOOSE!             |
|                                             |
|        Simple asset discovery tool using    |
|               crt.sh and duckdb             |
|                  created by                 |
|                 CHALKINGCODE                |
|                                             |
|                                             |
----------------------------------------------
What is your domain, please enter value: owasp.org

Thanks for using duckduckgoose we are now looking for your ducks

Name of all the fields that data is returned for


──────────────┬──────────────────────┬──────────────────────┬─────────────────────────────────┬─────────────┬─────────────────────────┬─────────────────────┬─────────────────────┬──────────────────────────────────────────┬──────────────┐
│ issuer_ca_id │     issuer_name      │     common_name      │           name_value            │     id      │     entry_timestamp     │     not_before      │      not_after      │              serial_number               │ result_count │
│    int64     │       varchar        │       varchar        │             varchar             │    int64    │         varchar         │       varchar       │       varchar       │                 varchar                  │    int64     │



What fields are you looking to select in paticular type * to see  all or  example common_name, if multiple comma seperate, if you would like to see all fields type *. *
┌──────────────┬──────────────────────┬──────────────────────┬─────────────────────────────────┬─────────────┬─────────────────────────┬─────────────────────┬─────────────────────┬──────────────────────────────────────────┬──────────────┐
│ issuer_ca_id │     issuer_name      │     common_name      │           name_value            │     id      │     entry_timestamp     │     not_before      │      not_after      │              serial_number               │ result_count │
│    int64     │       varchar        │       varchar        │             varchar             │    int64    │         varchar         │       varchar       │       varchar       │                 varchar                  │    int64     │
├──────────────┼──────────────────────┼──────────────────────┼─────────────────────────────────┼─────────────┼─────────────────────────┼─────────────────────┼─────────────────────┼──────────────────────────────────────────┼──────────────┤
│       247115 │ C=US, O=Amazon, CN…  │ secureflag.com       │ *.secureflag.owasp.org\nsecur…  │ 13578115545 │ 2024-07-01T00:07:46.162 │ 2024-07-01T00:00:00 │ 2025-07-31T23:59:59 │ 0ab762ebc61a483b107a10cf0c8b1575         │            2 │
│       295814 │ C=US, O=Let's Encr…  │ ocms.owasp.org       │ ocms.owasp.org                  │ 13531485464 │ 2024-06-27T02:14:23.1   │ 2024-06-27T01:14:22 │ 2024-09-25T01:14:21 │ 03de5d2783665c4e0584b2411f14fcfca48a     │            2 │
│       295814 │ C=US, O=Let's Encr…  │ ocms.owasp.org       │ ocms.owasp.org                  │ 13531474221 │ 2024-06-27T02:14:22.899 │ 2024-06-27T01:14:22 │ 2024-09-25T01:14:21 │ 03de5d2783665c4e0584b2411f14fcfca48a     │            2 │
│       295815 │ C=US, O=Let's Encr…  │ name-virt-host.owa…  │ name-virt-host.owasp.org        │ 13395183755 │ 2024-06-15T02:19:30.188 │ 2024-06-15T01:19:29 │ 2024-09-13T01:19:28 │ 0388383cb50804f5d112f4ef8679de0b9956     │            2 │
│       295815 │ C=US, O=Let's Encr…  │ name-virt-host.owa…  │ name-virt-host.owasp.org        │ 13395187385 │ 2024-06-15T02:19:29.991 │ 2024-06-15T01:19:29 │ 2024-09-13T01:19:28 │ 0388383cb50804f5d112f4ef8679de0b9956     │            2 │
│       295814 │ C=US, O=Let's Encr…  │ contact.owasp.org    │ contact.owasp.org               │ 13395182008 │ 2024-06-15T02:19:04.406 │ 2024-06-15T01:19:04 │ 2024-09-13T01:19:03 │ 033cbe081d963b94158da342472955fae844     │            2 │
│       295814 │ C=US, O=Let's Encr…  │ contact.owasp.org    │ contact.owasp.org               │ 13395177698 │ 2024-06-15T02:19:04.299 │ 2024-06-15T01:19:04 │ 2024-09-13T01:19:03 │ 033cbe081d963b94158da342472955fae844     │            2 │
│       295815 │ C=US, O=Let's Encr…  │ austin.owasp.org     │ austin.owasp.org                │ 13395181209 │ 2024-06-15T02:18:49.818 │ 2024-06-15T01:18:49 │ 2024-09-13T01:18:48 │ 035d09b9a9a49e1eb0e8b20ceeabd0c99b7f     │            2 │
│       295815 │ C=US, O=Let's Encr…  │ austin.owasp.org     │ austin.owasp.org                │ 13395181311 │ 2024-06-15T02:18:49.621 │ 2024-06-15T01:18:49 │ 2024-09-13T01:18:48 │ 035d09b9a9a49e1eb0e8b20ceeabd0c99b7f     │            2 │
│       295810 │ C=US, O=Let's Encr…  │ docs.owasp.org       │ docs.owasp.org                  │ 13381473004 │ 2024-06-13T20:14:04.81  │ 2024-06-13T19:14:04 │ 2024-09-11T19:14:03 │ 0420a56060f2d747bb7faa70e55b15fb684e     │            2 │
│           ·  │          ·           │       ·              │       ·                         │        ·    │           ·             │          ·          │          ·          │                  ·                       │            · │
│           ·  │          ·           │       ·              │       ·                         │        ·    │           ·             │          ·          │          ·          │                  ·                       │            · │
│           ·  │          ·           │       ·              │       ·                         │        ·    │           ·             │          ·          │          ·          │                  ·                       │            · │
│         7395 │ C=US, O=Let's Encr…  │ cheesemonkey.owasp…  │ cheesemonkey.owasp.org          │    11616740 │ 2015-12-23T01:07:45.999 │ 2015-12-23T00:08:00 │ 2016-03-22T00:08:00 │ 01252ed37a43ed0a59f44223fa325d22ac3f     │            2 │
│         1539 │ C=NL, L=Amsterdam,…  │ *.owasp.org          │ *.owasp.org                     │     6020816 │ 2014-12-24T12:27:12.26  │ 2014-12-22T17:55:40 │ 2015-12-22T17:55:38 │ 46dc2357f7d5a2eb59ed657cc145c11e00a64fec │            2 │
│         1539 │ C=NL, L=Amsterdam,…  │ *.owasp.org          │ *.owasp.org                     │     5974387 │ 2014-12-19T13:22:24.739 │ 2014-12-17T15:42:31 │ 2015-12-17T15:42:20 │ 35a4ca7a69fd4fb50b518a2855c885570ab7854f │            2 │
│           97 │ C=IL, O=StartCom L…  │ registration.owasp…  │ adrian.hayes@owasp.org\nowasp…  │     5766198 │ 2014-12-01T23:54:35.833 │ 2014-11-18T17:22:56 │ 2015-11-18T22:12:52 │ 146b28                                   │            4 │
│          275 │ O=Cybertrust Inc, …  │ *.owasp.org          │ *.owasp.org                     │     4993569 │ 2014-09-15T18:28:55.763 │ 2014-04-17T11:32:30 │ 2015-04-17T11:32:30 │ 020000000001456f75967ac5b343             │            1 │
│          904 │ C=US, ST=Arizona, …  │ lists.owasp.org      │ lists.owasp.org\nwww.lists.ow…  │     3903707 │ 2014-04-22T13:22:52.127 │ 2014-04-20T08:20:01 │ 2016-04-20T08:20:01 │ 27997523a3227b                           │            3 │
│          904 │ C=US, ST=Arizona, …  │ www.owasp.org        │ owasp.org\nwww.owasp.org        │     3899908 │ 2014-04-22T11:31:12.139 │ 2014-04-20T07:08:02 │ 2016-04-20T07:08:02 │ 2b211923cee8c5                           │            3 │
│          904 │ C=US, ST=Arizona, …  │ ocms.owasp.org       │ ocms.owasp.org\nwww.ocms.owas…  │     3899663 │ 2014-04-22T11:21:42.606 │ 2014-04-20T03:55:02 │ 2016-04-20T03:55:02 │ 2b24f575567b5c                           │            3 │
│           97 │ C=IL, O=StartCom L…  │ registration.owasp…  │ nick.freeman@owasp.org\nowasp…  │     2583660 │ 2013-08-30T22:06:21.29  │ 2013-08-08T01:12:08 │ 2014-08-08T11:26:55 │ 0b6f11                                   │            4 │
│           24 │ C=US, ST=Arizona, …  │ *.owasp.org          │ *.owasp.org\nowasp.org          │      248566 │ 2013-03-26T10:15:07.178 │ 2012-12-17T14:37:22 │ 2014-12-17T18:36:30 │ 2b2665601b9a78                           │            4 │
├──────────────┴──────────────────────┴──────────────────────┴─────────────────────────────────┴─────────────┴─────────────────────────┴─────────────────────┴─────────────────────┴──────────────────────────────────────────┴──────────────┤
│ 811 rows (20 shown)                                                                                                                                                                                                             10 columns │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘


Would you like to select other fields type (yes or no)? yes

are you sure you want to continue to select more fields (yes or no)? yes
Name of all the fields that data is returned for


──────────────┬──────────────────────┬──────────────────────┬─────────────────────────────────┬─────────────┬─────────────────────────┬─────────────────────┬─────────────────────┬──────────────────────────────────────────┬──────────────┐
│ issuer_ca_id │     issuer_name      │     common_name      │           name_value            │     id      │     entry_timestamp     │     not_before      │      not_after      │              serial_number               │ result_count │
│    int64     │       varchar        │       varchar        │             varchar             │    int64    │         varchar         │       varchar       │       varchar       │                 varchar                  │    int64     │



What fields are you looking to select in paticular type * to see  all or  example common_name, if multiple comma seperate, if you would like to see all fields type *. common_name,not_before,not_after
┌───────────────────────────┬─────────────────────┬─────────────────────┐
│        common_name        │     not_before      │      not_after      │
│          varchar          │       varchar       │       varchar       │
├───────────────────────────┼─────────────────────┼─────────────────────┤
│ secureflag.com            │ 2024-07-01T00:00:00 │ 2025-07-31T23:59:59 │
│ ocms.owasp.org            │ 2024-06-27T01:14:22 │ 2024-09-25T01:14:21 │
│ ocms.owasp.org            │ 2024-06-27T01:14:22 │ 2024-09-25T01:14:21 │
│ name-virt-host.owasp.org  │ 2024-06-15T01:19:29 │ 2024-09-13T01:19:28 │
│ name-virt-host.owasp.org  │ 2024-06-15T01:19:29 │ 2024-09-13T01:19:28 │
│ contact.owasp.org         │ 2024-06-15T01:19:04 │ 2024-09-13T01:19:03 │
│ contact.owasp.org         │ 2024-06-15T01:19:04 │ 2024-09-13T01:19:03 │
│ austin.owasp.org          │ 2024-06-15T01:18:49 │ 2024-09-13T01:18:48 │
│ austin.owasp.org          │ 2024-06-15T01:18:49 │ 2024-09-13T01:18:48 │
│ docs.owasp.org            │ 2024-06-13T19:14:04 │ 2024-09-11T19:14:03 │
│       ·                   │          ·          │          ·          │
│       ·                   │          ·          │          ·          │
│       ·                   │          ·          │          ·          │
│ cheesemonkey.owasp.org    │ 2015-12-23T00:08:00 │ 2016-03-22T00:08:00 │
│ *.owasp.org               │ 2014-12-22T17:55:40 │ 2015-12-22T17:55:38 │
│ *.owasp.org               │ 2014-12-17T15:42:31 │ 2015-12-17T15:42:20 │
│ registration.owasp.org.nz │ 2014-11-18T17:22:56 │ 2015-11-18T22:12:52 │
│ *.owasp.org               │ 2014-04-17T11:32:30 │ 2015-04-17T11:32:30 │
│ lists.owasp.org           │ 2014-04-20T08:20:01 │ 2016-04-20T08:20:01 │
│ www.owasp.org             │ 2014-04-20T07:08:02 │ 2016-04-20T07:08:02 │
│ ocms.owasp.org            │ 2014-04-20T03:55:02 │ 2016-04-20T03:55:02 │
│ registration.owasp.org.nz │ 2013-08-08T01:12:08 │ 2014-08-08T11:26:55 │
│ *.owasp.org               │ 2012-12-17T14:37:22 │ 2014-12-17T18:36:30 │
├───────────────────────────┴─────────────────────┴─────────────────────┤
│ 811 rows (20 shown)                                         3 columns │
└───────────────────────────────────────────────────────────────────────┘


are you sure you want to continue to select more fields (yes or no)? no
``` 
