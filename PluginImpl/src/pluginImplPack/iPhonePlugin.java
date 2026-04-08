package pluginImplPack;

import plugininterfacePack.DevicePlugin;

public class iPhonePlugin implements DevicePlugin {
    @Override
    public void assess() {
        System.out.println("Assessing iPhone...");
    }
}