# Plug-in-arch

In this assignment, you will modify a core system from this [repo](https://github.com/lunarlunarll123/Plugin-arch) to dynamically load device assessment plugins from a plugins folder, removing the need for hardcoded class names or Java Build Path dependencies at runtime. Additionally, you will add three new plugins to extend the system beyond the existing iPhone and Galaxy plugins.

Plan:
- [x] Added 3 new devices in `PluginImpl/src/pluginimpl` for a total of 5 plugin devices
- [ ] 

running the `build_plugins` shell script
```bash
chmod +x build_plugins.sh
./build_plugins.sh
java -cp build/interface:build/core coresystem.CoreSystem
```
