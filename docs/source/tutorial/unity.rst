Using the Package with Unity Game Engine
=========================================
This is a sort of experiment I did while developing this package, which I
focused in making a simple working example in Unity and make it work with a
build. I executed all necessary functions to check which python interpreter and
where the module is being loaded. And they returned that they were loaded from
the game build path, which it's important when you ship your game so you don't
need to ask for the user to install python together with your game.

However I did not try to execute it in a machine that doesn't have Python, so
if you want to use it in production that test must be made.

So in this example we will learn how to:

* Configure a Unity project
* Use Python using Unity
* Learn how to install a package using pip and use inside Unity
* Code C# using python modules and `Python.Net <http://pythonnet.github.io/>`_

.. note::

    You can't use yaml if you use Unity because
    `PyYaml <https://pyyaml.org/>`_ raises errors, so you have to use json raws.

Setting a Unity Project
########################
For this we are using Unity 2019.02.0f1 but it would probably work with any
Unity that is able to execute .net framework 4.x.

So, create a new Unity project as normal, for learning purposes let's name the
project *core_data*. Then set the API compatibility to framework 4.x you can
read how to in this link:
https://docs.microsoft.com/en-us/visualstudio/cross-platform/unity-scripting-upgrade?view=vs-2019#enabling-the-net-4x-scripting-runtime-in-unity
which will inform a couple more things about the difference between the versions.

.. note::

    I tested with netstandard 2.0 however it did not work because dynamic fields needs a microsoft
    dll which is not referenced.

Installing Python.net
######################
The easiest way that I found how to set everything up, is first of all, install
python 3.7 64 bits, or 32 depending on the final build you desire and then
install virtualenv with this command:

.. code:: console

    pip install virtualenv

If you fell with a parachute here. The command above installs packages from the
Python Library Index (PyPI) and virtualenv let you create a python interpreter
that is not linked to the one installed into the system. So, pretty much we
will create a virtualenv, *cd* to the root of your project and run this code:

.. code:: console

    virtualenv Packages/python_net

Wait for the command to execute. Then activate the virtualenv with:

.. code:: console

    ./Packages/python_net/Scripts/activate

Then simply install Python.Net with:

.. code:: console

    pip install pythonnet

Lastly create a file inside *core_data/Packages/python_net* named
*package.json* with this contents:

.. code:: json

    {
      "name": "com.company.package_name",
      "version": "0.0.1",
      "displayName": "Example",
      "description": "Any Description"
    }

Unity just needs those fields, the contents can be almost anything, but version
and name fields needs to follow the pattern above.

Installing PandaCoreData
#########################
The Python interpreter needs to load the module, but Unity compacts everything,
but it doesn't compact anything inside the folder *Assets/StreamingAssets* so
create that folder if it doesn't exist, then `cd` to that folder. Then execute
this command:

.. code:: console

    pip install --ignore-installed git+https://github.com/Cerberus1746/PandaCoreData.git --install-option="--prefix=absolute_folder"

And replace *absolute_folder* with the absolute folder to your streaming assets
folder. Wait the
command to execute and you are done.

Follow this tutorial :ref:`Getting Started` and create the file structure with
the command in there but inside *Assets/StreamingAssets* folder. Probably you
would need to use the quickstart command like this:

.. code:: console

    ./Script/panda_core_data_commands -o . -re json

Considering that you are executing that command inside the streaming folder, it
will create a *mods* folder using json raws. Again, yaml won't work. Then
follow :ref:`Getting Started` as normal, of course, you won't need to install
again the package. But delete the *main.py* file, you won't be needing it
because we use a:

C# Main File
##############
And here's the final working example, the results will be the same as the
:ref:`Getting Started` but this file will need to be inside the *Assets*
folder, outside *StreamingAssets* folder. For convenience sake, let's call it
*main.cs*

.. code:: cpp

    using UnityEngine;
    using Python.Runtime;
    using System.IO;
    using System.Collections.Generic;

    namespace PythonTest {
        public class PythonTest : MonoBehaviour {
            void Start() {
                using(Py.GIL()) {
                    // Let's import sys
                    dynamic py_sys = Py.Import("sys");

                    // We need this so we add the python modules from the
                    // streaming assets. Otherwise the module won't load.
                    string site_pkg = "Lib\\site-packages";
                    py_sys.path.insert(0, Path.Combine(Application.streamingAssetsPath, site_pkg));

                    // Now we can import all necesary modules for the example.
                    dynamic py_panda_core_data = Py.Import("panda_core_data");
                    dynamic py_dataclasses = Py.Import("dataclasses");
                    dynamic py_builtin = Py.Import("builtins");

                    // Now we get the mods folder from streaming assets
                    string mods_folder = Path.Combine(Application.streamingAssetsPath, "mods");

                    // And now we can use the data_core just like we do in python.
                    // List type is automatically converted to python equivalent with Pyton.Net
                    py_panda_core_data.data_core(mods_folder,
                                                 templates_folder: false,
                                                 excluded_extensions: new List<string>(){"meta"});

                    // Now we iterate along all model instances
                    dynamic item_model = py_panda_core_data.data_core.get_model_type("items");
                    foreach(dynamic instance in item_model) {
                        // And we can iterate along all fields
                        foreach(dynamic field in py_dataclasses.fields(instance)) {
                            // And show the field name and field value
                            Debug.Log($"{field.name}: {py_builtin.getattr(instance, field.name)}");
                        }
                    }
                }
            }
        }
    }

Then attatch this script to the camera or any object that you prefer. Then all
you need to do is hit play or build the project if you want.
