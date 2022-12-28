#Steps to generate a gif file representing an arbitrary f function of time and position,
#plotted over the surface of a sphere:
  #1. create a folder named 'tmp' in your work directory
  #2. define f and feed it to genframes, defined below. This will take a while, and
  #   will eventually generate save your frames into the tmp folder.
  #3. go to your preferred gif maker (e.g., ezgif.com/maker), and generate your gif
  #   file using the frames generated with genframe.
  #4. you may now delete the tmp folder.
#You might want to read the warning at the end of line 68 here




#Libraries used
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize as Norm

#Sample f function (see instructions above)
def f(theta,phi,t,
      points=250,tpoints=100):
    return np.sin(2*np.pi*t/tpoints)*np.sin(2*phi)*np.cos(2*theta)


#Main function. Everything is encapsulated here, so you can import this function to your code
def genframes(f=f, #your function to plot
              points=250,tpoints=100, #spatial and temporal resolution
              deform=True,rscale=.2, #whether to represent f as a distance from the origin or not.
                                     #If deform=True, then rscale=dr/1 is the scale at which
                                     #the deviation dr from the unit sphere is represented
              cmap='jet',s=1, #the colormap and point size used by pyplot
              rotate=True): #whether you'd function plotted on a rotating sphere or not

    #Generation of domain set
    theta=np.linspace(0,2*np.pi,points,endpoint=False) #azimuthal angle
    phi=np.linspace(0,np.pi,points,endpoint=False) #zenithal angle
    t=np.arange(0,tpoints) #time
    Theta,Phi,T=np.meshgrid(theta,phi,t)
    #Generation of the image set
    dr=f(Theta,Phi,T,points,tpoints) #deviation from a perfect sphere
    r=np.ones(dr.shape)
    R=r+dr*rscale #resultating deviated sphere

    #Transformation into cartesian coordinates
    if deform: #if you'd like to represent f as a distance from the origin, and a colormap
        X=R*np.sin(Phi)*np.cos(Theta)
        Y=R*np.sin(Phi)*np.sin(Theta)
        Z=R*np.cos(Phi)
    else: #if you'd like to represent f as a spherical colormap only
        X=r*np.sin(Phi)*np.cos(Theta)
        Y=r*np.sin(Phi)*np.sin(Theta)
        Z=r*np.cos(Phi)

    #Plotting
    if rotate: #if you'd like a rotating plot
        azimuth=360*t/tpoints #set of azimuthal angles for pyplot's camera, this will simulate a
                              #rotating sphere onto which your function is plotted. For reference, see
                              #https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html
    else: #if you'd like a static plot, where time only incides via your function
        azimuth=np.ones(t.shape)*45 #pyplot's default value
    for timestep in t:
        fig=plt.figure()
        ax=fig.add_subplot(projection="3d")
        ax.scatter(X[:,:,timestep].flatten(),Y[:,:,timestep].flatten(),Z[:,:,timestep].flatten(),
                        c=R[:,:,timestep].flatten(),
                        s=s,cmap=cmap,norm=Norm(vmin=R.min(),vmax=R.max()))
        ax.set_box_aspect((np.ptp(X[:,:,timestep].flatten()),
                           np.ptp(Y[:,:,timestep].flatten()),
                           np.ptp(Z[:,:,timestep].flatten()))) #*This line might not work on some
                                                               #interpreters or in some versions
                                                               #of pyplot, be careful!
        ax.set_axis_off()
        ax.view_init(elev=45, azim=azimuth[timestep])
        fig.savefig('tmp/tmp{}.png'.format(str(timestep).zfill(len(str(t[-1])))))
