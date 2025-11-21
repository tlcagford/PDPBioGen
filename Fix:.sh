# Debian/Ubuntu
sudo apt-get install graphviz

# In CI (GitHub Actions)
- name: Install graphviz
  run: sudo apt-get update && sudo apt-get install -y graphviz
git add pdp_biogen.py
git commit -m "Add main script"
git push
