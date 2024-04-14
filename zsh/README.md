# zsh

## Install
### Step 1: Install Zsh

```bash
sudo apt install zsh -y
zsh --version
```

### Step 2: Set zsh as default shell

```bash
sudo chsh -s /usr/bin/zsh $USER
echo $SHELL
```

### Step 3: Install [Oh-My-Zsh](https://github.com/ohmyzsh/ohmyzsh)
```bash
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh
```

### Step 4: Create symlink for existing .zshrc file
```bash
ln -s .../zsh/.zshrc
```

## Plugins need to install

### [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

### Theme
Currenly using sobole theme - [sobole-zsh-theme](https://github.com/sobolevn/sobole-zsh-theme)
```bash
git clone https://github.com/sobolevn/sobole-zsh-theme.git
ln -s $PWD/sobole-zsh-theme/sobole.zsh-theme ~/.oh-my-zsh/custom/themes/sobole.zsh-theme
