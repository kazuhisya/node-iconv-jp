import os

def make(ctx, rule):
	os.system('make %s NODE_INCLUDE_PATH="%s"' % (rule, ctx.env['CPPPATH_NODE']))
	os.system('./apply_jp_patch.sh');

def set_options(ctx):
	pass

def configure(ctx):
	ctx.check_tool('node_addon')

def build(ctx):
	make(ctx, 'all')
