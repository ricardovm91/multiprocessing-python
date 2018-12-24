# Multiprocessing-Python

An example of multiprocessing with python to speed up CPU intensive tasks using Digital Ocean Droplets.

## Intro

This is a short but complete tutorial on how to run multiprocessing jobs using Python. You can do it in your own computer or follow the tutorial to do it in Digital Ocean's droplets. To know more about the kind of problems you might solve with this, visit my [Medium blog post](https://medium.com/synapsis-rs/multiprocessing-with-python-in-digital-ocean-droplets-9bf26cc176e9). On the post there are also nice links if you want to read about the concepts of multiprocessing and multithreading.

## Python Code

The code provided works like this:

* Load a big plain text file.
* Divide it by the number of agents that will process it.
* Depending on which agent is processing, it will take its division and divide it for every available core.
* It launches a process per core. Logs when the job is complete.

For now, the Digital Ocean Deployment is manual. I hope in the future to update this repo with the API code to do it automatically.

## Digital Ocean Deployment

[Digital Ocean](https://digitalocean.com) is pretty straightforward in terms of use. To deploy this code follow the next instructions. Please have in mind this is intended for short executions. This is not production level configuration.

* Create an account and log in.
* Create a Droplet. I used Ubuntu 18.04.
* Connect to your Droplet using SSH. In my Mac I used Termius. For Windows you might want to use something like MobaXterm. In Linux you can just ssh from the terminal ([here's how to do it](https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/openssh/)).
* To set up the running environment very quickly (the Droplet will already have Python installed) run:

```bash
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip
```

* Install your required libraries. For the example is just:

```bash
pip3 install pandas
```

* Connect to your machine through SFTP using [Filezilla](https://filezilla-project.org/) or similar, and upload your code. If you log in with your root account, there's no setup to be made.
* Since your code will probably take time, create a screen by running `tmux new -s SCREEN-NAME`.
* `cd` to your code's directory and run `python3 multiprocessing.py`.
* You now have your code running on all of the server's cores.
* To check the progress, if you're logging it or something, reconnect through ssh and run `tmux attach -t SCREEN-NAME`.
* After finishing the job, destroy the Droplet so you don't get overcharged.

That's all!
