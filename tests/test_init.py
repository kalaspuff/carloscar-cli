import carloscar


def test_init() -> None:
    assert carloscar

    assert isinstance(carloscar.__version_info__, tuple)
    assert carloscar.__version_info__
    assert isinstance(carloscar.__version__, str)
    assert len(carloscar.__version__)
