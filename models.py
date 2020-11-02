from tortoise import fields,models
from tortoise.contrib.pydantic import pydantic_model_creator

class todo(models.Model):
    id = fields.IntField(pk = True)
    todo = fields.CharField(max_length = 250)
    due_data = fields.CharField(max_length = 250)

    class PydanticMeta:
        pass

Todo_Pydantic = pydantic_model_creator(todo,name = "Todo")
TodoIn_Pydantic = pydantic_model_creator(todo, name = "TodoIn" , exclude_readonly = True)
