# Instagram Reels Auto Sharer

This Python script automates the process of sharing Instagram Reels with a specified user using Selenium WebDriver.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/your-repo/instagram-reels-auto-sharer.git
   cd instagram-reels-auto-sharer
   ```

2. **Install Python Packages:**
   Ensure you have Python 3 installed. Then install the required packages using pip.

   ```sh
   pip install selenium
   ```

3. **Download ChromeDriver:**
   Download the ChromeDriver that matches your version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/). Extract the file and place it in a directory.

4. **Edit the Script:**
   Update the `chrome_driver_path` variable in the script with the path to your ChromeDriver executable.

## Setup

1. **Environment Variables:**
   Create a `.env` file in the root directory and add your Instagram credentials and other configurations:

   ```env
   INSTAGRAM_USERNAME=your_username
   INSTAGRAM_PASSWORD=your_password
   USERNAME_TO_SEND_REELS=username
   NO_OF_REELS=50
   ```

2. **Update the Script:**
   Update the script to read from the `.env` file:

   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()

   insta_username = os.getenv('INSTAGRAM_USERNAME')
   insta_password = os.getenv('INSTAGRAM_PASSWORD')
   username_to_send_the_reels = os.getenv('USERNAME_TO_SEND_REELS')
   no_of_reels = int(os.getenv('NO_OF_REELS'))
   ```

## Usage

1. **Run the Script:**
   Execute the script using Python.

   ```sh
   python script_name.py
   ```

2. **Script Flow:**
   - The script opens Instagram's login page.
   - Logs in using the provided credentials.
   - Navigates to the Reels page.
   - Iteratively shares the specified number of Reels with the specified user.

## Troubleshooting

- **Common Issues:**

  - **Element Not Found:** Ensure that the XPaths and element selectors match the current Instagram layout.
  - **Login Issues:** Verify that the credentials in the `.env` file are correct.
  - **ChromeDriver Version:** Ensure that the ChromeDriver version matches your installed version of Chrome.

- **Logging:**
  The script includes print statements for debugging. If an element is not found, it prints a corresponding message. Adjust the XPaths if necessary.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

### Notes:
- Replace `script_name.py` with the actual name of your script file.
- Ensure the `.env` file setup section is correctly implemented in your script for reading environment variables.

This `README.md` provides a comprehensive guide for setting up, running, and troubleshooting your Selenium script. Adjust paths and instructions as needed to fit your project structure.
```
