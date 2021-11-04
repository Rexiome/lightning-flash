##########
flash.text
##########

.. contents::
    :depth: 1
    :local:
    :backlinks: top

.. currentmodule:: flash.text

Classification
______________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~classification.model.TextClassifier
    ~classification.data.TextClassificationData

    classification.data.TextClassificationPostprocess
    classification.data.TextClassificationPreprocess
    classification.data.TextDeserializer
    classification.data.TextInput
    classification.data.TextCSVInput
    classification.data.TextJSONInput
    classification.data.TextDataFrameInput
    classification.data.TextParquetInput
    classification.data.TextHuggingFaceDatasetInput
    classification.data.TextListInput

Question Answering
__________________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~question_answering.model.QuestionAnsweringTask
    ~question_answering.data.QuestionAnsweringData

    question_answering.data.QuestionAnsweringBackboneState
    question_answering.data.QuestionAnsweringCSVInput
    question_answering.data.QuestionAnsweringInput
    question_answering.data.QuestionAnsweringDictionaryInput
    question_answering.data.QuestionAnsweringFileInput
    question_answering.data.QuestionAnsweringJSONInput
    question_answering.data.QuestionAnsweringPostprocess
    question_answering.data.QuestionAnsweringPreprocess
    question_answering.data.SQuADInput


Summarization
_____________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~seq2seq.summarization.model.SummarizationTask
    ~seq2seq.summarization.data.SummarizationData

    seq2seq.summarization.data.SummarizationPreprocess

Translation
___________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~seq2seq.translation.model.TranslationTask
    ~seq2seq.translation.data.TranslationData

    seq2seq.translation.data.TranslationPreprocess

General Seq2Seq
_______________

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: classtemplate.rst

    ~seq2seq.core.model.Seq2SeqTask
    ~seq2seq.core.data.Seq2SeqData
    ~seq2seq.core.finetuning.Seq2SeqFreezeEmbeddings

    seq2seq.core.data.Seq2SeqBackboneState
    seq2seq.core.data.Seq2SeqCSVInput
    seq2seq.core.data.Seq2SeqInput
    seq2seq.core.data.Seq2SeqFileInput
    seq2seq.core.data.Seq2SeqJSONInput
    seq2seq.core.data.Seq2SeqPostprocess
    seq2seq.core.data.Seq2SeqPreprocess
    seq2seq.core.data.Seq2SeqSentencesInput
    seq2seq.core.metrics.BLEUScore
    seq2seq.core.metrics.RougeBatchAggregator
    seq2seq.core.metrics.RougeMetric
