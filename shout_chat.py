from DashAI.back.core.schema_fields import BaseSchema
from DashAI.back.core.utils import MultilingualString
from DashAI.back.models.text_to_text_generation_model import (
    TextToTextGenerationTaskModel,
)
from DashAI.back.tasks.text_to_text_generation_task import TextToTextGenerationTask


class ShoutChatTask(TextToTextGenerationTask):
    DISPLAY_NAME = MultilingualString(
        en="Shout chat (plugin)", es="Chat gritón (plugin)"
    )


class ShoutSchema(BaseSchema):
    pass


class ShoutModel(TextToTextGenerationTaskModel):
    COMPATIBLE_COMPONENTS = ["ShoutChatTask"]
    SCHEMA = ShoutSchema
    DISPLAY_NAME = MultilingualString(en="Shout (plugin)", es="Grito (plugin)")

    def __init__(self, **kwargs):
        pass

    def generate(self, input):
        last = input[-1]["content"] if isinstance(input, list) else str(input)
        return [f"{last.upper()}!"]
