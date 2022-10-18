### Require
  - fast deloy in Unbuntu 20
  - Python3
  - Pip

### RUN
```bash
python3 -u server.py > backgroundlog &
ps ax | grep server.py
```
- ``http://localhost:8000?url={URL}&ref=[referer]``

### Clone Project
```bash
git clone https://github.com/nghyane/BypassCloudfare.git
```
### Install

```bash
cd BypassCloudfare
python3 -m pip install -r requirements.txt
```

### pip install
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### For dev
- auto create requirements
```bash 
python3 -m pip install pipreqs
pipreqs .
```
