# mewesh
bringing collaborative data analytic inspection one-step further

Setup:

1) npm install -g ttycast tty2js (only install in the main server)

2) npm install -g ttyrec (install in each client machines)

3) pip install flask (only install in the main server)

Usage of parts:

tty2js -s WxH /path/to/file.tty /path/to/output/data.js


How to shell collab:

To be later improved in a unified means. For now, to re-use existing usable parts:

1) each client has granted a common ssh access to main server

2) Client must open two terminals. On first terminal,

mkfifo /tmp/fifo1

ttyplay -n /tmp/fifo1 | ssh username@svr PORT=12345 ttycast

On second terminal,

ttyrec /tmp/fifo1

3) Access http://svr:12345 to view the wemesh collaborative shell

