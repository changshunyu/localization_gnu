# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_customModule_swig')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_customModule_swig')
    _customModule_swig = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_customModule_swig', [dirname(__file__)])
        except ImportError:
            import _customModule_swig
            return _customModule_swig
        try:
            _mod = imp.load_module('_customModule_swig', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _customModule_swig = swig_import_helper()
    del swig_import_helper
else:
    import _customModule_swig
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now() -> "gr::high_res_timer_type":
    """high_res_timer_now() -> gr::high_res_timer_type"""
    return _customModule_swig.high_res_timer_now()

def high_res_timer_now_perfmon() -> "gr::high_res_timer_type":
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _customModule_swig.high_res_timer_now_perfmon()

def high_res_timer_tps() -> "gr::high_res_timer_type":
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _customModule_swig.high_res_timer_tps()

def high_res_timer_epoch() -> "gr::high_res_timer_type":
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _customModule_swig.high_res_timer_epoch()
class ofdm_sync_shunyu(object):
    """
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of customModule::ofdm_sync_shunyu.

    To avoid accidental use of raw pointers, customModule::ofdm_sync_shunyu's constructor is in a private implementation class. customModule::ofdm_sync_shunyu::make is the public interface for creating new instances.

    Args:
        fft_len : 
        cp_len : 
        use_even_carriers : 
        threshold : 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make(fft_len: 'int', cp_len: 'int', use_even_carriers: 'bool'=False, threshold: 'float'=0.9) -> "gr::customModule::ofdm_sync_shunyu::sptr":
        """
        make(int fft_len, int cp_len, bool use_even_carriers=False, float threshold=0.9) -> ofdm_sync_shunyu_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of customModule::ofdm_sync_shunyu.

        To avoid accidental use of raw pointers, customModule::ofdm_sync_shunyu's constructor is in a private implementation class. customModule::ofdm_sync_shunyu::make is the public interface for creating new instances.

        Args:
            fft_len : 
            cp_len : 
            use_even_carriers : 
            threshold : 
        """
        return _customModule_swig.ofdm_sync_shunyu_make(fft_len, cp_len, use_even_carriers, threshold)

    make = staticmethod(make)
    __swig_destroy__ = _customModule_swig.delete_ofdm_sync_shunyu
    __del__ = lambda self: None
ofdm_sync_shunyu_swigregister = _customModule_swig.ofdm_sync_shunyu_swigregister
ofdm_sync_shunyu_swigregister(ofdm_sync_shunyu)

def ofdm_sync_shunyu_make(fft_len: 'int', cp_len: 'int', use_even_carriers: 'bool'=False, threshold: 'float'=0.9) -> "gr::customModule::ofdm_sync_shunyu::sptr":
    """
    ofdm_sync_shunyu_make(int fft_len, int cp_len, bool use_even_carriers=False, float threshold=0.9) -> ofdm_sync_shunyu_sptr

    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of customModule::ofdm_sync_shunyu.

    To avoid accidental use of raw pointers, customModule::ofdm_sync_shunyu's constructor is in a private implementation class. customModule::ofdm_sync_shunyu::make is the public interface for creating new instances.

    Args:
        fft_len : 
        cp_len : 
        use_even_carriers : 
        threshold : 
    """
    return _customModule_swig.ofdm_sync_shunyu_make(fft_len, cp_len, use_even_carriers, threshold)

class ofdm_sync_shunyu_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::customModule::ofdm_sync_shunyu)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::customModule::ofdm_sync_shunyu)> self) -> ofdm_sync_shunyu_sptr
        __init__(boost::shared_ptr<(gr::customModule::ofdm_sync_shunyu)> self, ofdm_sync_shunyu p) -> ofdm_sync_shunyu_sptr
        """
        this = _customModule_swig.new_ofdm_sync_shunyu_sptr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self) -> "gr::customModule::ofdm_sync_shunyu *":
        """__deref__(ofdm_sync_shunyu_sptr self) -> ofdm_sync_shunyu"""
        return _customModule_swig.ofdm_sync_shunyu_sptr___deref__(self)

    __swig_destroy__ = _customModule_swig.delete_ofdm_sync_shunyu_sptr
    __del__ = lambda self: None

    def make(self, fft_len: 'int', cp_len: 'int', use_even_carriers: 'bool'=False, threshold: 'float'=0.9) -> "gr::customModule::ofdm_sync_shunyu::sptr":
        """
        make(ofdm_sync_shunyu_sptr self, int fft_len, int cp_len, bool use_even_carriers=False, float threshold=0.9) -> ofdm_sync_shunyu_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of customModule::ofdm_sync_shunyu.

        To avoid accidental use of raw pointers, customModule::ofdm_sync_shunyu's constructor is in a private implementation class. customModule::ofdm_sync_shunyu::make is the public interface for creating new instances.

        Args:
            fft_len : 
            cp_len : 
            use_even_carriers : 
            threshold : 
        """
        return _customModule_swig.ofdm_sync_shunyu_sptr_make(self, fft_len, cp_len, use_even_carriers, threshold)


    def primitive_connect(self, *args) -> "void":
        """
        primitive_connect(ofdm_sync_shunyu_sptr self, basic_block_sptr block)
        primitive_connect(ofdm_sync_shunyu_sptr self, basic_block_sptr src, int src_port, basic_block_sptr dst, int dst_port)
        """
        return _customModule_swig.ofdm_sync_shunyu_sptr_primitive_connect(self, *args)


    def primitive_msg_connect(self, *args) -> "void":
        """
        primitive_msg_connect(ofdm_sync_shunyu_sptr self, basic_block_sptr src, swig_pmt_ptr srcport, basic_block_sptr dst, swig_pmt_ptr dstport)
        primitive_msg_connect(ofdm_sync_shunyu_sptr self, basic_block_sptr src, std::string srcport, basic_block_sptr dst, std::string dstport)
        """
        return _customModule_swig.ofdm_sync_shunyu_sptr_primitive_msg_connect(self, *args)


    def primitive_msg_disconnect(self, *args) -> "void":
        """
        primitive_msg_disconnect(ofdm_sync_shunyu_sptr self, basic_block_sptr src, swig_pmt_ptr srcport, basic_block_sptr dst, swig_pmt_ptr dstport)
        primitive_msg_disconnect(ofdm_sync_shunyu_sptr self, basic_block_sptr src, std::string srcport, basic_block_sptr dst, std::string dstport)
        """
        return _customModule_swig.ofdm_sync_shunyu_sptr_primitive_msg_disconnect(self, *args)


    def primitive_disconnect(self, *args) -> "void":
        """
        primitive_disconnect(ofdm_sync_shunyu_sptr self, basic_block_sptr block)
        primitive_disconnect(ofdm_sync_shunyu_sptr self, basic_block_sptr src, int src_port, basic_block_sptr dst, int dst_port)
        """
        return _customModule_swig.ofdm_sync_shunyu_sptr_primitive_disconnect(self, *args)


    def disconnect_all(self) -> "void":
        """disconnect_all(ofdm_sync_shunyu_sptr self)"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_disconnect_all(self)


    def lock(self) -> "void":
        """lock(ofdm_sync_shunyu_sptr self)"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_lock(self)


    def unlock(self) -> "void":
        """unlock(ofdm_sync_shunyu_sptr self)"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_unlock(self)


    def primitive_message_port_register_hier_in(self, port_id: 'swig_pmt_ptr') -> "void":
        """primitive_message_port_register_hier_in(ofdm_sync_shunyu_sptr self, swig_pmt_ptr port_id)"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_primitive_message_port_register_hier_in(self, port_id)


    def primitive_message_port_register_hier_out(self, port_id: 'swig_pmt_ptr') -> "void":
        """primitive_message_port_register_hier_out(ofdm_sync_shunyu_sptr self, swig_pmt_ptr port_id)"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_primitive_message_port_register_hier_out(self, port_id)


    def set_processor_affinity(self, mask: 'std::vector< int,std::allocator< int > > const &') -> "void":
        """set_processor_affinity(ofdm_sync_shunyu_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self) -> "void":
        """unset_processor_affinity(ofdm_sync_shunyu_sptr self)"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_unset_processor_affinity(self)


    def processor_affinity(self) -> "std::vector< int,std::allocator< int > >":
        """processor_affinity(ofdm_sync_shunyu_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_processor_affinity(self)


    def set_log_level(self, level: 'std::string') -> "void":
        """set_log_level(ofdm_sync_shunyu_sptr self, std::string level)"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_set_log_level(self, level)


    def log_level(self) -> "std::string":
        """log_level(ofdm_sync_shunyu_sptr self) -> std::string"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_log_level(self)


    def max_output_buffer(self, i: 'int') -> "size_t":
        """max_output_buffer(ofdm_sync_shunyu_sptr self, int i) -> size_t"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args) -> "void":
        """
        set_max_output_buffer(ofdm_sync_shunyu_sptr self, size_t max_output_buffer)
        set_max_output_buffer(ofdm_sync_shunyu_sptr self, int port, size_t max_output_buffer)
        """
        return _customModule_swig.ofdm_sync_shunyu_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i: 'int') -> "size_t":
        """min_output_buffer(ofdm_sync_shunyu_sptr self, int i) -> size_t"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args) -> "void":
        """
        set_min_output_buffer(ofdm_sync_shunyu_sptr self, size_t min_output_buffer)
        set_min_output_buffer(ofdm_sync_shunyu_sptr self, int port, size_t min_output_buffer)
        """
        return _customModule_swig.ofdm_sync_shunyu_sptr_set_min_output_buffer(self, *args)


    def to_hier_block2(self) -> "gr::hier_block2_sptr":
        """to_hier_block2(ofdm_sync_shunyu_sptr self) -> hier_block2_sptr"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_to_hier_block2(self)


    def name(self) -> "std::string":
        """name(ofdm_sync_shunyu_sptr self) -> std::string"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_name(self)


    def symbol_name(self) -> "std::string":
        """symbol_name(ofdm_sync_shunyu_sptr self) -> std::string"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_symbol_name(self)


    def input_signature(self) -> "gr::io_signature::sptr":
        """input_signature(ofdm_sync_shunyu_sptr self) -> io_signature_sptr"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_input_signature(self)


    def output_signature(self) -> "gr::io_signature::sptr":
        """output_signature(ofdm_sync_shunyu_sptr self) -> io_signature_sptr"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_output_signature(self)


    def unique_id(self) -> "long":
        """unique_id(ofdm_sync_shunyu_sptr self) -> long"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_unique_id(self)


    def to_basic_block(self) -> "gr::basic_block_sptr":
        """to_basic_block(ofdm_sync_shunyu_sptr self) -> basic_block_sptr"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_to_basic_block(self)


    def check_topology(self, ninputs: 'int', noutputs: 'int') -> "bool":
        """check_topology(ofdm_sync_shunyu_sptr self, int ninputs, int noutputs) -> bool"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_check_topology(self, ninputs, noutputs)


    def alias(self) -> "std::string":
        """alias(ofdm_sync_shunyu_sptr self) -> std::string"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_alias(self)


    def set_block_alias(self, name: 'std::string') -> "void":
        """set_block_alias(ofdm_sync_shunyu_sptr self, std::string name)"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_set_block_alias(self, name)


    def _post(self, which_port: 'swig_pmt_ptr', msg: 'swig_pmt_ptr') -> "void":
        """_post(ofdm_sync_shunyu_sptr self, swig_pmt_ptr which_port, swig_pmt_ptr msg)"""
        return _customModule_swig.ofdm_sync_shunyu_sptr__post(self, which_port, msg)


    def message_ports_in(self) -> "pmt::pmt_t":
        """message_ports_in(ofdm_sync_shunyu_sptr self) -> swig_pmt_ptr"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_message_ports_in(self)


    def message_ports_out(self) -> "pmt::pmt_t":
        """message_ports_out(ofdm_sync_shunyu_sptr self) -> swig_pmt_ptr"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_message_ports_out(self)


    def message_subscribers(self, which_port: 'swig_pmt_ptr') -> "pmt::pmt_t":
        """message_subscribers(ofdm_sync_shunyu_sptr self, swig_pmt_ptr which_port) -> swig_pmt_ptr"""
        return _customModule_swig.ofdm_sync_shunyu_sptr_message_subscribers(self, which_port)

ofdm_sync_shunyu_sptr_swigregister = _customModule_swig.ofdm_sync_shunyu_sptr_swigregister
ofdm_sync_shunyu_sptr_swigregister(ofdm_sync_shunyu_sptr)


ofdm_sync_shunyu_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
ofdm_sync_shunyu = ofdm_sync_shunyu.make;



