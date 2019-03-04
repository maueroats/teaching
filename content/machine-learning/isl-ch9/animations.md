---
title: "Animations"
date: 2019-03-02T22:17:46-06:00
weight: 20
draft: false
#type: slide
#theme: white
---

Matplotlib animations using the Seaborn library to draw. 

The back end needs to be told you are using an IPython notebook. There
is a `%matplotlib` [magic
command](https://ipython.readthedocs.io/en/stable/interactive/plotting.html)
that lets you choose how to display the results of plotting. For this
notebook, the best choice is `notebook`, which lets you interact with
the output when applicable. Another reasonable choice is `inline`,
which puts the pictures below the code cells that produce them.

## Notebook setup code

Put the following code in your initialization at the start of the
notebook.

	import matplotlib.pyplot as plt
	import matplotlib.animation as animation
	from matplotlib import rc
	rc('animation', html='html5')
	%matplotlib notebook
	

## Basic plots

When you are making a plot, usually you start out by getting a figure
and axis object using the `subplots()` command. If you want more than
one set of axes in your figure, this is the place to do that (look it
up). 

	fig, ax = plt.subplots()
	ax.set_xlim(-10,10)
	ax.set_ylim(-10,10)
	
## Draw handler 

The draw handler should take in a model and some other information,
usually including axes to draw on, and output a list of axes that have been
drawn on. Since we only have one set of axes, we output (axes,) so it
is a list (well, really a tuple).

Here is an example function that draws more and more blue dots on the screen.

	def one_frame(n,xs,ys,ax):
		ax = sns.scatterplot(xs[:n], ys[:n],color='blue',ax=ax)
		return (ax,)

## Animations

Run the `animation.FuncAnimation` command (really "build the
object"). Arguments:

* `fig`: The figure is the first argument. Required.
* `func=draw_handler`: The function named `draw_handler` (you can choose the
  name) is used to draw one frame of the animation. Return the axes
  you draw. 
* `frames=20`: How many frames to make. This number is passed as the
  value of the number model to your draw handler. (Can also pass a
  list of models, which are then used one by one.) 
* `fargs=(arg1,arg2,ax)`: Optional. Additional arguments your function is
  called with. In this case, your function would get called like this:
  `draw_handler(5,arg1,arg2,ax)`. I put my axes in the list of arguments.

