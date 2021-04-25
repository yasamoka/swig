import pathlib

from cpp17_std_filesystem import *

def check(flag):
    if not flag:
        raise RuntimeError("Check failed")

p = "foo"

# Test the output typemap. The wrapped C++ functions
# makePath is expected to return a std::filesystem::path object
# (see li_std_filesystem.i). The output typemap should be in place to
# convert this std::filesystem::path object into a pathlib.Path object.
path = makePath(p)
check(isinstance(path, pathlib.Path))
check(str(path) == p)

#
# Each of these should return a reference to a wrapped
# std::filesystem::path object.
#
pathPtr = makePathPtr(p)
check(not isinstance(pathPtr, pathlib.Path))

pathRef = makePathRef(p)
check(not isinstance(pathRef, pathlib.Path))

pathConstRef = makePathConstRef(p)
check(not isinstance(pathConstRef, pathlib.Path))

#
# Now test various input typemaps. Each of the wrapped C++ functions
# (pathToStr, pathConstRefToStr, pathPtrToStr) is expecting an argument of a
# different type (see li_std_filesystem.i). Typemaps should be in place to
# convert this pathlib.Path into the expected argument type.
#
check(pathToStr(path) == p)
check(pathConstRefToStr(path) == p)
check(pathPtrToStr(path) == p)

#
# Similarly, each of the input typemaps should know what to do
# with a string.
#
check(pathToStr(p) == p)
check(pathConstRefToStr(p) == p)
check(pathPtrToStr(p) == p)

#
# Similarly, each of the input typemaps should know what to do
# with a std::filesystem::path instance.
#
check(pathToStr(pathPtr) == p)
check(pathConstRefToStr(pathPtr) == p)
check(pathPtrToStr(pathPtr) == p)
