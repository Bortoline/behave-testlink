Feature
======


    Feature: Calculator: Sum numbers
      As  a student user
      I   want to sum numbers
      so that  I can operate with them
    
    
      @Scenario1.Example<row.index>
      @TL.1.GRAVItY-101 @TL.2.GRAVItY-102 @TL.3.GRAVItY-103
      Scenario Outline: The sum of numbers is the expected one. TestLink ID in tags.
        Given the number "<number1>"
        When  I add the given number number to "<number2>"
        Then  the result is "<result>"
    
        Examples:
          | number1 | number2 | result |
          | 5       | 5       | 10     |
          | 3       | 2       | 5      |
          | 100     | 0       | 115    |
    
    
      @Scenario2.Example<row.index>
      @TL.<testlink>
      Scenario Outline: The sum of numbers is the expected one (2). TestLink ID in Examples.
        Given the number "<number1>"
        When  I add the given number number to "<number2>"
        Then  the result is "<result>"
    
        Examples:
          | number1 | number2 | result | testlink     |
          | 5       | 5       | 10     | GRAVItY-201  |
          | 3       | 2       | 5      | GRAVItY-202  |
          | 100     | 0       | 115    | GRAVItY-203  |
    
    
      @Scenario3
      @TL.GRAVITY-300
      Scenario: The sum of numbers is the expected one (3). Normal Scenario.
        Given the number "1"
        When  I add the given number number to "1"
        Then  the result is "2"



Output
======


    Feature: Calculator: Add numbers # features/example01.feature:2
      As  a student user
      I   want to sum numbers
      so that  I can operate with them
      @Scenario1.Example1 @TL.1.GRAVItY-101 @TL.2.GRAVItY-102 @TL.3.GRAVItY-103
      Scenario Outline: The sum of numbers is the expected one. TestLink ID in tags. -- @1.1   # features/example01.feature:17
        Given the number "5"                                                                   # features/steps/sum.py:6 0.000s
        When I add the given number number to "5"                                              # features/steps/sum.py:11 0.000s
        Then the result is "10"                                                                # features/steps/sum.py:16 0.000s
        >>>>>   - TEST LINK ID:  GRAVItY-101
        >>>>>   - STATUS:  passed
    
      @Scenario1.Example2 @TL.1.GRAVItY-101 @TL.2.GRAVItY-102 @TL.3.GRAVItY-103
      Scenario Outline: The sum of numbers is the expected one. TestLink ID in tags. -- @1.2   # features/example01.feature:18
        Given the number "3"                                                                   # features/steps/sum.py:6 0.000s
        When I add the given number number to "2"                                              # features/steps/sum.py:11 0.000s
        Then the result is "5"                                                                 # features/steps/sum.py:16 0.000s
        >>>>>   - TEST LINK ID:  GRAVItY-102
        >>>>>   - STATUS:  passed
    
      @Scenario1.Example3 @TL.1.GRAVItY-101 @TL.2.GRAVItY-102 @TL.3.GRAVItY-103
      Scenario Outline: The sum of numbers is the expected one. TestLink ID in tags. -- @1.3   # features/example01.feature:19
        Given the number "100"                                                                 # features/steps/sum.py:6 0.000s
        When I add the given number number to "0"                                              # features/steps/sum.py:11 0.000s
        Then the result is "115"                                                               # features/steps/sum.py:16 0.000s
          Assertion Failed: ERROR: The result is not the expected one
    
        >>>>>   - TEST LINK ID:  GRAVItY-103
        >>>>>   - STATUS:  failed
    
      @Scenario2.Example1 @TL.GRAVItY-201
      Scenario Outline: The sum of numbers is the expected one (2). TestLink ID in Examples. -- @1.1   # features/example01.feature:31
        Given the number "5"                                                                           # features/steps/sum.py:6 0.000s
        When I add the given number number to "5"                                                      # features/steps/sum.py:11 0.000s
        Then the result is "10"                                                                        # features/steps/sum.py:16 0.000s
        >>>>>   - TEST LINK ID:  GRAVItY-201
        >>>>>   - STATUS:  passed
    
      @Scenario2.Example2 @TL.GRAVItY-202
      Scenario Outline: The sum of numbers is the expected one (2). TestLink ID in Examples. -- @1.2   # features/example01.feature:32
        Given the number "3"                                                                           # features/steps/sum.py:6 0.000s
        When I add the given number number to "2"                                                      # features/steps/sum.py:11 0.000s
        Then the result is "5"                                                                         # features/steps/sum.py:16 0.000s
        >>>>>   - TEST LINK ID:  GRAVItY-202
        >>>>>   - STATUS:  passed
    
      @Scenario2.Example3 @TL.GRAVItY-203
      Scenario Outline: The sum of numbers is the expected one (2). TestLink ID in Examples. -- @1.3   # features/example01.feature:33
        Given the number "100"                                                                         # features/steps/sum.py:6 0.000s
        When I add the given number number to "0"                                                      # features/steps/sum.py:11 0.000s
        Then the result is "115"                                                                       # features/steps/sum.py:16 0.000s
          Assertion Failed: ERROR: The result is not the expected one
    
        >>>>>   - TEST LINK ID:  GRAVItY-203
        >>>>>   - STATUS:  failed
    
      @Scenario3 @TL.GRAVITY-300
      Scenario: The sum of numbers is the expected one (3). Normal Scenario.  # features/example01.feature:38
        Given the number "1"                                                  # features/steps/sum.py:6 0.000s
        When I add the given number number to "1"                             # features/steps/sum.py:11 0.000s
        Then the result is "2"                                                # features/steps/sum.py:16 0.000s
        >>>>>   - TEST LINK ID:  GRAVITY-300
        >>>>>   - STATUS:  passed
    
    
    Failing scenarios:
      features/example01.feature:19  The sum of numbers is the expected one. TestLink ID in tags. -- @1.3
      features/example01.feature:33  The sum of numbers is the expected one (2). TestLink ID in Examples. -- @1.3
    
    0 features passed, 1 failed, 0 skipped
    5 scenarios passed, 2 failed, 0 skipped
    19 steps passed, 2 failed, 0 skipped, 0 undefined
    Took 0m0.002s