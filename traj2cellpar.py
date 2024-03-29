def traj2cellpar(traj, image=-1, rounding=8):
  # Small function to write out the cell data from an ASE trajectory file.
  # traj : (str)  Filename of trajectory
  # image : (int) Image to print cell data from
  # rounding : (int) Number of decimal places to round to

  import numpy as np
  from ase import Atoms
  from ase.io import Trajectory

  imprt = Trajectory(traj)
  atoms=imprt[image]
  rounding = rounding

  print('Writing cell data to file CellData.txt')
  with open('CellData.txt', 'w') as cd:

      cd.write('Rounding to ' + str(rounding) + ' decimal places' + '\n')
      cd.write('\n')
      cd.write('Atoms Object'+ '\n')
      cd.write(str(atoms)+ '\n')
      cd.write('\n')
      cd.write('Cell Vectors'+ '\n')
      cd.write(str(np.round(atoms.cell, rounding)) + '\n')
      cd.write('\n')
      cd.write('Cell Parameters' + '\n')
      cd.write(str(atoms.cell.cellpar()) + '\n')
      cd.write('\n')
      cd.write('Scaled Atomic Positions' + '\n')
      cd.write(str(np.round(atoms.get_scaled_positions(), rounding)) + '\n')
      cd.write('\n')
      cd.write('Scaled Atomic Positions Labeled by Element' + '\n')
      for atom in range(len(atoms.symbols)):
        cd.write(atoms.symbols[atom])
        cd.write(str(np.round(atoms.get_scaled_positions()[atom], rounding)) + '\n')
      
