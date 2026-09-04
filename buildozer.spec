[app]

# (str) Title of your application
title = Stock Signal Pro

# (str) Package name
package.name = stocksignalpro

# (str) Package domain
package.domain = org.stocksignal

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf,json,csv

# (list) Requirements (ভারী pandas/numpy বাদ দিয়ে হালকা লাইব্রেরি রাখা হয়েছে)
requirements = python3==3.10.12,kivy==2.3.0,requests


# (str) Android API level (SDK)
android.api = 33

# (str) Minimum API level
android.minapi = 21

# (int) Android NDK version
android.ndk = 25b

# (list) Permissions
android.permissions = INTERNET

# (bool) If True, fullscreen mode
fullscreen = 1

# (str) Supported orientation
orientation = portrait

# (list) Architectures to build for
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True
