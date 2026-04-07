package coresystem;

import java.io.File;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.HashMap;
import java.util.Map;
import java.util.ServiceLoader;
import plugininterface.DevicePlugin;

public class CoreSystem {

    // Map of device name -> plugin instance, populated at runtime
    private static final Map<String, DevicePlugin> pluginRegistry =
        new HashMap<>();

    public static void main(String[] args) {
        // Load plugins from the plugins/ folder at startup
        loadPlugins();

        // Assess devices after plugins are loaded
        assessDevice("iPhone");
        assessDevice("Galaxy");
        assessDevice("Motorola");
        assessDevice("Pixel");
        assessDevice("Xiaomi");
        assessDevice("Unknown");
    }

    // public static void assessDevice(String deviceID) {
    //     try {
    //         String pluginClassName = pluginRegistry.get(deviceID);
    //         if (pluginClassName == null) {
    //             System.out.println("No plugin found for device: " + deviceID);
    //             return;
    //         }

    //         Class<?> pluginClass = Class.forName(pluginClassName);

    //         DevicePlugin plugin = (DevicePlugin) pluginClass
    //             .getDeclaredConstructor()
    //             .newInstance();

    //         plugin.assess();
    //     } catch (ClassNotFoundException e) {
    //         System.err.println(
    //             "Plugin class not found for device: " + deviceID
    //         );
    //         e.printStackTrace();
    //     } catch (Exception e) {
    //         e.printStackTrace();
    //     }
    // }

    public static void assessDevice(String deviceID) {
        // Look up the plugin in the registry
        DevicePlugin plugin = pluginRegistry.get(deviceID);

        if (plugin == null) {
            // No plugin found for this device
            System.out.println("No plugin found for device: " + deviceID);
            return;
        }

        // Run the assessment
        plugin.assess();
    }

    public static void loadPlugins() {
        // Locate the plugins directory relative to the working directory
        File pluginsDir = new File("plugins");

        // Check that the plugins directory exists
        if (!pluginsDir.exists() || !pluginsDir.isDirectory()) {
            System.err.println(
                "Plugins directory not found: " + pluginsDir.getAbsolutePath()
            );
            return;
        }

        // Get all .jar files in the plugins directory
        File[] jarFiles = pluginsDir.listFiles(file ->
            file.getName().endsWith(".jar")
        );

        if (jarFiles == null || jarFiles.length == 0) {
            System.out.println("No plugin JARs found in plugins directory.");
            return;
        }

        // Iterate through each JAR file and load plugins from it
        for (File jarFile : jarFiles) {
            try {
                // Convert the JAR file to a URL for the class loader
                URL jarUrl = jarFile.toURI().toURL();

                // Create a URLClassLoader that can read classes from this JAR.
                // The parent class loader is CoreSystem's loader, which has
                // access to the DevicePlugin interface.
                URLClassLoader classLoader = new URLClassLoader(
                    new URL[] { jarUrl },
                    CoreSystem.class.getClassLoader()
                );

                // Use ServiceLoader to find all DevicePlugin implementations in this JAR.
                // This looks for META-INF/services/plugininterface.DevicePlugin inside the JAR.
                ServiceLoader<DevicePlugin> serviceLoader = ServiceLoader.load(
                    DevicePlugin.class,
                    classLoader
                );

                // Register each discovered plugin by its device name
                for (DevicePlugin plugin : serviceLoader) {
                    String deviceName = plugin.getDeviceName();
                    pluginRegistry.put(deviceName, plugin);
                    System.out.println(
                        "Loaded plugin: " +
                            deviceName +
                            " from " +
                            jarFile.getName()
                    );
                }
            } catch (Exception e) {
                System.err.println(
                    "Failed to load plugin from: " + jarFile.getName()
                );
                e.printStackTrace();
            }
        }

        System.out.println("Total plugins loaded: " + pluginRegistry.size());
        System.out.println("---");
    }
}
