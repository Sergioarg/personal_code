from pprint import pprint


range_clases = range(64, 73)
range_xpaths = ["%.2d" % i for i in range(6, 15)]


clases_comp = {
    f'clase_{clase}': f'//*[@id="Grid1ContainerRow_00{xpath}"]/td[6]'
    for (clase, xpath) in zip(range_clases, range_xpaths)
}


pprint(clases_comp)
