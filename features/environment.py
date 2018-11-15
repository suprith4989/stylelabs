import os
from config_parser import data
from selenium import webdriver

def before_all(context):
    context.data = data

def before_scenario(context, scenario):
    context.running_scenario = scenario
    profile = webdriver.FirefoxProfile()
    context.browser = webdriver.Firefox(profile)

def after_scenario(context, scenario):
    context.browser.quit()

def get_feature_name(feature_name):
    names_dict = {"Surf Google": "None"}
    return(names_dict[feature_name])
