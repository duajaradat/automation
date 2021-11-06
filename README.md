#  Automation

## Author : 

Du'a Jaradat

---

## Links and Resources

- [Automation Code](https://github.com/duajaradat/automation/blob/automation/automation/filter.py)
- [Pull Request](https://github.com/duajaradat/automation/pull/1)

---


## Overview

A colleague has abruptly left the team to pursue a career as a novelist.

This colleague’s last days (and weeks) on the job were a mixed bag in terms of productivity.

Looking through the documents left behind there is some important contact info in the form of email addresses and phone numbers.

Unfortunately it’s mixed in with a bunch of useless notes.

Find the needles in the haystack.

---
## Feature Tasks and Requirements

- Given a document potential-contacts, find and collect all email addresses and phone numbers.

- Phone numbers may be in various formats.
     - (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.

     - phone numbers with missing area code should presume 206

     - phone numbers should be stored in xxx-yyy-zzzz format.

- Once emails and phone numbers are found they should be stored in two separate documents.

- The information should be sorted in ascending order.

- Duplicate entries are not allowed.

---
     

## User Acceptance Tests

The ‘phone_numbers.txt’ and ‘emails.txt’ files will be verified by an automated system. So make sure to match the naming/formatting requirements exactly.

---

## Tools and Dependencies

- Poetry
- shutil
- black
- pytest

---

## Getting Started

- Clone down this repo
- cd automation
- `poetry install`
- `poetry shell`