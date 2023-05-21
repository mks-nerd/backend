def run_and_test_app() -> bool:
    from subprocess import call, run

    result: list[bool] = []
    action: str = input("actions: str = run | run and test | stop\n> ")

    def _test() -> bool:
        try:
            call(["coverage", "run", "-m", "pytest"])
            call(["coverage", "report"])
        except Exception as e:
            print(e)
            return False
        return True

    def _stop() -> bool:
        try:
            call(["docker-compose", "down"])
            run(["docker", "container", "prune"], input="y", encoding="ascii")
            run(["docker", "image", "prune"], input="y", encoding="ascii")
        except Exception as e:
            print(e)
            return False
        return True

    def _run() -> bool:
        try:
            call(["docker-compose", "up", "-d"])
        except Exception as e:
            print(e)
            return False
        return True

    with open("requirements.txt", "w") as f:
        call(["pipenv", "requirements", "--dev"], stdout=f)

    call(["black", "."])
    call(["mypy", "."])

    match action:
        case "run":
            result.append(_run())
        case "run and test":
            result.append(_run())
            result.append(_test())
        case "stop":
            result.append(_stop())
        case _:
            print("Please pass a valid argument")
            result.append(False)
    return all(result)


if __name__ == "__main__":
    run_and_test_app()
