# 🛠️ PotatoAI Configuration Guide

This document explains how to use and customize PotatoAI using dotfiles. These configuration files give you full control over the behavior, appearance, and memory of your local AI instance.

---

## 📄 Dotfiles Overview

| File                    | Location                                  | Purpose                                                   |
| ----------------------- | ----------------------------------------- | --------------------------------------------------------- |
| `.env`                  | Project root                              | Local development overrides, ports, API keys (if needed)  |
| `.potatoai.config.toml` | Project root or `~/.potatoai/config.toml` | User-facing preferences (theme, memory, privacy, compute) |
| `.potatoai.dev.toml`    | Project root                              | Developer/debug configuration for advanced use            |

---

## 🧾 `.potatoai.config.toml`

This file controls user-level preferences and persistent app behavior.

### ✅ Example:

```toml
[ui]
theme = "dark"
font_size = "medium"
voice_enabled = true

[privacy]
default = "private"
auto_prompt_share = true

[memory]
importance_threshold = 0.75
max_cache_mb = 512
use_dims = true
```

### 🔍 Config Keys

#### `[ui]`

| Key             | Type   | Description                                        |
| --------------- | ------ | -------------------------------------------------- |
| `theme`         | string | UI theme name (e.g. `dark`, `light`, `classic-xp`) |
| `font_size`     | string | UI text size: `small`, `medium`, `large`           |
| `voice_enabled` | bool   | Enable voice input/output if supported             |

#### `[privacy]`

| Key                 | Type   | Description                                                |
| ------------------- | ------ | ---------------------------------------------------------- |
| `default`           | string | `private` or `shared` (default per chat)                   |
| `auto_prompt_share` | bool   | Whether to auto-prompt user to share memory at end of chat |

#### `[memory]`

| Key                    | Type  | Description                                         |
| ---------------------- | ----- | --------------------------------------------------- |
| `importance_threshold` | float | Min score to store memory in DIMS hierarchy         |
| `max_cache_mb`         | int   | Max memory used for cache (in MB)                   |
| `use_dims`             | bool  | Whether to use the dynamic importance memory system |

---

## 🛠️ `.potatoai.dev.toml`

This file is used for debugging or developer overrides.

### ✅ Example:

```toml
[dev]
log_level = "debug"
auto_reload = true
debug_memory_dump = false
```

| Key                 | Type   | Description                                              |
| ------------------- | ------ | -------------------------------------------------------- |
| `log_level`         | string | `debug`, `info`, `warn`, `error`                         |
| `auto_reload`       | bool   | Auto-refresh local UI during dev                         |
| `debug_memory_dump` | bool   | Dump memory layer to file every cycle (for testing only) |

---

## 🧭 Where to Place Config Files

| Use Case       | Recommended Location                                      |
| -------------- | --------------------------------------------------------- |
| Development    | Place dotfiles in the project root                        |
| End-user setup | Copy `.potatoai.config.toml` to `~/.potatoai/config.toml` |

On launch, PotatoAI will look for the following in order:

1. `~/.potatoai/config.toml`
2. Project root `.potatoai.config.toml`
3. Default baked-in config values

---

## 🧪 Tips

* Never commit real `.env` or `.potatoai.config.toml` files unless sanitized.
* Provide a `*.example.toml` template in the repo.
* Document config keys inside the UI for non-technical users.
* You can live-reload settings on UI load (planned feature).

---

For more help, see `ARCHITECTURE.md` or `README.md`.
