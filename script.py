def run_and_test_app() -> bool:
    from subprocess import call, run

    result: list[bool] = []
    action: str = input(
        "actions = start | restart | test | test and start | test and restart | check | stop\n> "
    )

    def _check() -> bool:
        try:
            call(["black", "."])
            call(["mypy", "."])
            with open("requirements.txt", "w") as f:
                call(["pipenv", "requirements", "--dev"], stdout=f)
        except Exception as e:
            print(e)
            return False
        return True

    def _test() -> bool:
        try:
            call(["coverage", "run", "-m", "pytest"])
            call(["coverage", "report"])
        except Exception as e:
            print(e)
            return False
        return True

    def _start(command: list[str]) -> bool:
        try:
            _check()
            call(command)
        except Exception as e:
            print(e)
            return False
        return True

    def _stop(command: list[str]) -> bool:
        try:
            call(command)
            run(["docker", "container", "prune"], input="y", encoding="ascii")
            run(["docker", "image", "prune"], input="y", encoding="ascii")
        except Exception as e:
            print(e)
            return False
        return True

    start_command_prefix: list[str] = [
        "docker-compose",
        "-f",
        "docker-compose-mongo.yml",
        "-f",
        "docker-compose-postgres.yml",
        "-f",
        "docker-compose-web.yml",
    ]
    test_command_prefix: list[str] = [
        "docker-compose",
        "-f",
        "docker-compose-mongo.yml",
    ]

    start_command_suffix: list[str] = ["up", "-d", "--build"]
    stop_command_suffix: list[str] = ["down"]

    start_command: list[str] = start_command_prefix + start_command_suffix
    stop_command: list[str] = start_command_prefix + stop_command_suffix
    test_start_command: list[str] = test_command_prefix + start_command_suffix
    test_stop_command: list[str] = test_command_prefix + stop_command_suffix

    def _stop_all() -> None:
        result.append(_stop(command=stop_command))
        result.append(_stop(command=test_stop_command))

    def _test_all() -> None:
        _stop_all()
        result.append(_start(command=test_start_command))
        result.append(_test())

    match action:
        case "start":
            result.append(_start(command=start_command))
        case "restart":
            _stop_all()
            result.append((_start(command=start_command)))
        case "test":
            _test_all()
            result.append(_stop(command=test_stop_command))
        case "test and start":
            _test_all()
            result.append(_stop(command=test_stop_command))
            result.append(_start(command=start_command))
        case "test and restart":
            _test_all()
            _stop_all()
            result.append(_start(command=start_command))
        case "check":
            result.append(_check())
        case "stop":
            _stop_all()
        case _:
            print("Please pass a valid argument")
            result.append(False)
    return all(result)


if __name__ == "__main__":
    run_and_test_app()
