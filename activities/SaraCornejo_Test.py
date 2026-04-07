#!/usr/bin/env python3
import os
import grass.script as gs

def run_lake(scanned_elev, env, **kwargs):
    gs.run_command('r.lake', elevation=scanned_elev, lake='output_lake',
                   water_level=110, env=env)
    gs.write_command('r.colors', map='output_lake', rules='-',
                     stdin='0 0:0:255\n5 0:0:100', env=env)
    gs.run_command('v.to.rast', input='streets_wake@PERMANENT',
                   output='streets_rast', use='val', value=1, env=env)
    gs.write_command('r.colors', map='streets_rast', rules='-',
                     stdin='1 255:255:0', env=env)
    gs.run_command('v.to.rast', input='streams@PERMANENT',
                   output='streams_rast', use='val', value=1, env=env)
    gs.write_command('r.colors', map='streams_rast', rules='-',
                     stdin='1 0:191:255', env=env)

def main():
    env = os.environ.copy()
    env["GRASS_OVERWRITE"] = "1"
    run_lake(scanned_elev="elevation", env=env)

if __name__ == "__main__":
    main()
    
