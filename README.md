
## Setup & Usage

### 1. Clone Repo
```bash
git clone https://github.com/adarsh-gowda/name_matching_system.git
cd name_matching_system
```

### 2. Setup Environment
```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt

```
### 4.Run script
```bash
python main.py

```
You’ll be prompted to enter a name:
```bash


Enter a name to search (or type 'quit'/'exit' to stop): Githa

Input Name: Githa
Best Match: ('Githa', 100.0, 5)

Ranked Matches:
Githa → 100.0
Gita → 88.88888888888889
Githu → 80.0

```
To exit:
```bash
Enter a name to search (or type 'quit'/'exit' to stop): quit
Exiting the name matcher. Goodbye!


```
