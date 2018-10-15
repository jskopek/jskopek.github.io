---
layout: post
title:  "Encoding Video with .NET Core and Azure Media Services - Part 2"
description: "Azure Media Services offers a powerful set of video editing and delivery tools, but there is no official library for .NET Core. In this tutorial, I demonstrate how to build a basic REST client to upload and encode video with Azure"
date:   2018-04-24 12:00:00 +0000
canonical: "https://medium.com/jean-marcs-thoughts/encoding-video-with-net-core-and-azure-media-services-part-2-b19e6de42b60"
categories: programming
---

![1](/assets/encoding-video-with-net-core/1.png)

## Part 2: Uploading Videos to Azure Storage

Let’s continue from where we left off in [Part 1](/programming/2018/04/23/encoding-video-with-net-core-and-azure.html). We now have a MediaServices class that can communicate with Azure Media Services and establish an authentication token. Now let’s upload a video to Azure.

### How files are uploaded to Azure

Before we can upload a video file to Azure, we need to define an *Asset*, an *Access Policy*, and a file *Locator*.

[Assets](https://docs.microsoft.com/en-us/rest/api/media/operations/asset) are collections of video, audio, image, or text files with corresponding metadata. The files attached to an Asset instance can be encoded or streamed using AMS.

[Access Policies](https://docs.microsoft.com/en-us/rest/api/media/operations/accesspolicy) define the permissions and access timeframes for an Asset. An Access Policy with upload permissions must be defined before a file can be uploaded to an Asset.

[Locators](https://docs.microsoft.com/en-us/rest/api/media/operations/locator) provide an entry point to access files in an Asset. Locators can be configured with [Shared Access Signatures](https://docs.microsoft.com/en-us/rest/api/storageservices/Delegating-Access-with-a-Shared-Access-Signature?redirectedfrom=MSDN) for additional permissions, such as the ability to upload a file to the locator address. Locators require a corresponding Asset and Access Policy before they can be created.

### Generating an asset

Let’s start by creating the method to generate an asset:

<script src="https://gist.github.com/jskopek/99d2b564e74d7a429d4e0213c5a6d900.js"></script>

This method takes an asset name and a storage account name and creates an *Asset* instance in Azure Media Services. Note that the method returns an instance of an *Asset* class. This can be defined with the following code:

<script src="https://gist.github.com/jskopek/68891100d22348452b466ff707713446.js"></script>

### Generating an Access Policy

Next, let’s create a method that generates an *Access Policy* in AMS. Insert the following method in your *MediaServices* class:

<script src="https://gist.github.com/jskopek/db2aeac10475f9e4aeb394fcfc193f4d.js"></script>

### Generating a Locator

Finally, let’s create a *Locator* instance that will be used when uploading the file. Insert the following code in your *MediaServices* class:

<script src="https://gist.github.com/jskopek/0ec39f7463ecc2ff94dc0858003e29c3.js"></script>

This method returns an instance of a *Locator* class, which can be defined with the following code:

<script src="https://gist.github.com/jskopek/6adf87d713e617ffd1fc7613c56ce5ce.js"></script>

Finally, let’s tie it all together by calling these methods from the main *Program.cs* file:

<script src="https://gist.github.com/jskopek/ca14982b8ff70e28193a1468db08941f.js"></script>

### Uploading a video to Azure Media Services

Now that we have a locator instance for an asset with an upload-enabled access policy, we can upload a file to Azure. Let’s start by creating a method that takes a file stream, an *Asset* instance, and a *Locator* instance:

<script src="https://gist.github.com/jskopek/4df895c07f8f262c773c9935a2c29f48.js"></script>

Once the file has been uploaded to the locator, we must generate a file info request before the file is registered to the asset. The following code generates a file info request:

<script src="https://gist.github.com/jskopek/d314e1af1f1a5006e9369654a0779c3b.js"></script>

Finally, let’s tie it all together in the *Program.cs* file. This code demonstrates an example upload:

<script src="https://gist.github.com/jskopek/1298d3d86a7947407bb1761dd63be037.js"></script>

Your should now have a video file uploaded and registered to an asset.

Your code [should now look like this](https://github.com/jskopek/AzureMediaServicesEncoderNetCore/tree/467fed0a3f35d7b159acd51f4994ad79e0dbba1e).

![4](/assets/encoding-video-with-net-core/4.png)

If you are having trouble determining the state of your Azure Media Services account, you may wish to install the [Azure Media Services Explorer](https://github.com/Azure/Azure-Media-Services-Explorer). This tool provides a nice GUI for navigating your Azure Media Services instance.

In the next step, we will [encode our newly uploaded video file](/programming/2018/05/08/encoding-video-with-net-core-and-azure-media-services-part-3.html).
