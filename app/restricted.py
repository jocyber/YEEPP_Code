from RestrictedPython import compile_restricted
from RestrictedPython import limited_builtins
from RestrictedPython import safe_builtins
from RestrictedPython.PrintCollector import PrintCollector
from RestrictedPython.Guards import full_write_guard
from RestrictedPython.Eval import default_guarded_getiter
# def exec_file(file_path,input):
#     with open(file_path,"r") as fp:
#         source_code = fp.read()
#
#     try:
#         byte_code = compile_restricted(source_code,filename=file_path,mode="exec")
#         exec(byte_code, {'__builtins__':limited_builtins}, None)
#
#     except SyntaxError as e:
#         return e


# _print_ = PrintCollector
# _getattr_=getattr

fibonacci = [1,2,3,4]

#_write_=full_write_guard
#_getattr_= getattr
#_getiter_ = default_guarded_getiter
#_print_=PrintCollector
fibofloppy = 1
print(safe_builtins)
safe_builtins["_getiter_"] = default_guarded_getiter
safe_builtins["_getattr_"] = getattr
safe_builtins["_write_"] = full_write_guard

src = """
fibofloppy = 1
for i in range(4):
    fibofloppy=fibofloppy+1

"""
code = compile_restricted(src,'<string>','exec')
exec(code, {'__builtins__': safe_builtins},{"fibofloppy":fibofloppy})

print(fibofloppy)