# This version only works on Amy's laptop! Go to the updated version for a program that works on all computers

# Before running the program, make sure that params_filepath and destination_filepath are accurate. 
# They must be the complete filepath. 
# For example: 
#     params_filepath = r'C:\Users\ahuan\Desktop\AutoFlattPack\FLattPackSampleParams - Test.csv'
#     destination_filepath = r'C:\Users\ahuan\Desktop\FLatt Samples'
# Note that destination_filepath is a folder, but does not include the backslash (\) at the end

import pyautogui as pg
import pandas as pd

"""
These two paths should be changed for each user
"""
# read csv file
params_filepath = r'C:\Users\ahuan\Desktop\AutoFlattPack\FLattPackSampleParams.csv'
destination_filepath = r'C:\Users\ahuan\Desktop\FLatt Samples'

df = pd.read_csv(params_filepath)
print(df)

def generate_name(row): # i.e., g_0p5ys_0p3vf 
    vf_min = 0.1
    # CELL TYPE
    if str(row['Cell Type']).strip().lower() == 'gyroid':
        cell_type = 'g'
    elif str(row['Cell Type']).strip().lower() == 'diamond':
        cell_type = 'd'
    elif str(row['Cell Type']).strip().lower() == 'primitive':
        vf_min = 0.24
        cell_type = 'p'
    else: 
        pg.alert(f'Cell Type for sample {row.name + 1} is not recognized')
        quit()

    # Y_SHIFT
    if 0 <= row['y Shift'] <= 1:
        yshift = f'{round(row['y Shift'], 1):.1f}'.replace('.', 'p')
    else:
        pg.alert(f'y-shift for sample {row.name + 1} must be between 0 and 1')
        quit()

    # VOLUME FRACTION
    if vf_min <= row['Volume Fraction'] <= 0.85:
        vf = f'{round(row['Volume Fraction'], 2):.2f}'.replace('.', 'p')
    else:
        pg.alert(f'volume fraction for sample {row.name + 1} must be between {vf_min} and 0.85')
        quit()

    # CREATE NAME
    name = f'{cell_type}_{yshift}ys_{vf}vf'
    return name

df['Name'] = df.apply(generate_name, axis=1)
print(df)
df.to_csv(params_filepath, index=False)

# start pyautogui-ing here
pg.click(1478, 485)
pg.sleep(2)

# FLATTPACK 
for index, row in df.iterrows(): # for each row (each sample)    
    print(f'Starting sample {row.name + 1}: {row['Name']}')
    # on Geometry page, click "Next" button (1857, 1265)  or 4 tabs
    # pg.press('tab', interval=1, presses=4)
    pg.click(1857, 1265)
    # wait ~3 seconds
    pg.sleep(3)

    # on Dimensions page, double-click the box for "x:" (1806, 824) or 1 tab 
    # change to (50, 60, 50) and (5, 6, 5). Do this by typing the number and Tab in between
    pg.write('\t50\t60\t50\t', interval=0.2)
    pg.write('5\t6\t5', interval=0.2)
    # click "Next" button (1866, 1185) or 3 tabs
    pg.click(1866, 1185)
    # wait ~3 seconds
    pg.sleep(3)

    # on Cell Type page, double-click y-shift for cell translation box (1660, 452) or 3 tabs
    pg.doubleClick(1660, 452)
    # change to value given by csv
    pg.write(str(round(row['y Shift'], 1)), interval=0.2)
    # click gyroid (1030, 800), diamond (1030, 1090), or primitive (1300, 1090) based on cell_type given by csv
    if str(row['Cell Type']).strip().lower() == 'gyroid':
        pg.click(1030, 800, _pause=True)
    elif str(row['Cell Type']).strip().lower() == 'diamond':
        pg.click(1030, 1090,_pause=True)
    elif str(row['Cell Type']).strip().lower() == 'primitive':
        pg.click(1300, 1090, _pause=True)
    else:
        pg.alert(f'Cell Type for sample {row.name + 1} is not recognized')
        exit()

    # click "Next" button (1870, 1443)
    pg.click(1870, 1443)
    # wait ~3 seconds
    pg.sleep(4)

    # on Volume Fraction page, double-click the text box for volume fraction (1161, 752)
    pg.doubleClick(1161, 752)
    # change to value given by csv
    pg.write(str(round(row['Volume Fraction'], 2)), interval=0.2)
    # click "Next" button (1879, 1295)
    pg.click(1879, 1295)
    # wait 7 seconds or until confirmation page shows up?
    pg.sleep(7)

    # on Volume Fraction preview page, click "Next" button (1689, 964)
    pg.click(1689, 964)
    pg.sleep(2)

    # on Lattice Skin page, click "Side Skin" option (952, 892)
    pg.click(952, 892)
    # click "y" option (1070, 955)
    pg.click(1070, 955)
    # double-click the box for "skin thickness" (1285, 1025)
    pg.doubleClick(1285, 1025)
    # type 5 
    pg.write('5')
    # click "Next" button (1864, 1206)
    pg.click(1864, 1206)
    # wait ~4 seconds
    pg.sleep(4)

    # on Output files page, click "Save as" button (1038, 1173)
    pg.click(1038, 1173)
    pg.sleep(2)

    # type in name we determined earlier
    sample_filepath = destination_filepath + '\\' + row['Name'] + '.stl'
    pg.write(sample_filepath)
    # click Save button (2014, 1501)
    pg.click(2014, 1501)
    pg.sleep(3)

    # click "Write files" button (1826, 1173)
    pg.click(1826, 1173)
    # wait ~3 seconds
    pg.sleep(3)

    # on triangle mesh reduction page, click "Next" button (1862, 1112)
    pg.click(1862, 1112)
    # wait 18 seconds or until lattice preview page shows
    pg.sleep(20)

    # on Lattice Preview page, click "Next" button (1691, 957)
    pg.click(1691, 957)
    # wait ~5 seconds
    pg.sleep(5)

    # on file creation complete page, click "Create another structure" button (1625, 1004)
    pg.click(1625, 1004)
    # wait ~3 seconds
    pg.sleep(3)




