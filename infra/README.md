# infra
## About
Deployment scirpts for [ISUCON9](http://isucon.net/archives/53231706.html).

## Requirements
- Python >= 2.7, < 3

## Setup
```
$ pip install 'fabric<2' cuisine
```

## Initial Deploy
**Default sudo password is `yharima`.**
```
$ fab init -H '<user>@<host>'
```

### _setup_users
Creates following users using public keys of GitHub.
- [yuta1024](https://github.com/yuta1024)
- [tyabuki](https://github.com/tyabuki)
- [nhirokinet](https://github.com/nhirokinet)
