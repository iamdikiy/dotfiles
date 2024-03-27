# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"
# Theme is set via `zplug`, see `config/zplug.txt`.
ZSH_THEME="sobole"
SOBOLE_THEME_MODE=dark
# Uncomment the following line to use case-sensitive completion.
CASE_SENSITIVE='false'

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
HYPHEN_INSENSITIVE='false'

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="false"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS='yyyy-mm-dd'

# Commands starting from " " (whitespace) won't be saved in history:
HIST_IGNORE_SPACE='true'

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.

plugins=(
  gitfast
  safe-paste
  zsh-syntax-highlighting
)

# Sourcing the Oh-My-ZSH source:

source "$ZSH/oh-my-zsh.sh"

# This PATH needs to be set before all other modifications:
export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/sbin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"


# === Plugin management ===
#
if [ "$CODESPACES" = true ]; then
  ZPLUG_HOME="$HOME/.zplug"
fi
