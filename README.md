# Python Authentication System

Simple authentication system on python modified by Grisha *HeavenOf22865*

## Tech Stack & Architecture

- **Language:** Python 3
- **GUI FrameWork:** TKinter

## Project Structure

```text
├── main.py             # Handles the visual interface of the main window
├── err_window.py       # Handles the visual interface of the error window
├── login_window.py     # Handles the visual interface of the login window
├── register_window.py  # Handles the visual interface of the register window
├── controller.py       # Manages user requests and updates the main/model
├── User.py             # User data model
├── user_repository.py  # Data access layer (saving/loading user data)
├── config.py           # Application configurations and constants
```

## Installation & Running

1. **Clone the repository:**

   ```bash
   git clone --branch Grisha-dayn --single-branch https://github.com/ALekcui/python-auth-system.git
   cd python-auth-system
   ```

2. **Run the application:**

   ```bash
   python main.py
   ```
