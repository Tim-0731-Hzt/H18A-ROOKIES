def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    if img_url != 200:
        raise ValueError('url corrupted')
    size = 400
    if x_end > 400 or y_end >400 or x_start > 400 or y_start > 400:
        raise ValueError('Out of bound')
    if x_end < 0 or y_end < 0 or x_start < 0 or y_start < 0:
        raise ValueError('Out of bound')
    pass