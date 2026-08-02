# 🥟 Dumpling Macro

A desktop automation tool for automating dumpling upgrades.

Dumpling Macro uses configurable screen coordinates, color detection, and a toggle hotkey to automate repetitive upgrade actions while allowing the user to easily configure positions for their own game setup.

---

# ✨ Features

- Cross-platform support:
  - Windows
  - Linux

- Modern PyQt6 interface

- Custom coordinate setup:
  - Dumpling 1
  - Dumpling 2
  - Dumpling 3
  - Auto Upgrade
  - Upgrade Start
  - Change Dumpling
  - Color Detect

- Automatic saving:
  - Coordinates
  - Timing settings

- F8 toggle control:
  - Press F8 once → Start
  - Press F8 again → Stop

- Smart color detection:
  - Detects the SS already-owned notification

- Forward and reverse upgrade cycles

- Interruptible waiting:
  - Long waits can still be stopped instantly

---

# 📦 Requirements

## Python

Python 3.10 or newer is recommended.

Check your version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Juke1992kilum/Dumpling-Auto-Upgrade-Inventory-Macro
```

Enter the project folder:

```bash
cd Dumpling-Auto-Upgrade-Inventory-Macro

```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Program

Start the application:

```bash
python main.py
```

The Dumpling Macro window will open.

---

# 🎮 Game Setup Tutorial

Before running the macro, the coordinate points must be configured.

The game must be in the correct upgrade interface.

The program works by clicking specific locations, so accurate point placement is extremely important.

---

# Point Configuration

## Point 1 — Dumpling 1

Select the **left-most dumpling** in the upgrade window.

Example:

```
[Dumpling 1]   [Dumpling 2]   [Dumpling 3]
```

Click:

```
Set Dumpling 1
```

Then click the center area of the left dumpling.

---

## Point 2 — Dumpling 2

Select the **middle dumpling**.

Important:

Points 1, 2, and 3 should be placed on the same horizontal imaginary line.

Example:

```
       X           X           X

   Dumpling 1  Dumpling 2  Dumpling 3
```

Do not place one point higher or lower than the others.

Click:

```
Set Dumpling 2
```

Then select the center area of the middle dumpling.

---

## Point 3 — Dumpling 3

Select the **right-most dumpling**.

Click:

```
Set Dumpling 3
```

Place the point at the same vertical height as Dumpling 1 and Dumpling 2.

---

# Auto Upgrade Setup

## Point 4 — Auto Upgrade

1. Enter one of the dumpling upgrade screens.
2. Locate the Auto Roll button.
3. Click:

```
Set Auto Upgrade
```

4. Select the Auto Roll button location.

This point is used to open the auto upgrade menu.

---

# Upgrade Start Setup

## Point 5 — Upgrade Start

Inside the Auto Roll window:

1. Make sure:

```
SS
```

is selected.

2. Find:

```
Start Auto Roll
```

3. Click:

```
Set Upgrade Start
```

4. Select the Start Auto Roll button.

---

# Change Dumpling Setup

## Point 6 — Change Dumpling

Point 6 is the button used to change dumplings.

Click:

```
Set Change Dumpling
```

Then select the Change Dumpling button.

This is also where the macro finishes every upgrade cycle.

---

# Color Detection Setup

## Point 7 — Color Detect

This point is used to detect the orange SS notification.

When starting Auto Roll on a dumpling that already has SS:

You will see an orange message:

```
This dumpling is already SS
```

The orange text disappears quickly.

Follow these steps:

1. Press Start Auto Roll.
2. When the orange SS message appears:
   - Put your finger on the orange letters.
   - Do not move.
   - Do not release until the point is saved.

3. Alt-tab back to Dumpling Macro.

4. Click:

```
Set Color Detect
```

5. Alt-tab back into the game.

6. Move your mouse to where your finger is holding.

7. Click directly on the orange part of the letters.

The point must be placed on the orange text itself.

The color detector specifically checks:

```
RGB:
255, 205, 112

Hex:
#ffcd70
```

---

# Starting the Macro

After all points are configured:

1. Return to the main dumpling upgrade screen.

The screen should show the normal dumpling overview.

2. Minimize Dumpling Macro.

3. Press:

```
F8
```

The macro will start.

---

# Macro Behavior

The macro follows this sequence:

```
Dumpling 1
    ↓
Auto Upgrade
    ↓
Upgrade Start
    ↓
Color Detect
    ↓
Change Dumpling


Dumpling 2
    ↓
Auto Upgrade
    ↓
Upgrade Start
    ↓
Color Detect
    ↓
Change Dumpling


Dumpling 3
    ↓
Auto Upgrade
    ↓
Upgrade Start
    ↓
Color Detect
    ↓
Change Dumpling
```

Then it scrolls and repeats in reverse:

```
Dumpling 3
Dumpling 2
Dumpling 1
```

The cycle continues until stopped.

---

# Controls

## Start / Stop

### Keyboard

```
F8
```

Toggle:

```
Stopped → Running
Running → Stopped
```

### UI Button

The Start/Stop button performs the same action.

---

# Troubleshooting

## Macro clicks the wrong dumpling

Reconfigure:

- Dumpling 1
- Dumpling 2
- Dumpling 3

Make sure they are:

- Centered on each dumpling
- On the same horizontal line

---

## Color detection does not work

Check:

- Point 7 is directly on the orange text.
- The orange portion is not partially transparent.
- The game window is not resized after setting points.

---

## Macro starts but does nothing

Check:

- All seven points are configured.
- The game is on the correct screen.
- The macro window is minimized.
- F8 was pressed.

---

# Settings

The program automatically creates:

```
settings.json
```

This stores:

- Point coordinates
- Timing settings

You do not need to edit this manually.

---

# Disclaimer

This tool is designed to automate repetitive user actions.

Use responsibly and ensure automation is allowed by the game's rules and terms of service.
