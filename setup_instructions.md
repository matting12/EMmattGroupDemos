# Python Style Checker Setup

## Installation Steps

### 1. Install flake8
```bash
pip install flake8
```

### 2. Set up the pre-commit hook
```bash
# Navigate to your git repository
cd /path/to/your/repo

# Create the hooks directory if it doesn't exist
mkdir -p .git/hooks

# Create the pre-commit hook file
# Copy the pre-commit script content to this file
nano .git/hooks/pre-commit

# Make it executable
chmod +x .git/hooks/pre-commit
```

### 3. Add flake8 configuration (optional)
```bash
# Copy the .flake8 config to your project root
# This allows you to customize the style rules
```

## Usage

Once set up, the style checker will automatically run whenever you try to commit Python files:

```bash
# Stage your changes
git add your_file.py

# Commit - this will trigger the style check
git commit -m "Your commit message"
```

### If style checks fail:
- Fix the reported issues
- Stage the fixes: `git add your_file.py`
- Try committing again

### To bypass the check (use sparingly):
```bash
git commit --no-verify -m "Your commit message"
```

## Common PEP8 Violations

- **E501**: Line too long (> 79 characters)
- **E302**: Expected 2 blank lines, found 1
- **E303**: Too many blank lines
- **W291**: Trailing whitespace
- **E265**: Block comment should start with '# '
- **F401**: Module imported but unused
- **E401**: Multiple imports on one line

## Customization

Edit `.flake8` to:
- Change max line length
- Ignore specific error codes
- Exclude directories
- Adjust complexity thresholds