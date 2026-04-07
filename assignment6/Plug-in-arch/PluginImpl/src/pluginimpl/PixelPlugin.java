package pluginimpl;

import plugininterface.DevicePlugin;

public class PixelPlugin implements DevicePlugin {

    @Override
    public void assess() {
        System.out.println("Assessing Pixel...");
    }

    @Override
    public String getDeviceName() {
        return "Pixel";
    }
}
