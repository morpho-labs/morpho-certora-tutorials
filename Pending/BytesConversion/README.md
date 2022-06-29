## How to reproduce

`make` does not go through because the function is expecting a bytes4 but the `f.selector` gives back a uint32 in CVL. The problem is that there is no way to cast it to the expected bytes4 type.
