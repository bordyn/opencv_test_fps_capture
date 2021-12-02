#------------------------------------------------------------------------------------------------
#
#  Copyright 2021 by Bordyn Cheevatanakonkul.
#
#  Author: Bordyn Cheevatanakonkul.
#  License: MIT
#  Maintainer: Bordyn Cheevatanakonkul.
#  Email: bordyn.ch@gmail.com
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
#------------------------------------------------------------------------------------------------

import shutil
import os
import PyInstaller.__main__

# ----------------------------------------------------------------------------------------------------------------------
# settings

gen_path = "__gen"

base_source_path = "."
main_source_name = "capture"
module_name = f"{main_source_name}.py"
include_path = [base_source_path]

dist_path = os.path.join(gen_path,"dist")
build_path = os.path.join(gen_path,"build")
target = os.path.join(base_source_path,module_name)

# ----------------------------------------------------------------------------------------------------------------------

curr_dir = os.path.abspath(os.getcwd())

# ----------------------------------------------------------------------------------------------------------------------

# clean up old stuff
if os.path.isdir(dist_path):
    shutil.rmtree(dist_path)
if os.path.isdir(build_path):
    shutil.rmtree(build_path)

PyInstaller.__main__.run([
    target,
    '--clean',
    '--paths={}'.format(":".join(include_path)),
    '--distpath={}'.format(dist_path),
    '--workpath={}'.format(build_path)
])
os.remove(f"{main_source_name}.spec")
shutil.move(os.path.join(dist_path,f'{main_source_name}'),os.path.join(dist_path,'bin'))

with open(os.path.join(dist_path,"run.bat"),'w') as bat_file:
    bat_file.write(f"bin\\{main_source_name} --video=0")

# ----------------------------------------------------------------------------------------------------------------------
