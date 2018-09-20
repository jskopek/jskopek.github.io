---
layout: post
title:  "Encoding Video with .NET Core and Azure Media Services"
description: "Azure Media Services offers a powerful set of video editing and delivery tools, but there is no official library for .NET Core. In this tutorial, I demonstrate how to build a basic REST client to upload and encode video with Azure"
date:   2018-04-23 12:00:00 +0000
canonical: "https://medium.com/jean-marcs-thoughts/encoding-video-with-net-core-and-azure-media-services-part-1-51bf6035ffcb"
categories: programming
---

![1](/assets/encoding-video-with-net-core/1.png)

# Part 1: Authenticating with Azure Media Services

Azure Media Services is a service that can encode video for mobile devices, generate thumbnails, and even create subtitles from audio tracks. It’s powerful and cheap, and I wanted to use it in an application.

Sadly, there is no official API for .NET Core.

In this tutorial, I will demonstrate how to create a bare-bones REST connector for Azure Media Services in C# and .NET Core 2.0. We will start by building a project that can talk to Azure Media Services.

# Creating the Project

Let’s start by creating our new project. For this demonstration, we will create a simple console application, but all of the principles should work just as well in a web application.

Open Visual Studio and create a new “Console App (.NET Core)” project:

![2](/assets/encoding-video-with-net-core/2.png)

You should now have a simple project that outputs “Hello World!” to a console.

Time to spice things up a notch.

# Setting up our Azure Media Services Account

Before you can even start to think about talking to Azure Media Services (or AMS, for short), you first need to create an Azure Media Services account via the Azure portal.

Once your Azure Media Services account is created, you will need to create a client id/secret pair and download the required connection information. This includes:

- Azure Active Directory tenant domain
- REST API Endpoint
- Client ID
- Client Secret

 The AAD tenant domain and REST API endpoint can be found by clicking on your Azure Media Service instance from the Azure portal, then clicking on “API Access” and then “Connect to Azure Media Services API with service principal”.

![3](/assets/encoding-video-with-net-core/2.png)

You will then see your tenant domain and REST API endpoint.

You may generate a Client ID and Secret from this part of the Azure Portal. The interface is clunky and hard to follow, but Microsoft has a decent guide for how to generate the client information.

Once you have the required information, add it to the main method of your console program. This is a bad approach in practice — it is important to never hard-code sensitive data into code or commit it into a repository — but we’re going for the simplest possible solution to start.

<script src="https://gist.github.com/jskopek/6d0cafae51cc304459c1171c1a69b4e4.js"></script>

Now that our credentials are accessible, let’s start building the REST service

# Building our Azure Media Services Client

Let’s create a new class to serve as our Media Encoder Service. Create a Services folder within the Solution Explorer, then create a MediaServices class within the newly created folder.

<script src="https://gist.github.com/jskopek/7aff615b356852d2c24e98d6306be7e2.js"></script>

Now let’s create a constructor that takes the configuration values and stores them internally

<script src="https://gist.github.com/jskopek/5a499019f05e5e7a6b8a0f1962d6d34e.js"></script>

We will need to create an HttpClient instance that will be used to communicate with the AMS REST API. Let’s initialize that client and set the proper request headers:

<script src="https://gist.github.com/jskopek/a707d237e0a39acaf311ad79dcdf836c.js"></script>
*Create a new HttpClient in the newly created MediaService class*

Pay close attention to the request headers! The AMS API is very sensitive to these values, and any omission or altered value will likely trigger one of many fairly obtuse error messages.

The next step is to request an access token from AMS. This will allow us to authorize our subsequent requests to AMS. In the MediaServices class, create a method named “InitializeAccessTokenAsync”. The following code will request a token from AMS:

<script src="https://gist.github.com/jskopek/19caa3983f0d79604bda2ffd586c0a84.js"></script>
*Request an Access Token from AMS*

Thanks to the [azure-media-services-core](https://github.com/shawnmclean/azure-media-services-core) SDK created by [Shawn Mclean](https://github.com/shawnmclean) for the code.

In the main *Program.cs* file, initialize a M*ediaServices *instance and request an access token:

<script src="https://gist.github.com/jskopek/2b08334c1d71f73e3a12f5e203a5fde5.js"></script>
*Initialize MediaService instance and request a token*

This will require converting the Main program into an asynchronous task. NET Core 2.0 supports asynchronous console-based commands, but the program’s .csproj file must explicitely specify a LangVersion of latest. Your .csproj file may look like this:

<script src="https://gist.github.com/jskopek/03212fbab0a3bdd85550b6c57a034c09.js"></script>

Run the project, and you should have an HttpClient that has been authorized with your access token.

Congratulations! You have created a MediaServices class and successfully authenticated with your Azure Media Services instance. At this point, your code [should look something like this project](https://github.com/jskopek/AzureMediaServicesEncoderNetCore/tree/2dca4cac6436d1a63c2ff297718e555f103a3cca).

In [Part 2](/programming/2018/04/24/encoding-video-with-net-core-and-azure-media-services-part-2.html), we will start uploading files to Azure and creating Media Services Assets.
