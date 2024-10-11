# Presetting
1. Install JDK (version over 1.5)
2. Install Node.js
3. Install Android SDK
4. Install Python 3.10 (Install library Appium-Python-Client and Selenium)
5. Install Appium Server and Appium Inspector
6. Install Charles and Postman 





# Introduction

1. I tried to use ADB to collect related configurations from devices and app, then locating elements by Appium Inspector. Finally, use Behave combine with Appium for achieving Android UI automation on MyObservatory
2. About API testing, I used Charles to catch web packages at first but it hit SSL Pinning, so I tried to execute in VirtualXposed and JustTrustMe module to skip SSL issues. After collecting related api requests and call successfully on Postman, used Behave combine with Requests to complete API automation test.

