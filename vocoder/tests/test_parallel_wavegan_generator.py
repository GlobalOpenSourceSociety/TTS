import numpy as np
import torch

from TTS.vocoder.models.parallel_wavegan_generator import ParallelWaveganGenerator


def test_pwgan_generator():
    model = ParallelWaveganGenerator(
        in_channels=1,
        out_channels=1,
        kernel_size=3,
        num_res_blocks=30,
        stacks=3,
        res_channels=64,
        gate_channels=128,
        skip_channels=64,
        aux_channels=80,
        aux_context_window=2,
        dropout=0.0,
        bias=True,
        use_weight_norm=True,
        use_causal_conv=False,
        upsample_conditional_features=True,
        upsample_factors=[4, 4, 4, 4])
    dummy_c = torch.rand((4, 80, 64))
    output = model(dummy_c)
    assert np.all(output.shape == (4, 1, 64 * 256))
    model.remove_weight_norm()
    output = model.inference(dummy_c)
    assert np.all(output.shape == (4, 1, (64 + 4) * 256))