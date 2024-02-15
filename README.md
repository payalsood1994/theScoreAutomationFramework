# Project Structure
The project structure follows POM (Page Object) and is organized as follows:

- **Pages Directory:** Contains page objects corresponding to the application's UI pages.
   Pages Created (located at pages/android_pages)
   1. welcome_page
   2. signin_page
   3. home_page
   4. search_page
   5. player_page
- **Utils Directory:** Houses locators, test data, and common functions for the test automation framework.
   Utils Created (located at Utils)
   1. Locators (Contains both locators for android and IOS)
   2. config.py
   3. data (Contains the data for the test scripts)
   4. Util (Contains reusable functionality function to be used across the framework)
- **Tests Directory:** Includes test cases for various functionalities.
   Tests Created (located at tests/test_android)
   1. test_welcome_page
   2. test_signin_page
   3. test_player_search
   4. test_team_search
   
# Setup

Dependency Software List:
- Appium Server 2.0.0
- Java version "20.0.0"
- Android Studio (Optional)
- Node.js (18) and npm (9.6.7)
- Android SDK
- ADB (Android Debug Bridge)
- WebDriver Library (Appium-Python-Client)
**Download JDK**

Download From https://www.oracle.com/java/technologies/downloads/

Install the JDK on your machine

Also, set Environment Variables 

**Download ANDROID SDK**

Download sdk  From https://developer.android.com/studio

Set ANDROID_HOME as environment variable by adding mentioned path in .bashrc file

          - export ANDROID_HOME=/home/user/Android/Sdk
 
Also set path variables by following by adding :

         - export PATH=${PATH}:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

**Appium Installation:**

You can follow following link for installation https://medium.com/@syamsasi/setting-up-appium-on-windows-and-ubuntu-ea9a73ab989

Install Appium driver after install Appium server 2.0.0
```
    appium driver install uiautomator2
 ```
**Pycharm Installation:**

Download the Pycharm from their official website.

Install the Pycharm on your machine.

1. Clone this repository
    ```
    git clone https://github.com/payalsood1994/theScoreAutomationFramework
    ```

2. If you clone this repository before then run this on the project's root directory
    ```
    git pull
    ```
3. Copy your APK file, & paste it in project app folder.
    ```
    app/android/theScore.apk
    ```
4. Make sure you connect you android device/emulator. Devices UDID, APK, ApK path, appPackage & appActivity will detect automatically.
5. Go to the project's root directory and install requirements (Recommended create virtual env first).
    ```
    pip install -r requirements.txt
    ```
## Run Automated Tests
Go to the tests python scripts located at tests/test_android and run them by clicking on green icon next to the scripts.

