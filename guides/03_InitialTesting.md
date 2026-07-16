# Testing Developed Software
Testing is the process of verifying that software behaves as expected. Tests provide confidence that the code satisfies its requirements and continues to work as changes are made.

A good test:
- Verifies one specific behavior.
- Can be run repeatedly with the same result.
- Clearly indicates whether the software passed or failed.

For this project, tests will be used to verify that the `SetSpeedManager` satisfies the requirements defined in the [requirements](../REQUIREMENTS.md).

## Creating Your First Test

Before testing `SetSpeedManager`, you must first build and source your package. This installs your package into the workspace environment so Python can import it.

```bash
colcon build
source install/setup.bash
```

> **Note:** Make sure that you run these commands in `/workspaces/learn-ros2-cavs` and not your package directory.

Next, you'll want to create a new file to test your module. Put this in the `<package_name>/test/` directory and name it `test_<module_name>.py`. Inside this file, import your module and write a basic test using the [pytest](https://docs.pytest.org/en/stable/) framework.

```python
from Set_Speed_Manager.manager import SetSpeedManager

def test_initial_set_speed():
    SSM = SetSpeedManager()
    assert SSM.get_speed() == 0
```

The assert statement above verifies that a newly created `SetSpeedManager` starts with a speed of 0. The test passes if the expression after assert evaluates to True.

> **Note:** Your package must be built before it can be imported. Imports follow the format `from package_name.module_name import class`.

## Running Your First Test

Once you've written your test, run all tests in the workspace using:

```bash
colcon test
colcon test-result --verbose
```

> **Note:** By default, packages include `pep257`, `flake8`, and `copyright` tests to check documentation, formatting, and licensing requirements. These tests are separate from the functionality tests you will write for `SetSpeedManager`.
>
> If these tests are failing, you can temporarily skip them using the `@pytest.mark.skip` decorator:
>
> ```python
> import pytest
>
> @pytest.mark.skip(reason="Not implemented yet")
> def test_example():
>     ...
> ```
>
> Remove the skip marker once you are ready to address these checks.


If all tests pass, you'll see a summary indicating they completed successfully. If a test fails, the output will identify the failing test and display the assertion that failed, helping you determine what behavior did not match the expected result.

## Writing More Tests

Continue adding tests as you implement the requirements. Each requirement should have one or more tests that verify the expected behavior of your code.

When you make changes to your code, you'll need to **rebuild your workspace** before running the tests again:

```bash
colcon build
colcon test
```

<!-- This causes issues with the import for some reason
> **Tip:** During development, you can build your workspace with `--symlink-install`:
>
> ```bash
> colcon build --symlink-install
> ```
>
> This makes it faster to test changes by using your updated Python files directly instead of requiring a rebuild after every edit. You will still need to rebuild when **adding new files or changing your package configuration**.
-->