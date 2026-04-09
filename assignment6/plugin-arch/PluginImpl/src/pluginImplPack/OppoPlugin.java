package pluginImplPack;

import plugininterfacePack.DevicePlugin;

public class OppoPlugin implements DevicePlugin {
    @Override
    public void assess() {
        System.out.println("Assessing Oppo...");
    }
}