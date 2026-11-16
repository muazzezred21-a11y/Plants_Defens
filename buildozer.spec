[app]
title = Bitki Savunması
package.name = bitkisavunmasi
package.domain = org.bitkisavunmasi
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,wav,ogg,mp3
version = 1.0
requirements = python3,kivy,pyjnius
orientation = landscape
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.archs = arm64-v8a
android.api = 35
android.minapi = 23
