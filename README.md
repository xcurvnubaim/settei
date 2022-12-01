# settei package

```
in your workspace folder create and open ~/src/
```

# build dependencies

settei_interfaces

```
git clone https://github.com/xcurvnubaim/settei_interfaces.git
```

clone repo

```
git clone https://github.com/xcurvnubaim/settei.git
```

in your workspace open terminal and type

```
colcon build --packages-select settei2
``` 

run package

```
. install/setup.bash
```

```
ros2 run settei settei
```

```
ros2 run settei service
```

in another terminal

```
. install/setup.bash
```

```
ros2 run settei client <package_name> <robot> <branch>
```

### output in service terminal should be
```
[filename_array] ; [data_array]
```