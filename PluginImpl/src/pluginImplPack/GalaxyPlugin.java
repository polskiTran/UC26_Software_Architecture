package pluginImplPack;

import plugininterfacePack.DevicePlugin;

public class GalaxyPlugin implements DevicePlugin {
    @Override
    public void assess() {
        System.out.println("Assessing Galaxy...");
    }
}