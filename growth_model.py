import numpy
from matplotlib import pyplot

def cells_conc_in_time(A, growth_rate_max, lag_phase, time):
    return A * numpy.exp(-numpy.exp((growth_rate_max * numpy.exp(1) * (lag_phase-time))/A + 1))

def substrate_conc_in_time(A, growth_rate_max, lag_phase, time, t, index, Y):
    X1 = cells_conc_in_time(A, growth_rate_max, lag_phase, time) * 0.38
    X2 = cells_conc_in_time(A, growth_rate_max, lag_phase, t[index[0]+1]) * 0.38
    return ((X2-X1)/Y)

def check_run_out_substrate(substrate_concentrations, cells_concentrations):
    substrate_run_out_index = find_substrate_run_out_index(substrate_concentrations)
    print(substrate_run_out_index)
    if substrate_run_out_index:
        for index, cell_concentration in numpy.ndenumerate(cells_concentrations):
            if index[0] == substrate_run_out_index:
                max_concentration = cells_concentrations[index[0]-1]
                cells_concentrations[index[0]] = max_concentration
            elif index[0] > substrate_run_out_index:
                cells_concentrations[index[0]] = max_concentration
    return cells_concentrations
            
def find_substrate_run_out_index(substrate_concentrations):
    try:
        index = substrate_concentrations.index(0)
        print(index)
    except ValueError:
        return None
    return index 

t = numpy.linspace(0, 15) # x-axis
t0 = t[0]
induction = 2.5 #in hours
stop_induction = 6 #in hours
Y = 0.35 
y2=[]  # for substrate
A = 6 # maximal optical density
growth_rate_max = 0.6 #k-1
lag_phase = 1 # in hours
X0 = cells_conc_in_time(A, growth_rate_max, lag_phase, 0)
S = 5 # initial substrate concentration g/l
y2.append(S)
y1 = []  # for bacteria

# second cells and substrate
S4 = 5
Y3 = 0.35
y4=[]  # for substrate
A3 = 6 # maximal optical density
growth_rate_max3 = 0.6
lag_phase3 = 5 # in hours
X0 = cells_conc_in_time(A3, growth_rate_max3, lag_phase3, 0)
y3 = []  # for bacteria
y4.append(S4)

# Calculate the growth curve for bacteria
for time in t:
    if induction != None:
        if time < induction:
            y1.append(cells_conc_in_time(A, growth_rate_max, lag_phase, time))
            y3.append(cells_conc_in_time(A3, growth_rate_max3, lag_phase3 + induction, time))
        if stop_induction != None:
            growth_curve_shift = cells_conc_in_time(A, growth_rate_max, lag_phase, stop_induction) - cells_conc_in_time(A, growth_rate_max, lag_phase, induction)
            if induction <= time < stop_induction:
                y1.append(cells_conc_in_time(A, growth_rate_max, lag_phase, induction)) # after induction the values are the same
                if len(y3) < len(t):
                    y3.append(cells_conc_in_time(A3, growth_rate_max3, lag_phase3 + induction, time))
            elif time >= stop_induction:
                y1.append(cells_conc_in_time(A, growth_rate_max, lag_phase, time) - growth_curve_shift)
                y3.append(cells_conc_in_time(A3, growth_rate_max3, lag_phase3 + induction, time))
        else:
            if time > induction:
                y1.append(cells_conc_in_time(A, growth_rate_max, lag_phase, induction)) # after induction the values are the same
                if len(y3) < len(t):
                    y3.append(cells_conc_in_time(A3, growth_rate_max3, lag_phase3 + induction, time))
    else:
        y1.append(cells_conc_in_time(A, growth_rate_max, lag_phase, time))

# calculate the curve for substrate consumption
for index, time in numpy.ndenumerate(t):
    if S > 0:
        if len(y2) < len(t):
            if induction != None:
                if time < induction:
                    try:
                        dS = substrate_conc_in_time(A, growth_rate_max, lag_phase, time, t, index, Y)
                        S = S - dS
                        if S > 0:
                            y2.append(S)
                        else:
                            y2.append(0)
                    except IndexError:
                        break
                if stop_induction != None:
                    if induction <= time < stop_induction:
                        S = S - dS
                        if S > 0:
                            y2.append(S)
                        else:
                            y2.append(0)
                    elif time >= stop_induction:
                        try:
                            dS = substrate_conc_in_time(A, growth_rate_max, lag_phase, time, t, index, Y)
                            S = S - dS
                            if S > 0:
                                y2.append(S)
                            else:
                                y2.append(0)
                        except IndexError:
                            break 
                else:
                    S = S - dS
                    if S > 0:
                        y2.append(S)
                    else:
                        y2.append(0)
            else:
                try:
                    dS = substrate_conc_in_time(A, growth_rate_max, lag_phase, time, t, index, Y)
                    S = S - dS
                    if S > 0:
                        y2.append(S)
                    else:
                        y2.append(0)
                except IndexError:
                    break
    else:
        if len(y2) < len(t):
            y2.append(0)
            
        else:
            break

# second substrate
#for index, time in numpy.ndenumerate(t):
 #   if S4 > 0:
  #      if len(y4) < len(t):
   #             try: 
    #                dS4 = substrate_conc_in_time(A3, growth_rate_max3, (lag_phase + induction), time, t, index, Y3)
     #               S4 = S4 - dS4
      #              y3_const = y3[index[0]+1]
       #             if S4 > 0:
        #                y4.append(S4)
         #           else:
          #              y4.append(0)
           #     except IndexError:
            #        break
  #  else:
   #     if len(y4) < len(t):
    #        y3[index[0]+1] = y3_const
     #       y4.append(0)
      #  else:
       #     break

# Recalculating the growth curve based on the depletion of the substrate
y1 = check_run_out_substrate(y2, y1)


#Graphical representation
fig, ax1 = pyplot.subplots()

# Settings for the graphs
color = 'tab:red'
color2 = 'tab:green'
ax1.set_xlabel('time (h)')
ax1.set_ylabel('OD', color=color)
ax1.set_ylim(top=6.4)  # adjust the top leaving bottom unchanged
ax1.plot(t, y1, color=color)
#ax1.plot(t, y3, color=color2)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
color4 = 'tab:purple'
ax2.set_ylabel('[S]', color=color)  # we already handled the x-label with ax1
ax2.plot(t, y2, color=color)
#ax2.plot(t, y4, color=color4)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
pyplot.show()