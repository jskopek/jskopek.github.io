---
layout: post
title:  "Fast insert or update statements with Django"
description: "I benchmark three ways of inserting or updating entries in a database with Django. If you know the behavior of your application you can see some nice performance gains"
date:   2016-05-04 12:00:00 +0000
canonical: "https://medium.com/@jmskopek/fast-insert-or-update-statements-with-django-a8b4ef1f6c06"
categories: programming
---

# Fast insert or update statements with Django

TLDR: use update_or_create / get_or_create when the likelihood of updating existing instances is high. Use create with an IntegrityError catch when the odds of inserting new instances is higher.

Anyone who has worked with Django for any period of time will inevitable run into the *update_or_create* / *get_or_create* methods. These are wonderful little methods that simplify the process of inserting or updating a model instance.

Let’s say your application tracked a runner’s best lap time with a RecordLap model…

<script src="https://gist.github.com/jskopek/2459aebf9d56b5d8d485783294991999.js"></script>

… and you wanted to either add an initial time or update their time with the newest record

<script src="https://gist.github.com/jskopek/0bc834389f57ad02fb3b9703020074d3.js"></script>

This is a clean, easy to read method. But is this the best approach? It turns out there’s another way of doing the same task:

<script src="https://gist.github.com/jskopek/d7eb47c5a25f1db4ba42ded12d836301.js"></script>

What’s going on here? We’re taking advantage of the *unique=True* property and the *IntegrityError* exception to catch scenarios where a runner already has a *RecordLap* instance. When this is the case, we get the runner’s *RecordLap* instance and update it with the new lap time.

For the sake of completion, let’s also take a look at a third option. Django provides us with a *get_or_create* method

<script src="https://gist.github.com/jskopek/5963fe15ba4abbcf1d0b6bc9a9fe1c4b.js"></script>

So, which is better? It turns out each has its strengths and weaknesses. I ran each variant through a series of benchmarks. In each case, I repeatedly ran each command over 500 data points. One benchmark tested a scenario where each call would insert a new instance, and a second benchmark tested a scenario where each call would update an existing instance. Tests were run with a PostgreSQL database backend.

It turns out the *update_or_create* / *get_or_create* approach is more useful when the likelihood of updating an existing instance is high. The *create* + *IntegrityError* combination seems to perform better when the odds of inserting new instances is higher.

**Benchmark: updating 500 existing instances**

* update_or_create: 11.4s average

* get_or_create: 11.3s average

* create: 12.1s average

**Benchmark: insert 500 new instances**

* update_or_create: 8.7s average

* get_or_create: 8.6s average

* create: 7.4s average

Of course, there’s a third option available to us. We can get clever by splitting up the update and insert commands into two sections and then grouping the inserts in one statement via the *bulk_insert* command. The bulk insert option is not always available, however.
