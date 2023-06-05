def run_and_test_app() -> bool:
    from subprocess import call, run

    result: list[bool] = []
    action: str = input(
        "actions = start | restart | test | test and start | test and restart | check | stop | --build\n> "
    )
    build: bool = False
    if action.endswith("--build"):
        build = True
        action = action.split(" --")[0]

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

    def _start(command: list[str], test: bool = False) -> bool:
        if test:
            command = command + ["mongodb_test"]
        else:
            command = command + ["mongodb", "postgres", "web"]

        try:
            _check()
            call(command)
        except Exception as e:
            print(e)
            return False
        return True

    def _stop(test: bool = False) -> bool:
        try:
            if test:
                run(
                    ["docker-compose", "rm", "-s", "-v", "mongodb_test"],
                    input="y",
                    encoding="ascii",
                )
            else:
                call(["docker-compose", "down"])
            run(["docker", "container", "prune"], input="y", encoding="ascii")
            run(["docker", "image", "prune"], input="y", encoding="ascii")
        except Exception as e:
            print(e)
            return False
        return True

    start_command: list[str] = ["docker-compose", "up", "-d"]
    start_command.append("--build") if build else start_command

    def _test_all() -> None:
        result.append(_stop(test=True))
        result.append(_start(command=start_command, test=True))
        result.append(_test())
        result.append(_stop(test=True))

    match action:
        case "start":
            result.append(_start(command=start_command))
        case "restart":
            result.append(_stop())
            result.append((_start(command=start_command)))
        case "test":
            _test_all()
        case "test and start":
            _test_all()
            result.append(_start(command=start_command))
        case "test and restart":
            _test_all()
            _stop()
            result.append(_start(command=start_command))
        case "check":
            result.append(_check())
        case "stop":
            result.append(_stop())
        case _:
            print("Please pass a valid argument")
            result.append(False)
    return all(result)


if __name__ == "__main__":
    run_and_test_app()
