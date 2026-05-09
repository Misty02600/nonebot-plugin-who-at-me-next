def test_config_can_be_instantiated():
    from nonebot_plugin_template.config import Config

    assert Config().model_dump() == {}
