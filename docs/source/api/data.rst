###############
flash.core.data
###############

.. contents::
    :depth: 1
    :local:
    :backlinks: top

flash.core.data.auto_dataset
____________________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.auto_dataset.AutoDataset
    ~flash.core.data.auto_dataset.BaseAutoDataset
    ~flash.core.data.auto_dataset.IterableAutoDataset

flash.core.data.base_viz
________________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.base_viz.BaseVisualization

flash.core.data.batch
________________________

.. autosummary::
    :toctree: generated/
    :nosignatures:

    ~flash.core.data.batch.default_uncollate

flash.core.data.callback
________________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.callback.BaseDataFetcher
    ~flash.core.data.callback.ControlFlow
    ~flash.core.data.callback.FlashCallback

flash.core.data.data_module
___________________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.data_module.DataModule

flash.core.data.data_pipeline
_____________________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.data_pipeline.DataPipeline
    ~flash.core.data.data_pipeline.DataPipelineState

flash.core.data.io.input
___________________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.io.input.DatasetInput
    ~flash.core.data.io.input.Input
    ~flash.core.data.io.input.InputDataKeys
    ~flash.core.data.io.input.InputFormat
    ~flash.core.data.io.input.FiftyOneInput
    ~flash.core.data.io.input.ImageLabelsMap
    ~flash.core.data.io.input.LabelsState
    ~flash.core.data.io.input.MockDataset
    ~flash.core.data.io.input.NumpyInput
    ~flash.core.data.io.input.PathsInput
    ~flash.core.data.io.input.SequenceInput
    ~flash.core.data.io.input.TensorInput

.. autosummary::
    :toctree: generated/
    :nosignatures:

    ~flash.core.data.io.input.has_file_allowed_extension
    ~flash.core.data.io.input.has_len
    ~flash.core.data.io.input.make_dataset

flash.core.data.process
_______________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.process.BasePreprocess
    ~flash.core.data.process.DefaultPreprocess
    ~flash.core.data.process.DeserializerMapping
    ~flash.core.data.process.Deserializer
    ~flash.core.data.process.Postprocess
    ~flash.core.data.process.Preprocess
    ~flash.core.data.process.SerializerMapping
    ~flash.core.data.process.Serializer

flash.core.data.properties
__________________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.properties.ProcessState
    ~flash.core.data.properties.Properties

flash.core.data.splits
______________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.splits.SplitDataset

flash.core.data.transforms
__________________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.transforms.ApplyToKeys
    ~flash.core.data.transforms.KorniaParallelTransforms

.. autosummary::
    :toctree: generated/
    :nosignatures:

    ~flash.core.data.transforms.merge_transforms
    ~flash.core.data.transforms.kornia_collate

flash.core.data.utils
_____________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~flash.core.data.utils.CurrentFuncContext
    ~flash.core.data.utils.CurrentRunningStageContext
    ~flash.core.data.utils.CurrentRunningStageFuncContext
    ~flash.core.data.utils.FuncModule

.. autosummary::
    :toctree: generated/
    :nosignatures:

    ~flash.core.data.utils.convert_to_modules
    ~flash.core.data.utils.download_data
