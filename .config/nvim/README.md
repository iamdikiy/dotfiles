# Nvim setup 
## Install Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Add to path (already added in .zshrc file)
```bash 
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
```

## Install gcc, g++ and make
```bash
sudo apt update
sudo apt install build-essential
```
## Install Neovim
```bash
brew install neovim
```

## Install Ripgrep
```bash
brew install ripgrep
```
## Install Node
```bash
brew install node
```
