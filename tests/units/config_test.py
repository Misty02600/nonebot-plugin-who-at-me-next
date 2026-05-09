def test_config_can_be_instantiated():
    from nonebot_plugin_who_at_me_next.config import Config

    assert Config().model_dump() == {}
