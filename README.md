# UWU 👉🏽👈🏽

This language main intent is to be familiar to the developers who use it. Almost like it is ***simping*** for the developer.

Language design is still a work in progress please update as you see fit.

# Language Specification /emo

**Variable declaration**

```
// type is implied
var x = 1;
// type is defined
var x:int = 1;
// notype

var name = 'Rumone';
var name: string = 'Rumone';

var cost = 12.44;
var cost:decimal = 12.44;
```

**Assignment**

```
name = 'Rumone';
x = 12;
cost = 12.44;
```

**Function Definition**

```
func name () -> {
	
}
```

**Function Parameters**

```
func name (first:string, last:string):string -> {
}
```

**Return**

```
func name ():string -> {
	return "Rumone";
}

// The return type is a string
```

**Conditionals**

```
if name is "Rumone" {
	return true;
} else {
	return false;
}
```

**Arithmetic**

```
func operations (a:int, b:int, oper:string):int -> {
	var output:int;
	
	if oper is 'add' {
		output = a + b;
	}
	...

	return output;
}
```

**Loops**

```
for val in vals {
	print(val);
}

// vals is a list how would you implement this

while true {
	print("FOO BAR");
}
```

# Contributions 🛠️

To work on the project the following resources may be helpful.

- [PLY Documentation](https://ply.readthedocs.io/en/latest/ply.html)
- [PLY YouTube Tutorial](https://www.youtube.com/watch?v=Hh49BXmHxX8)

The project currently has no external dependencies. PLY is installed by adding the files to the project directory. Therefore the only requirement is python 3.