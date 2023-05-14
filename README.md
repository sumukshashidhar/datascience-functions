# datascience-functions
A repository of functions helpful for datascience workflows. Mostly in Python

# Purpose

The purpose of this repository is to provide a collection of functions that are useful for datascience workflows. These functions are primarily written in Python and aim to be general enough to be applicable in various scenarios. The repository will be periodically updated with new functions as the author continues their datascience work.

## Additional

I will also try to refine and structure this repository to make the finetuing of a model easier.


## File Format

The repository includes a `meta.json` file that contains essential information about the functions. This JSON file provides details about each function except for its implementation. The structure of each function entry in the meta.json file is as follows:
```json
{
    "name": "function_name",
    "description": "A description of the function",
    "input" : "The input required by the function",
    "output" : "The output returned by the function",
    "dependencies" : "The libraries on which the function depends",
    "language" : "The programming language used for the function",
    "path" : "The path to the function's file"
}
```

## Other

If a file in the src directory contains the `# processed` comment, it means that it has been added to the metadata. Else, it remains to be added.