## Build
First install Flathub user-wide:
```
flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

Then build and install the application:
```
flatpak-builder --force-clean --user --install-deps-from=flathub --repo=repo --install builddir rocks.snap4arduino.Snap4Arduino.yml
```

## Create .flatpak bundle

```
flatpak build-bundle repo snap4arduino.flatpak org.snap4arduino.Snap4Arduino --runtime-repo=https://flathub.org/repo/flathub.flatpakrepo
```
