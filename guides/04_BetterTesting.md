# Testing Tips and Tricks
## Test Fixtures
Often, the first few lines of a test are dedicated to repeated "setup" that is unrelated to the test itself. Rather than repeat this for every test, this can be extracted to a [fixture](https://docs.pytest.org/en/stable/explanation/fixtures.html).

In our case, an efficient fixture to make would be one that provides us a fresh instance of the `SetSpeedManager`.

```python
import pytest
from set_speed_manager.manager import SetSpeedManager

@pytest.fixture
def speed_setpoint():
    return SetSpeedManager()

def test_initial_speed(speed_setpoint):
    return speed_setpoint.get_speed() == 0
```

> **Note:** The name of the fixture function determines the name of the passed input to the test.

## Parameterization
When multiple tests differ only in their inputs or expected results, they can be combined  into a [parameterized](https://docs.pytest.org/en/stable/how-to/parametrize.html#parametrize) test. This keeps the test logic in one place while still verifying multiple scenarios.

```python
import pytest
from set_speed_manager.manager import SetSpeedManager

@pytest.fixture
def speed_setpoint():
    return SetSpeedManager()

@pytest.mark.parametrize(
    "speed, expected",
    [
        pytest.param(-5, 0, id='below-minimum'),
        pytest.param(0, 0, id='minimum'),
        pytest.param(15, 15, id='normal'),
        pytest.param(65, 65, id='maximum'),
        pytest.param(70, 65, id='above-maximum'),
    ],
)
def test_speed_setting(speed_setpoint, speed, expected):
    speed_setpoint.set_speed(speed)
    assert speed_setpoint.get_speed() == expected
```

>**Note:** When selecting test parameters, think about where your code might behave differently, such as at minimums, maximums, and unusual inputs.

Each row in the parameter list is executed as a separate test. In this example, `test_speed_setting` runs five times, once for each (speed, expected) pair. This approach makes it easy to add new test cases by simply appending another row to the list.