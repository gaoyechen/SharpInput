# Privacy and Local State

SharpInput is a prompt/input optimization skill. It should not publish or commit real user preference history.

## What the repository contains

The public repository only contains sanitized state definitions:

```text
references/user-preferences.schema.json
references/user-preferences.example.json
```

These files are safe to commit because they contain schema/default structure, not personal history.

## What must stay local

Real runtime preference data should be stored in the active user's local Hermes profile data directory, for example:

```text
$HERMES_HOME/data/sharpinput/user-preferences.json
```

If `$HERMES_HOME` is unavailable, use the equivalent active agent/profile data directory.

Do **not** write private preferences into:

```text
references/user-preferences.json
```

That path is ignored by git and reserved only as a legacy migration source for older installs.

## Why this matters

Keeping runtime state outside the skill package prevents:

- leaking the author's personal usage history into the public repo
- new users inheriting someone else's preferences
- skill updates overwriting user preferences
- multiple Hermes profiles sharing the wrong state
- dirty git working trees after normal skill usage

## Resetting preferences

If the user says "重置偏好" or "reset preferences", clear the runtime file contents back to the empty example shape.

CLI reset example:

```bash
mkdir -p "$HERMES_HOME/data/sharpinput"
cp references/user-preferences.example.json "$HERMES_HOME/data/sharpinput/user-preferences.json"
```

Or delete the file and let SharpInput run with no preferences:

```bash
rm -f "$HERMES_HOME/data/sharpinput/user-preferences.json"
```

## Legacy migration

Older SharpInput versions stored preferences under:

```text
references/user-preferences.json
references/user-preferences.md
```

If either file exists in an installed package and contains real data:

1. Copy it once into the runtime state path.
2. Validate or normalize it against `references/user-preferences.schema.json`.
3. Remove the legacy file from the installed skill package.
4. Never commit the migrated runtime file.

## Data handling promise

SharpInput itself does not require any network upload of preference data. Preference state is intended to remain local to the user's active Hermes profile.
