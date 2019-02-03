# https://forum.omz-software.com/topic/2271/beta-suggestion-safariviewcontroller/3

# coding: utf-8

from objc_util import *
import appex

SFSafariViewController = ObjCClass('SFSafariViewController')

UIApplication = ObjCClass('UIApplication')


def open_in_safari_vc(url):
    vc = SFSafariViewController.alloc().initWithURL_entersReaderIfAvailable_(nsurl(url), True)
    
    root_vc = UIApplication.sharedApplication().keyWindow().rootViewController()
    
    while root_vc.presentedViewController():
        root_vc = root_vc.presentedViewController()
    root_vc.presentViewController_animated_completion_(vc, True, None)
    vc.release()

def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    url = appex.get_url()
    if not url:
        print('No input url')
        return
    open_in_safari_vc(url)
    
if __name__ == '__main__':
    main()

