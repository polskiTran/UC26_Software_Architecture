package pluginimpl;

import plugininterface.DevicePlugin;

public class GalaxyPlugin implements DevicePlugin {

    @Override
    public void assess() {
        System.out.println("Assessing Galaxy...");
    }

    @Override
    public String getDeviceName() {
        return "Galaxy";
    }
}
