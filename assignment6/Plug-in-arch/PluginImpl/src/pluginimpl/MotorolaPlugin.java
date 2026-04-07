package pluginimpl;

import plugininterface.DevicePlugin;

public class MotorolaPlugin implements DevicePlugin {

    @Override
    public void assess() {
        System.out.println("Assessing Motorola...");
    }

    @Override
    public String getDeviceName() {
        return "Motorola";
    }
}
