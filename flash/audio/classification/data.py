# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Any, Callable, Dict, Optional, Tuple

import numpy as np

from flash.audio.classification.transforms import default_transforms, train_default_transforms
from flash.core.data.io.input import (
    InputDataKeys,
    InputFormat,
    has_file_allowed_extension,
    LoaderDataFrameInput,
    NumpyInput,
    PathsInput,
)
from flash.core.data.process import Deserializer, Preprocess
from flash.core.utilities.imports import _TORCHVISION_AVAILABLE
from flash.image.classification.data import ImageClassificationData
from flash.image.data import ImageDeserializer, IMG_EXTENSIONS, NP_EXTENSIONS

if _TORCHVISION_AVAILABLE:
    from torchvision.datasets.folder import default_loader


def spectrogram_loader(filepath: str):
    if has_file_allowed_extension(filepath, IMG_EXTENSIONS):
        img = default_loader(filepath)
        data = np.array(img)
    else:
        data = np.load(filepath)
    return data


class AudioClassificationNumpyInput(NumpyInput):
    def load_sample(self, sample: Dict[str, Any], dataset: Optional[Any] = None) -> Dict[str, Any]:
        sample[InputDataKeys.INPUT] = np.transpose(sample[InputDataKeys.INPUT], (1, 2, 0))
        return sample


class AudioClassificationTensorInput(AudioClassificationNumpyInput):
    def load_sample(self, sample: Dict[str, Any], dataset: Optional[Any] = None) -> Dict[str, Any]:
        sample[InputDataKeys.INPUT] = sample[InputDataKeys.INPUT].numpy()
        return super().load_sample(sample, dataset=dataset)


class AudioClassificationPathsInput(PathsInput):
    def __init__(self):
        super().__init__(loader=spectrogram_loader, extensions=IMG_EXTENSIONS + NP_EXTENSIONS)


class AudioClassificationDataFrameInput(LoaderDataFrameInput):
    def __init__(self):
        super().__init__(spectrogram_loader)


class AudioClassificationPreprocess(Preprocess):
    def __init__(
        self,
        train_transform: Optional[Dict[str, Callable]] = None,
        val_transform: Optional[Dict[str, Callable]] = None,
        test_transform: Optional[Dict[str, Callable]] = None,
        predict_transform: Optional[Dict[str, Callable]] = None,
        spectrogram_size: Tuple[int, int] = (128, 128),
        time_mask_param: Optional[int] = None,
        freq_mask_param: Optional[int] = None,
        deserializer: Optional["Deserializer"] = None,
    ):
        self.spectrogram_size = spectrogram_size
        self.time_mask_param = time_mask_param
        self.freq_mask_param = freq_mask_param

        super().__init__(
            train_transform=train_transform,
            val_transform=val_transform,
            test_transform=test_transform,
            predict_transform=predict_transform,
            data_sources={
                InputFormat.FILES: AudioClassificationPathsInput(),
                InputFormat.FOLDERS: AudioClassificationPathsInput(),
                "data_frame": AudioClassificationDataFrameInput(),
                InputFormat.CSV: AudioClassificationDataFrameInput(),
                InputFormat.NUMPY: AudioClassificationNumpyInput(),
                InputFormat.TENSORS: AudioClassificationTensorInput(),
            },
            deserializer=deserializer or ImageDeserializer(),
            default_data_source=InputFormat.FILES,
        )

    def get_state_dict(self) -> Dict[str, Any]:
        return {
            **self.transforms,
            "spectrogram_size": self.spectrogram_size,
            "time_mask_param": self.time_mask_param,
            "freq_mask_param": self.freq_mask_param,
        }

    @classmethod
    def load_state_dict(cls, state_dict: Dict[str, Any], strict: bool = False):
        return cls(**state_dict)

    def default_transforms(self) -> Optional[Dict[str, Callable]]:
        return default_transforms(self.spectrogram_size)

    def train_default_transforms(self) -> Optional[Dict[str, Callable]]:
        return train_default_transforms(self.spectrogram_size, self.time_mask_param, self.freq_mask_param)


class AudioClassificationData(ImageClassificationData):
    """Data module for audio classification."""

    preprocess_cls = AudioClassificationPreprocess
