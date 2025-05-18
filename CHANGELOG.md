# CHANGELOG


## v0.3.0 (2025-05-18)

### Bug Fixes

- **config**: Remove unused config class from settings
  ([`ed8135d`](https://github.com/matiagimenez/cryptoward/commit/ed8135df04935f8f562ab3d70d2a9f7576e7e0b3))

- **config**: Set default values for KAFKA_HOST and KAFKA_TOPIC
  ([`8e9c73c`](https://github.com/matiagimenez/cryptoward/commit/8e9c73cfab609ee32bd856a69acdcc0f3427afa8))

- **test**: Add fixtures for kafka settings
  ([`f4930d1`](https://github.com/matiagimenez/cryptoward/commit/f4930d1fff9c4718951d6cf39cf069291e2f546f))

- **test**: Add kafka settings fixtures for consistent test environment
  ([`53fc2a5`](https://github.com/matiagimenez/cryptoward/commit/53fc2a5a6e70cbe6a581ae57493bf25a5fc5f740))

- **test**: Add tests for kafka event handler
  ([`3fa9446`](https://github.com/matiagimenez/cryptoward/commit/3fa944615d25d0d8588c30780bd3b06af28ebcd6))

- **test**: Correct pytest_plugins path in conftest
  ([`fd9b508`](https://github.com/matiagimenez/cryptoward/commit/fd9b50868c6a80414417a99589c6f892710b4a94))

- **test**: Move fixtures to correct test module
  ([`511a3e1`](https://github.com/matiagimenez/cryptoward/commit/511a3e1dbf1dd9079911e660711bcbbc532e7b5c))

- **test**: Update pytest_plugins path to include tests directory
  ([`6fb4947`](https://github.com/matiagimenez/cryptoward/commit/6fb4947ff88adb826e8080b7dd262b2143079020))

### Chores

- **config**: Add initial docker-compose configuration for Kafka and Kafka UI
  ([`da3be94`](https://github.com/matiagimenez/cryptoward/commit/da3be948999d081c11a11a6d54be3a2e64a61fd9))

- **config**: Add missing step to run unit tests
  ([`f7b9e23`](https://github.com/matiagimenez/cryptoward/commit/f7b9e23a8143bd053f4a52f0262a14a70ee03126))

- **config**: Integrates pycracks in workflow
  ([`e6dee48`](https://github.com/matiagimenez/cryptoward/commit/e6dee48dbdc0a945438e1085c87bd6f7d201f66a))

- **config**: Remove breaking changes check step from workflow
  ([`9d11e0d`](https://github.com/matiagimenez/cryptoward/commit/9d11e0d48ea63319941ac6d5da5f0fb32d558fb6))

- **config**: Update docs
  ([`7cd664a`](https://github.com/matiagimenez/cryptoward/commit/7cd664aecf77a0893eefdcadeeec7ece79149c7e))

- **config**: Update kafka configuration and add topic initialization script
  ([`a73e6fa`](https://github.com/matiagimenez/cryptoward/commit/a73e6fa0be80b5473dc46e61c8a76e2080558f3d))

- **config**: Update pre-commit hooks
  ([`b06670f`](https://github.com/matiagimenez/cryptoward/commit/b06670f2ca6d2c457d054a64a934a11835bc6617))

- **config**: Update semantic-release and pycracks installation steps
  ([`df9e23a`](https://github.com/matiagimenez/cryptoward/commit/df9e23a7ad4ec458c8abef7c1e76602603ada02f))

- **dependencies**: Add kafka-python and mockafka-py
  ([`e41dccd`](https://github.com/matiagimenez/cryptoward/commit/e41dccd965a6bb0985af1c3af5019ff5f43f044d))

### Features

- **config**: Implement dependency injection
  ([`0e63d67`](https://github.com/matiagimenez/cryptoward/commit/0e63d6728f21ffd7e5193525f7ea3805b599d3a4))

- **config**: Implement kafka and fake event handlers
  ([`c4016b9`](https://github.com/matiagimenez/cryptoward/commit/c4016b9ee4532e245ce109d1514940bd8f3d1044))


## v0.2.0 (2025-05-18)

### Features

- **config**: Add cryptocurrency scrapper
  ([`d4c9e99`](https://github.com/matiagimenez/cryptoward/commit/d4c9e99432ca00b40b9bb0f7557821911cd1ffc7))


## v0.1.0 (2025-05-17)

### Chores

- **config**: Add autoupdate for pre-commit hooks and commit changes
  ([`55205c8`](https://github.com/matiagimenez/cryptoward/commit/55205c867ff587b8c72078da127b8f36d8aca9c0))

- **config**: Add condition to bump version only on main branch
  ([`e2167d7`](https://github.com/matiagimenez/cryptoward/commit/e2167d7948bd6dcd6b7e1ba4415484528ff9a499))

- **config**: Enable schedule task for pre-commit autoupdate
  ([`aee1122`](https://github.com/matiagimenez/cryptoward/commit/aee112201d71415468a4b364542fb91fbe62085d))

- **config**: Refactor CI workflow to separate lint and test jobs
  ([`dfb29fc`](https://github.com/matiagimenez/cryptoward/commit/dfb29fc18b8eca689e6f824b6df2f684329a8eab))

- **config**: Remove schedule package
  ([`d534382`](https://github.com/matiagimenez/cryptoward/commit/d534382c32555cdcce884323defda8ba5c654647))

- **config**: Update pre-commit hooks
  ([`60722ec`](https://github.com/matiagimenez/cryptoward/commit/60722ecbe1d9eff295b866ee03e1cb7e0ea23575))

- **config**: Update pre-commit hooks installation and configuration
  ([`12bd808`](https://github.com/matiagimenez/cryptoward/commit/12bd808724963d482bd65b3d942a65c09214d0fe))

### Features

- **config**: Implement logging functionality
  ([`96e1f5a`](https://github.com/matiagimenez/cryptoward/commit/96e1f5ac3cd663f44b094313e87bbb2c3141e601))


## v0.0.0 (2025-05-17)

### Chores

- **config**: Repository initial setup
  ([`08c898e`](https://github.com/matiagimenez/cryptoward/commit/08c898e1df9db49ac1562b45cc99bd3d30d18f25))
