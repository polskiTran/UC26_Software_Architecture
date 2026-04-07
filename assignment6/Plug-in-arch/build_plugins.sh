#!/bin/bash
# Builds all 5 plugin JARs in one shot.

# Define plugins: "ClassName DeviceName"
PLUGINS=(
  "iPhonePlugin|iPhone"
  "GalaxyPlugin|Galaxy"
  "PixelPlugin|Pixel"
  "MotorolaPlugin|Motorola"
  "XiaomiPlugin|Xiaomi"
)

# Clean and create directories
rm -rf build plugins
mkdir -p build/interface plugins

# Compile PluginInterface
echo "Compiling PluginInterface..."
javac -d build/interface PluginInterface/src/plugininterface/DevicePlugin.java

# Compile CoreSystem
echo "Compiling CoreSystem..."
mkdir -p build/core
javac -cp build/interface -d build/core CoreSystem/src/coresystem/CoreSystem.java

# Generate, compile, and package each plugin
for entry in "${PLUGINS[@]}"; do
  IFS='|' read -r CLASS DEVICE <<< "$entry"
  echo "Building ${CLASS}.jar..."

  # Create temp directory for this plugin
  mkdir -p "build/${CLASS}/pluginimpl"
  mkdir -p "build/${CLASS}/META-INF/services"

  # Generate the Java source file
  cat > "build/${CLASS}/pluginimpl/${CLASS}.java" <<EOF
package pluginimpl;

import plugininterface.DevicePlugin;

public class ${CLASS} implements DevicePlugin {
    @Override
    public String getDeviceName() {
        return "${DEVICE}";
    }

    @Override
    public void assess() {
        System.out.println("Assessing ${DEVICE}...");
    }
}
EOF

  # Generate the ServiceLoader config file
  echo "pluginimpl.${CLASS}" > "build/${CLASS}/META-INF/services/plugininterface.DevicePlugin"

  # Compile
  javac -cp build/interface -d "build/${CLASS}" "build/${CLASS}/pluginimpl/${CLASS}.java"

  # Package into JAR
  jar cf "plugins/${CLASS}.jar" -C "build/${CLASS}" pluginimpl -C "build/${CLASS}" META-INF
done

echo ""
echo "Done! Built $(ls plugins/*.jar | wc -l) plugin JARs:"
ls -la plugins/
echo ""
echo "Run with: java -cp build/interface:build/core coresystem.CoreSystem"
