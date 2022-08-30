from tortoise import Model, fields


class Todo(Model):
    """数据库中表 todo"""
    id = fields.IntField(pk=True)
    content = fields.CharField(max_length=500)
    # 每一次新增都会自动使用当前时间
    created_time = fields.DatetimeField(auto_now_add=True)
    # 每一次修改都会更新
    updated_time = fields.DatetimeField(auto_now=True)
