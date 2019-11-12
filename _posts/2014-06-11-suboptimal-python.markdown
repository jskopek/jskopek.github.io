---
layout: post
title:  "Suboptimal Python"
description: "Some brief thoughts on how to write effecient Python code. Don’t optimize too early and benchmark, benchmark, benchmark"
date:   2014-06-11 12:00:00 +0000
canonical: "https://medium.com/@jmskopek/suboptimal-python-d29858ddbe1f"
categories: programming
thumbnail: posts/suboptimal-python.png
thumbnail-background: "#277b45"
body_class: light
---

Why it doesn’t always make sense to think about performance

I recently watched [an interesting talk](https://www.youtube.com/watch?v=50OIO9ONmks) by [@regebro](http://twitter.com/regebro) on sub-optimal, prehistoric patterns. Through the 25 minute talk, Lennart walks through several programming patterns and examines their performance accross multiple python versions. There’s a lot of meat in these 25 minutes.

My takeaways:

1. Performance varies significantly from one version of python to another
2. Later versions of python do not always perform faster. Upgrading can sometimes cause performance regressions
3. Programming patterns change significantly over time
4. The less code you need to write, the faster it will usually perform
5. Some patterns aren’t universally better. What works best in one scenario may not be ideal in another scenario

I walked away with the conclusion that writing efficient code on the first take isn’t always possible. It’s helpful to keep performance in mind during development, but the outcome can vary siginifcantly from one scenario to another. The best approach for one problem may not work for another.

What this means is that benchmarking is more important than I expected. You can’t always tell which scenario is best, so it’s always a good idea to run real-world tests on your code.
