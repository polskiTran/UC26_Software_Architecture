package pluginImplPack;

import plugininterfacePack.DevicePlugin;

public class PixelPlugin implements DevicePlugin {
    @Override
    public void assess() {
        System.out.println("Assessing Pixel...");
    }
}