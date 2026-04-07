package pluginimpl;

import plugininterface.DevicePlugin;

public class iPhonePlugin implements DevicePlugin {

    @Override
    public void assess() {
        System.out.println("Assessing iPhone...");
    }

    @Override
    public String getDeviceName() {
        return "iPhone";
    }
}
