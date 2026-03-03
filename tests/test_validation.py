import unittest
import torch
from kie_api.validation import _validate_image_tensor_batch

class TestValidateImageTensorBatch(unittest.TestCase):
    def test_valid_tensor(self):
        """Test with a valid tensor [B, H, W, 3]."""
        tensor = torch.randn(1, 64, 64, 3)
        result = _validate_image_tensor_batch(tensor)
        self.assertTrue(torch.equal(tensor, result))

    def test_none_input(self):
        """Test with None as input."""
        with self.assertRaisesRegex(RuntimeError, "images input is required."):
            _validate_image_tensor_batch(None)

    def test_non_tensor_input(self):
        """Test with an input that is not a torch.Tensor."""
        with self.assertRaisesRegex(RuntimeError, "images input must be a tensor batch."):
            _validate_image_tensor_batch([1, 2, 3])

    def test_wrong_dimensions(self):
        """Test with a tensor that has wrong dimensions."""
        tensor_3d = torch.randn(64, 64, 3)
        with self.assertRaisesRegex(RuntimeError, r"images input must have shape \[B, H, W, 3\]."):
            _validate_image_tensor_batch(tensor_3d)

        tensor_5d = torch.randn(1, 1, 64, 64, 3)
        with self.assertRaisesRegex(RuntimeError, r"images input must have shape \[B, H, W, 3\]."):
            _validate_image_tensor_batch(tensor_5d)

    def test_wrong_channel_size(self):
        """Test with a tensor that has wrong channel size."""
        tensor_1_channel = torch.randn(1, 64, 64, 1)
        with self.assertRaisesRegex(RuntimeError, r"images input must have shape \[B, H, W, 3\]."):
            _validate_image_tensor_batch(tensor_1_channel)

        tensor_4_channels = torch.randn(1, 64, 64, 4)
        with self.assertRaisesRegex(RuntimeError, r"images input must have shape \[B, H, W, 3\]."):
            _validate_image_tensor_batch(tensor_4_channels)

    def test_empty_batch(self):
        """Test with a tensor that has an empty batch size."""
        empty_tensor = torch.randn(0, 64, 64, 3)
        with self.assertRaisesRegex(RuntimeError, "images input batch is empty."):
            _validate_image_tensor_batch(empty_tensor)

if __name__ == '__main__':
    unittest.main()
