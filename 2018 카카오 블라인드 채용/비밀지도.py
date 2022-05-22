def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        overlay = str(bin(i | j)[2:])
        overlay = overlay.rjust(n, '0')
        overlay = overlay.replace('1', '#')
        overlay = overlay.replace('0', ' ')
        answer.append(overlay)

    return answer