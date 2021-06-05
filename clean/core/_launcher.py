if __name__ == '__main__':
    import json
    from _distributor import Worker
    Worker(*list(json.load(open('//jsons/working', 'r')).values())).forward()
