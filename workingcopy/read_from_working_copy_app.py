#!/usr/bin/env python3
# coding: utf-8

# 工作流程：*在_Working Copy_中打开要复制到_Pythonista_ *的GitHub存储库，如果您的需求较为温和，您甚至可以选择单个文件或文件夹*单击工作复制屏幕右上角的共享图标*单击运行Pythonista脚本*单击此脚本*单击运行按钮

# 当你[返回Pythonista]（pythonista：//）时，你的文件应该在'from Working Copy'目录中

## Pythonista  - &gt;工作副本：工作副本有一个“__save to Working Copy__”共享表操作（您可能必须在共享表中启用，更多...）

# 工作流程A  - 单个文件：*在Pythonista编辑器中打开感兴趣的文件*单击右上角的扳手图标*单击“共享...”按钮*单击“保存在工作副本”按钮*选择回购您要将文件保存到*单击“另存为...”*如果需要更改文件名并再次单击“另存为...”如果要将多个文件捆绑到一个文件中，请单击“仅保存”单个提交 - 或 - 键入您的提交消息，然后单击“提交”

# 工作流程B  - 文件夹或文件：*在Pythonista文件浏览器中单击“编辑”*选择感兴趣的文件夹或文件*单击文件浏览器底部的“共享”图标*单击“保存在工作副本”按钮*选择“导入为存储库”或“另存为目录”

# 注意：选择多个文件夹或多个文件时，仅处理第一个文件夹或多个文件.

# __现在我们有一个端到端的工作流程：GitHub  - &gt;工作副本 - &gt; Pythonista  - &gt;工作副本 - &gt; GitHub__

# See: https://forum.omz-software.com/topic/2382/git-or-gist-workflow-for-pythonista/24

# Appex script to copy a git file, folder, or repo from the Working Copy app

import appex, os, shutil

from_wc = os.path.abspath(os.path.expanduser('from Working Copy'))


def main():
    if appex.is_running_extension():
        file_paths = appex.get_file_paths()
        assert len(file_paths) == 1, 'Invalid file paths: {}'.format(file_paths)
        srce_path = file_paths[0]
        dest_path = srce_path.split('/File Provider Storage/')[-1]
        dest_path = os.path.join(from_wc, dest_path)
        file_path, file_name = os.path.split(dest_path)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        if os.path.isdir(srce_path):
            shutil.rmtree(dest_path, ignore_errors=True)
            print(shutil.copytree(srce_path, dest_path))
        else:
            print(shutil.copy2(srce_path, dest_path))
        print('{} was copied to {}'.format(file_name, file_path))
    else:
        print('''* In Working Copy app select a repo, file, or directory to be
copied into Pythonista.  Click the Share icon at the upperight.  Click Run
Pythonista Script.  Pick this script and click the run button.  When you return
to Pythonista the files should be in the 'from Working Copy'
directory.'''.replace('\n', ' ').replace('.  ', '.\n* '))

if __name__ == '__main__':
    main()
