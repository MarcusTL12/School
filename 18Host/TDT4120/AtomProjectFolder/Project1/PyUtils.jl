using PyCall
@pyimport importlib.machinery as mach

function pyimp(file)
	mach.SourceFileLoader("module", abspath(joinpath(dirname(@__FILE__), file)))[:load_module]("module")
end
