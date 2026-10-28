# Python Authentication System

Simple authentication system on python

## Tech Stack & Architecture

- **Language:** Python 3
- **GUI FrameWork:** TKinter

## Project Structure

```text
├── main.py             # Handles the visual interface of the authentication window
├── err_window.py       # Handles the visual interface of the error window
├── controller.py       # Manages user requests and updates the main/model
├── User.py             # User data model
├── user_repository.py  # Data access layer (saving/loading user data)
├── config.py           # Application configurations and constants
```

## Installation & Running

1. **Clone the repository:**

   ```bash
   git clone git@github.com:ALekcui/python-auth-system.git
   cd python-auth-system
   ```

2. **Run the application:**

   ```bash
   python main.py
   ```
