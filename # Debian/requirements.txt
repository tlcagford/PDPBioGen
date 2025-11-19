# Debian/Ubuntu
sudo apt-get install graphviz

# In CI (GitHub Actions)
- name: Install graphviz
  run: sudo apt-get update && sudo apt-get install -y graphviz
