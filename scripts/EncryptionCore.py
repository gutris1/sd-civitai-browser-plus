from PIL import Image
import hashlib
import numpy as np

def get_range(input: str, offset: int, range_len=4):
    offset = offset % len(input)
    return (input * 2)[offset:offset + range_len]

def get_sha256(input: str):
    return hashlib.sha256(input.encode('utf-8')).hexdigest()

def shuffle_arr_v2(arr, key):
    sha_key = get_sha256(key)
    arr_len = len(arr)

    for i in range(arr_len):
        s_idx = arr_len - i - 1
        to_index = int(get_range(sha_key, i, range_len=8), 16) % (arr_len - i)
        arr[s_idx], arr[to_index] = arr[to_index], arr[s_idx]

    return arr

def encrypt_image_v3(image: Image.Image, psw):
    try:
        width = image.width
        height = image.height
        x_arr = np.arange(width)
        shuffle_arr_v2(x_arr,psw) 
        y_arr = np.arange(height)
        shuffle_arr_v2(y_arr,get_sha256(psw))
        pixel_array = np.array(image)
        
        _pixel_array = pixel_array.copy()
        for x in range(height): 
            pixel_array[x] = _pixel_array[y_arr[x]]
        pixel_array = np.transpose(pixel_array, axes=(1, 0, 2))
        
        _pixel_array = pixel_array.copy()
        for x in range(width): 
            pixel_array[x] = _pixel_array[x_arr[x]]
        pixel_array = np.transpose(pixel_array, axes=(1, 0, 2))

        return pixel_array
    except Exception as e:
        if "axes don't match array" in str(e):
            return np.array(image)

def decrypt_image_v3(image: Image.Image, psw):
    try:
        width = image.width
        height = image.height
        x_arr = np.arange(width)
        shuffle_arr_v2(x_arr, psw)
        y_arr = np.arange(height)
        shuffle_arr_v2(y_arr, get_sha256(psw))
        pixel_array = np.array(image)

        _pixel_array = pixel_array.copy()
        for x in range(height): 
            pixel_array[y_arr[x]] = _pixel_array[x]
        pixel_array = np.transpose(pixel_array, axes=(1, 0, 2))

        _pixel_array = pixel_array.copy()
        for x in range(width): 
            pixel_array[x_arr[x]] = _pixel_array[x]
        pixel_array = np.transpose(pixel_array, axes=(1, 0, 2))

        return pixel_array

    except Exception as e:
        if "axes don't match array" in str(e):
            return np.array(image)
