# Install SharpInput

SharpInput is distributed as a Hermes Agent skill package.

Canonical skill name from v3.1 onward:

```text
sharpinput
```

Older installs may appear as `SharpInput`. Remove or archive the old folder before installing the new package to avoid duplicate entries.

---

## 1. Install for Hermes Agent

### Windows / Git Bash

```bash
git clone https://github.com/gaoyechen/SharpInput.git
mkdir -p "$LOCALAPPDATA/hermes/skills/sharpinput"
cp -R SharpInput/* "$LOCALAPPDATA/hermes/skills/sharpinput/"
```

Equivalent native Windows path:

```text
C:\Users\<your-user>\AppData\Local\hermes\skills\sharpinput
```

### macOS / Linux

```bash
git clone https://github.com/gaoyechen/SharpInput.git
mkdir -p ~/.hermes/skills/sharpinput
cp -R SharpInput/* ~/.hermes/skills/sharpinput/
```

### Reload Hermes skills

In an existing Hermes session:

```text
/reload-skills
```

Or start a new Hermes session.

### Use it

```text
/skill sharpinput
```

Then ask:

```text
帮我优化：为什么我的 GitHub skill 没有 star？
```

---

## 2. Verify installation

CLI verification:

```bash
hermes skills list | grep -i sharpinput
```

Expected: one main skill named `sharpinput`.

A healthy v3.1 install should **not** show internal modules as separate skills, such as:

```text
sharpinput-context-completion
sharpinput-prompt-compiler
sharpinput-judge-review
```

If those appear, you probably installed an older package layout where internal modules lived under `skills/*/SKILL.md`.

Run an actual trigger test:

```bash
hermes chat --skills sharpinput -q "帮我优化：为什么我的 GitHub skill 没有 star？请输出一个可以直接复制给 AI 的提问。" -Q
```

Expected output should include a SharpInput identification section and an upgraded prompt, for example:

```text
SharpInput 识别：
Level: ...
...
可直接复制给 AI 的提问：
> ...
```

---

## 3. Upgrade from old `SharpInput` installs

If you previously installed a folder named `SharpInput`, remove or archive it first.

### Windows / Git Bash

```bash
backup_dir="$LOCALAPPDATA/hermes/skills-backups"
mkdir -p "$backup_dir"
mv "$LOCALAPPDATA/hermes/skills/SharpInput" "$backup_dir/SharpInput.backup.$(date +%Y%m%d-%H%M%S)" 2>/dev/null || true
rm -rf "$LOCALAPPDATA/hermes/skills/sharpinput"
mkdir -p "$LOCALAPPDATA/hermes/skills/sharpinput"
cp -R SharpInput/* "$LOCALAPPDATA/hermes/skills/sharpinput/"
```

### macOS / Linux

```bash
backup_dir=~/.hermes/skills-backups
mkdir -p "$backup_dir"
mv ~/.hermes/skills/SharpInput "$backup_dir/SharpInput.backup.$(date +%Y%m%d-%H%M%S)" 2>/dev/null || true
rm -rf ~/.hermes/skills/sharpinput
mkdir -p ~/.hermes/skills/sharpinput
cp -R SharpInput/* ~/.hermes/skills/sharpinput/
```

Then reload:

```text
/reload-skills
```

---

## 4. Troubleshooting

### `hermes skills install <raw-url>` fails

The GitHub API may rate-limit unauthenticated requests. Manual copy installation is the most reliable path.

If you want to use the official installer, authenticate GitHub first:

```bash
gh auth login
```

or set a GitHub token in your Hermes `.env`.

### Skill appears but does not trigger

Check:

1. Did you load it?
   ```text
   /skill sharpinput
   ```
2. Did you start a fresh session or run `/reload-skills`?
3. Is your request asking to optimize the input itself? SharpInput intentionally should not trigger for direct coding, factual lookup, file edits, or data analysis.

### Too many SharpInput entries appear

If `hermes skills list` shows internal modules as standalone skills, remove the old install and reinstall v3.1+.

A correct installed package should have this internal layout:

```text
sharpinput/
├── SKILL.md
├── AGENT.md
├── modules/
├── references/
├── examples/
└── tests/
```

There should be no nested `skills/*/SKILL.md` inside the package.

### Preference data looks wrong

Runtime preferences should be private local state, not committed files. See [PRIVACY.md](PRIVACY.md).

To reset preferences, remove the runtime preference file:

```bash
rm -f "$HERMES_HOME/data/sharpinput/user-preferences.json"
```

If `$HERMES_HOME` is unset, check your active Hermes profile data directory.
