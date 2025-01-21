Hi, how are you? Thanks for reading this PR. This test is part of a series of validations the [Guará](https://github.com/douglasdcm/guara) team is conducting to explore and demonstrate the capabilities of the framework in real-world scenarios. By applying the Page Transactions pattern, we aim to simplify automation workflows while enhancing code readability, scalability, and maintainability.

This specific test showcases how Guará streamlines the process of interacting with dynamic web pages like Amazon, encapsulating actions like opening the home page and signing in into reusable transactions. Through this approach, we emphasize how automation can be both clean and intuitive, enabling teams to focus on validating critical business logic while keeping the implementation details neatly abstracted.

As we continue testing Guará’s potential, we’re excited to show how this pattern seamlessly adapts to diverse test cases and web environments, reinforcing its flexibility and power. Stay tuned for more examples and insights!

Key Changes and Benefits

    Encapsulation of Actions:
        OpenAmazonHomePage: Encapsulates opening the Amazon home page.
        SignIn: Handles all the actions and interactions related to signing in.
    Test Flow Simplification:
    The test case (test_successful_signin) becomes easy to read and focuses only on describing the test steps without implementation details.
    Reusability:
    The OpenAmazonHomePage and SignIn transactions can be reused across multiple test cases.
    Maintainability:
    If the locator values change, updates are localized to the transaction classes, minimizing the impact on the test case itself.

This refactor aligns the code with the Page Transactions pattern, improving readability, scalability, and maintainability.