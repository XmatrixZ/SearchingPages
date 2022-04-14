def insertionSort(links, significance, l, r):
    for i in range(l, r):

        significanceKey = significance[i]
        linksKey = links[i]

        j = i - 1
        while j >= 0 and significanceKey > significance[j]:
            significance[j + 1] = significance[j]
            links[j + 1] = links[j]
            j -= 1
        significance[j + 1] = significanceKey
        links[j + 1] = linksKey

def merge(links, significance, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    #     Llinks = links[l:n1]
    #     Rlinks = links[m+1:n2]
    #
    #     Lsignificances = significances[l:n1]
    #     Rsignificances = significances[m+1:n2]

    Lsignificance = [0] * (n1)
    Rsignificance = [0] * (n2)

    Llinks = [0] * (n1)
    Rlinks = [0] * (n2)

    for i in range(0, n1):
        Lsignificance[i] = significance[l + i]
        Llinks[i] = links[l + i]

    for j in range(0, n2):
        Rsignificance[j] = significance[m + 1 + j]
        Rlinks[j] = links[m + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if Lsignificance[i] >= Rsignificance[j]:
            significance[k] = Lsignificance[i]
            links[k] = Llinks[i]
            i += 1
        else:
            significance[k] = Rsignificance[j]
            links[k] = Rlinks[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        significance[k] = Lsignificance[i]
        links[k] = Llinks[i]
        i += 1
        k += 1

    while j < n2:
        significance[k] = Rsignificance[j]
        links[k] = Rlinks[j]
        j += 1
        k += 1


def WebpagesSort(links, significance, l, r):
    # Constion where Insertion sort is faster than merge sort
    if r <= l + 7:
        insertionSort(links,significance,l,r+1)
        return

    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        WebpagesSort(links, significance, l, m)
        WebpagesSort(links, significance, m + 1, r)

        if significance[m+1] <= significance[m]:
            merge(links, significance, l, m, r)

