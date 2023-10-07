# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r'^.*$'

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'^.*$'

# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = None

# Pattern for released versions
smv_released_pattern = r'^tags/.*$'

# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = False


''' 
=============================== 标签/分支/远程白名单配置例子 =============================== 
smv_tag_whitelist = r'^.*$'                   # Include all tags
smv_tag_whitelist = r'^v\d+\.\d+$'            # Include tags like "v2.1"

smv_branch_whitelist = r'^.*$'                # Include all branches
smv_branch_whitelist = r'^(?!master).*$'      # Include all branches except "master"

smv_remote_whitelist = None                   # Only use local branches
smv_remote_whitelist = r'^.*$'                # Use branches from all remotes
smv_remote_whitelist = r'^(origin|upstream)$' # Use branches from origin and upstream
=============================== 标签/分支/远程白名单配置例子 =============================== 


===================================== 发布模式配置例子 ===================================== 
smv_released_pattern = r'^tags/.*$'           # Tags only
smv_released_pattern = r'^heads/\d+\.\d+$'    # Branches like "2.1"
smv_released_pattern = r'^(tags/.*|heads/\d+\.\d+)$'           # Branches like "2.1" and all tags
smv_released_pattern = r'^(heads|remotes/[^/]+)/(?!:master).*$' # Everything except master branch
===================================== 发布模式配置例子 ===================================== 


=================================== 输出目录格式配置例子 ===================================
smv_outputdir_format = '{ref.name}'        # Use the branch/tag name
smv_outputdir_format = '{ref.commit}'      # Use the commit hash
smv_outputdir_format = '{ref.commit:.7s}'  # Use the commit hash truncated to 7 characters
smv_outputdir_format = '{ref.refname}'     # Use the full refname
smv_outputdir_format = '{ref.source}/{ref.name}'      # Equivalent to the previous example
smv_outputdir_format = 'versions/{config.release}'    # Use "versions" as parent directory and the "release" variable from conf.py
smv_outputdir_format = '{config.version}/{ref.name}'  # Use the version from conf.py as parent directory and the branch/tag name as subdirectory
=================================== 输出目录格式配置例子 ===================================


=================================== 覆盖配置变量配置例子 ===================================
sphinx-multiversion docs build/html -D 'exhale_args.containmentFolder=${sourcedir}/api'
=================================== 覆盖配置变量配置例子 ===================================

'''
