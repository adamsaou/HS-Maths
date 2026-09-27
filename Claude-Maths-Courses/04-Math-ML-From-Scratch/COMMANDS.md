# Commands

Always run from repo root: `cd C:\Users\HP\math-ml-from-scratch`

## Compile

```powershell
g++ -std=c++20 -Wall -Wextra -g -I linalg/include linalg/tests/test_vec2.cpp -o test_vec2
```

Swap the test file and the output name for other tests.

## Run

```powershell
.\test_vec2.exe
```

Note the `.\` — PowerShell needs it.

## Git

```powershell
git status              # what's changed
git add .
git commit -m "message"
git push
```

## Flags, what they mean

- `-std=c++20`  language version
- `-Wall -Wextra`  turn on warnings (leave these on)
- `-g`  debug symbols
- `-I linalg/include`  where to find headers, so `#include "Vec2.h"` works
- `-o name`  name of the output .exe

## Fixes

- `error: src refspec main does not match any` → nothing committed yet, commit first
- `remote origin already exists` → use `git remote set-url origin URL`
- Writing files with `>` in PowerShell breaks encoding → use `Set-Content -Encoding ascii`