# Real FizzBuzz1
version number: 925cf7f189d1e404cfd55df6e8398d831df0f45a

Contains a class that produces the following for any contiguous range of integers:

* If the number contains a three you must output the text ‘lucky’. This overrides any existing behaviour
* the number
* ‘fizz’ for numbers that are multiples of 3
* ‘buzz’ for numbers that are multiples of 5
* ‘fizzbuzz’ for numbers that are multiples of 15

### Prerequisites

This project uses PyBuilder to build and automate tests. PyBuilder requires Python 3.6 or earlier. 

### Using this Class

This class accepts a starting and ending value, and returns a string following the above parameters. To use:

Import the class:

```
from fizzbuzz import fizzBuzz
```

Initialize a fizzBuzz object:

```
fizzbuzz =  fizzBuzz()
```

Use the 'fizzMyBuzz' method to print a string:

```
fizzbuzz.fizzMyBuzz(1,20)
```


### Building and Running Tests

Getting PyBuilder up and running is super easy! 

The first step is to initialize a Python virtual environment (make sure to not use Python 3.7, Python 3.6 is preferred):

```
python -m virtualenv venv
source venv/bin/activate
```

Then use pip to install PyBuilder:

```
pip install pybuilder
```

PyBuilder can handle installing any dependancies needed:

```
pyb install_dependancies
```

All that's left is to run PyBuilder and let it do it's magic:

```
pyb
```

You should see output that resembles:

```
PyBuilder version 0.11.17
Build started at 2018-10-18 15:58:22
------------------------------------------------------------
[INFO]  Building nr_real_fizzbuzz version 1.0.dev0
[INFO]  Executing build in /Users/mikebmc/Documents/job_hunting_2018/applications/Intersection/nr_real_fizzbuzz
[INFO]  Going to execute task publish
[INFO]  Running unit tests
[INFO]  Executing unit tests from Python modules in /Users/mikebmc/Documents/job_hunting_2018/applications/Intersection/nr_real_fizzbuzz/src/unittest/python
[INFO]  Executed 19 unit tests
[INFO]  All unit tests passed.
[INFO]  Building distribution in /Users/mikebmc/Documents/job_hunting_2018/applications/Intersection/nr_real_fizzbuzz/target/dist/nr_real_fizzbuzz-1.0.dev0
[INFO]  Copying scripts to /Users/mikebmc/Documents/job_hunting_2018/applications/Intersection/nr_real_fizzbuzz/target/dist/nr_real_fizzbuzz-1.0.dev0/scripts
[INFO]  Collecting coverage information
[WARN]  coverage_branch_threshold_warn is 0 and branch coverage will not be checked
[WARN]  coverage_branch_partial_threshold_warn is 0 and partial branch coverage will not be checked
[INFO]  Running unit tests
[INFO]  Executing unit tests from Python modules in /Users/mikebmc/Documents/job_hunting_2018/applications/Intersection/nr_real_fizzbuzz/src/unittest/python
[INFO]  Executed 19 unit tests
[INFO]  All unit tests passed.
[INFO]  Overall coverage is 100%
[INFO]  Overall coverage branch coverage is 100%
[INFO]  Overall coverage partial branch coverage is 100%
------------------------------------------------------------
BUILD SUCCESSFUL
------------------------------------------------------------
Build Summary
             Project: nr_real_fizzbuzz
             Version: 1.0.dev0
      Base directory: /Users/mikebmc/Documents/job_hunting_2018/applications/Intersection/nr_real_fizzbuzz
        Environments:
               Tasks: prepare [12 ms] compile_sources [0 ms] run_unit_tests [39 ms] package [3 ms] run_integration_tests [0 ms] verify [227 ms] publish [0 ms]
Build finished at 2018-10-18 15:58:22
Build took 0 seconds (296 ms)
```

## Built With

* [PyBuilder](http://pybuilder.github.io/) - Python Build Tool

