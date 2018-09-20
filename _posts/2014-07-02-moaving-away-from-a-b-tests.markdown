---
layout: post
title:  "Moving away from A/B Tests"
description: "“Intuition guides, data decides” - at times. But it’s easy to go overboard with A/B testing and underestimate the cost"
date:   2014-07-02 12:00:00 +0000
canonical: "https://medium.com/@jmskopek/moving-away-from-a-b-tests-4fb66d8ee9e2"
categories: programming
---

# Moving away from A/B Tests

I’ve long been an advocate of using A/B tests to build things. That’s slowly starting to change.

Ever since Markus Frind introduced the concept of “intuition guides, data decides” to me nearly two years ago, I’ve been A/B testing my way through life. Recently, however, I’ve found myself subconsciously moving away from the darling in my development toolkit. What could be happening? After some introspection, I think I’ve figured it out:

**A/B tests are really, really hard to do right**

The simplicity of setting up an A/B test is one of the approach’s biggest problems. Because pretty much *any* variation can be considered an A/B test, it’s very easy to build a bad or overly broad hypothesis. It’s also incredibly hard to collect the proper analysis data for an A/B test, and very easy to misinterpret that data during analysis.

I’ve found that the majority of my A/B tests have had a certain amount of bias towards one variant. Perhaps I’m comparing an exciting new design against an existing version, or testing my approach over a team-mate’s. As much as I would like to claim I have total impartiality, I can think of many situations when I’ve been secretly rooting for one variant.

So I’m a little biased — is that a big deal? The data should be the ultimate judge over which variant makes it. Unfortunately, data analysis is an art as much as a science. When the seed of an outcome is planted in someone’s head, it’s usually pretty easy to find the right data to back up your claim.

I was recently doing an analysis on a new dashboard I had been testing out. I was worried the new version wouldn’t drive traffic to the right destination, and the numbers were backing up my concern. It wasn’t until a little while later that I realized that I was looking at traffic across all devices; traffic from mobile devices, which the page had not been optimized for, was driving the overall conversion down. I found myself going through a total reversal of my original conclusion; not only was the feature working, but we were desperately in need of mobile optimizations!

So, if A/B testing is error prone, what can we do about it?

For starters, practice makes perfect. Like all skills, understanding how to build a solid A/B test takes time and effort. Over time, common traps emerge and can be squashed.

Like all powerful tools, A/B tests need to be given respect. Tests can be great at making your product better, but they have a specific place in development. Tests work well when you’re fine tuning a small detail; if you test a massive variation, you will find your test is worthless. Tests can’t be rushed; you must give yourself enough time to develop a hypothesis, make sure the correct data is being collected, and think about pitfalls while you’re analyzing the results.

Two years after falling in love with A/B tests, I’ve started delegating them to a smaller role. They’ll still take an important place in my development toolkit, but I’m not relying on them nearly as much for major features and design decisions.
