package pluginImplPack;

import plugininterfacePack.DevicePlugin;

public class XiaomiPlugin implements DevicePlugin {
    @Override
    public void assess() {
        System.out.println("Assessing Xiaomi...");
    }
}