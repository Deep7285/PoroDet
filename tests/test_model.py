# This file contains unit tests for the UNet model defined in the package
import torch
from porodet.model import UNet

def test_unet_initialization():
    model = UNet(in_channels=1, out_channels=1)
    assert model is not None

# Test that the model can process a dummy tensor without errors
def test_unet_forward_pass():
    model = UNet(in_channels=1, out_channels=1)
    
    # Create a tiny 64x64 vertual test image (Batch Size 1, Channels 1, H 64, W 64)
    dummy_input = torch.randn(1, 1, 64, 64) 
    
    # Run it through the model
    output = model(dummy_input)
    
    # The output should have the exact same dimensions
    assert output.shape == (1, 1, 64, 64)