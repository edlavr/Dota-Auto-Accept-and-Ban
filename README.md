# Dota_Auto_Accept

## Requirements

```pip install pyautogui```

```pip install imagehash```

## How to use

#### To use, run main.py, open your Dota 2 client and start the matchmaking search
#### The program will automatically press the 'Accept' button for you

## Auto Ban

#### You can also choose to automatically ban a hero, just specify the name as an argument!
#### The program will find the closest match to your input in the list of heroes (heroes.txt) and ban this hero

### Examples

```python3 main.py``` accepts the matchmaking but doesn't ban a hero

```python3 main.py invoker``` accepts the matchmaking and bans Invoker

```python3 main.py invok``` accepts the matchmaking and still bans Invoker