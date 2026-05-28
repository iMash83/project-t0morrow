# project-t0morrow

Personal assistant bot — starting point for a refactor of the existing monolithic assistant into a modular structure.

## Planned structure

- `main.py` — entry point / CLI loop
- `commands.py` — command handlers (add, change, phone, all, add-birthday, show-birthday, birthdays, etc.)
- `contacts.py` — `Field`, `Name`, `Phone`, `Birthday`, `Record`, `AddressBook`
- `notes.py` — notes feature (to be added)
- `validators.py` — `input_error` decorator and input validation helpers
- `storage.py` — `save_data` / `load_data` (pickle persistence)

## Run

```
python main.py
```

## Requirements

See `requirements.txt`.
