from RestrictedPython import compile_restricted
from RestrictedPython import limited_builtins
from RestrictedPython import safe_builtins
from RestrictedPython.PrintCollector import PrintCollector
from RestrictedPython.Guards import full_write_guard
from RestrictedPython.Eval import default_guarded_getiter


#defining additional available builtin functions
safe_builtins["_getiter_"] = default_guarded_getiter
safe_builtins["_getattr_"] = getattr
safe_builtins["_write_"] = full_write_guard



def run_code(source_code,function_name="myFunc",input_values=[""], output_values=""):

    output = {} 
    try: 
        code = compile_restricted(source_code,'<string>','exec') 
    except SyntaxError as e: return f"Syntax Error {e}"
    print(source_code)
    
    try:
        exec(code,{'__builtins__':safe_builtins},output)
    except SyntaxError as e:
        print(f"Synax error by user: {e}")
        #user facing return
        return "syntax error"
    except ImportError as oi:
        return "Hey now, I said no importing packages :<"
    try:
        if len(input_values) > 0:
            out = output[function_name](input_values)
        else: out = output[function_name]()

        if out == output_values:
            return "success"
        else:
            return "fail"


    except KeyError as k:
        print(k)
        print(f"function {function_name} not found in \n{source_code}")
        #user facing return
        return f"function {function_name} not found"

    except SyntaxError as e: 
        return f"syntax error {e}"

    except:
        return "Stop executing that sus code now. By the way, you've been reported :)"
