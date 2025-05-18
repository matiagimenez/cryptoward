from cryptoward.injections import Environment, configure_injections


def test_configure_injections(environment: Environment) -> None:
    configure_injections(environment)
