package coresystemPack;

import java.io.File;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.HashMap;
import java.util.Map;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;

import plugininterfacePack.DevicePlugin;

public class CoreSystem {

    // Registry populated at runtime — no hardcoded plugin class names
    private static final Map<String, DevicePlugin> pluginRegistry = new HashMap<>();

    // Path to the plugins directory
    private static final String PLUGIN_DIR = "plugins";

    public static void main(String[] args) {
        // Step 1: Dynamically discover and load all plugins
        loadPlugins();

        // Step 2: Assess each device
        assessDevice("iPhone");
        assessDevice("Galaxy");
        assessDevice("Pixel");
        assessDevice("Oppo");
        assessDevice("Xiaomi");
        assessDevice("Unknown");
    }

    /**
     * Scans the plugins/ directory for JAR files.
     * For each JAR, uses URLClassLoader to load classes dynamically.
     * Iterates through JAR entries to find .class files that implement DevicePlugin.
     * Registers each discovered plugin using the class name (minus "Plugin" suffix)
     * as the device name key.
     */
    public static void loadPlugins() {
        File pluginFolder = new File(PLUGIN_DIR);

        if (!pluginFolder.exists() || !pluginFolder.isDirectory()) {
            System.err.println("Plugins directory not found: " + pluginFolder.getAbsolutePath());
            return;
        }

        // Get all .jar files in the plugins directory
        File[] jarFiles = pluginFolder.listFiles(
            (dir, name) -> name.endsWith(".jar")
        );

        if (jarFiles == null || jarFiles.length == 0) {
            System.out.println("No plugin JARs found.");
            return;
        }

        for (File jarFile : jarFiles) {
            try {
                // Create URLClassLoader to load classes from this JAR
                // Parent classloader gives access to the DevicePlugin interface
                URLClassLoader classLoader = new URLClassLoader(
                    new URL[]{jarFile.toURI().toURL()},
                    CoreSystem.class.getClassLoader()
                );

                // Open the JAR and iterate through its entries
                JarFile jar = new JarFile(jarFile);
                var entries = jar.entries();

                while (entries.hasMoreElements()) {
                    JarEntry entry = entries.nextElement();
                    String entryName = entry.getName();

                    // Step 3a: Check if this entry is a .class file
                    if (entryName.endsWith(".class")) {

                        // Convert file path to fully qualified class name
                        // e.g., "pluginImplPack/iPhonePlugin.class" → "pluginImplPack.iPhonePlugin"
                        String className = entryName
                            .replace("/", ".")
                            .replace(".class", "");

                        // Load the class using our URLClassLoader
                        Class<?> pluginClass = classLoader.loadClass(className);

                        // Step 3b: Check it's NOT an interface and implements DevicePlugin
                        if (!pluginClass.isInterface()
                            && DevicePlugin.class.isAssignableFrom(pluginClass)) {

                            // Instantiate the plugin
                            DevicePlugin plugin = (DevicePlugin)
                                pluginClass.getDeclaredConstructor().newInstance();

                            // Derive device name from class name by removing "Plugin" suffix
                            // e.g., "iPhonePlugin" → "iPhone"
                            String deviceName = pluginClass.getSimpleName()
                                .replace("Plugin", "");

                            pluginRegistry.put(deviceName, plugin);
                            System.out.println("Loaded plugin: " + deviceName
                                + " from " + jarFile.getName());
                        }
                    }
                }

                jar.close();

            } catch (Exception e) {
                System.err.println("Failed to load plugin from: " + jarFile.getName());
                e.printStackTrace();
            }
        }

        System.out.println("Total plugins loaded: " + pluginRegistry.size());
        System.out.println("---");
    }

    /**
     * Looks up the device in the plugin registry and calls assess().
     * Prints a fallback message if no matching plugin exists.
     */
    public static void assessDevice(String deviceID) {
        DevicePlugin plugin = pluginRegistry.get(deviceID);

        if (plugin == null) {
            System.out.println("No plugin found for device: " + deviceID);
            return;
        }

        plugin.assess();
    }
}