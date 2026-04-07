package pluginimpl;

import plugininterface.DevicePlugin;

public class XiaomiPlugin implements DevicePlugin {

    @Override
    public void assess() {
        System.out.println("Assessing Xiaomi...");
    }

    @Override
    public String getDeviceName() {
        return "Xiaomi";
    }
}
