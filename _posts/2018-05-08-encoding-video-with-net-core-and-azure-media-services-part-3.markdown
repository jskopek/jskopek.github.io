---
layout: post
title:  "Encoding Video with .NET Core and Azure Media Services - Part 3"
description: "Azure Media Services offers a powerful set of video editing and delivery tools, but there is no official library for .NET Core. In this tutorial, I demonstrate how to build a basic REST client to upload and encode video with Azure"
date:   2018-05-08 12:00:00 +0000
canonical: "https://medium.com/jean-marcs-thoughts/encoding-video-with-net-core-and-azure-media-services-part-3-5429c9c14e5a"
ignore: true
categories: programming
---

![1](/assets/encoding-video-with-net-core/1.png)

## Part 3: Running an Azure Media Services Job

In [Part 2]({% post_url 2018-04-24-encoding-video-with-net-core-and-azure-media-services-part-2 %}), we were able to upload a video file to Azure Media Services. Now that an *Asset* has been created and a file has been uploaded to it, let’s run an encoding job on it.

Before we can create an encoding job, we must request an Azure Media Services media processor. AMS has many media processors, each of which can do different tasks. Some of these include:

* Video thumbnail generator

* Optical character recognition processor

* Face redactor/blurring

* Motion detection processor

* Face detector

* Hyperlapse time-lapse encoder

* Transcript/subtitles generator

The Azure Media Services media processors are described in more detail in an [article from Microsoft](https://docs.microsoft.com/en-us/azure/media-services/media-services-analytics-overview).

### Request a Media Processor

In the *MediaServices* class, create a method that retrieves the ID of a specified media processor:

<script src="https://gist.github.com/jskopek/8bca3fe9c17d5894b461b78f430c755a.js"></script>

### Create a Job

In the *MediaServices* class, create a method that generates an encoding job:

<script src="https://gist.github.com/jskopek/38548ef7f68a49964d5cb8146ac5861f.js"></script>

### Running a video encoder job on an asset

Now that we have the ability to request a media processor and generate a job, let’s run an encoding job on our uploaded video file from the main *Program.cs* file:

<script src="https://gist.github.com/jskopek/59a29a73f81c53bd625482648d643380.js"></script>

Congratulations! You should now have a video encoding job running on your newly uploaded asset.

Your code [should now look like this](https://github.com/jskopek/AzureMediaServicesEncoderNetCore/tree/4cdb370d1926f855479607a089e363f0cf02d6dc).

You now have everything you need to upload video files to Azure Media Services and run a number of different encoding jobs.
