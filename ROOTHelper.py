from ROOT import TFile, TTree, TH1F, TH1D, TCanvas


def tree_to_TH1F(var, tree, binning, cut="1", bins=0, xmin=0, xmax=0, opt=""):
    if bins == 0:
        bins = len(binning)-1
        name = var + "_hist"
        hist = TH1F(name, name, bins, binning)
        tree.Draw(var+">>"+name, cut, opt)
        return hist
    else:
        name = var + "_hist"
        hist = TH1F(name, name, bins, xmin, xmax)
        tree.Draw(var+">>"+name, cut, opt)
        return hist


def tree_to_TH1D(var, tree, binning, cut="1", bins=0, xmin=0, xmax=0, opt=""):
    if bins == 0:
        bins = len(binning)-1
        name = var + "_hist"
        hist = TH1D(name, name, bins, binning)
        tree.Draw(var+">>"+name, cut, opt)
        return hist
    else:
        name = var + "_hist"
        hist = TH1D(name, name, bins, xmin, xmax)
        tree.Draw(var+">>"+name, cut, opt)
        return hist


def plot_efficiency(name, numerator, denominator, xaxisTitle):
    efficiency = denominator.Clone()
    efficiency.Sumw2()
    efficiency.SetName(name)
    efficiency.SetTitle(name)
    efficiency.Divide(numerator, denominator, 1., 1., "B")
    efficiency.SetXTitle(xaxisTitle)
    efficiency.SetYTitle("Efficiency")
    return efficiency


def print_hist(hist, name, xsize=600, ysize=400,
               xaxis_title="", yaxis_title="", ymin=0, opt="hist",
               extension=".png"):
    canvas = TCanvas(name, name, xsize, ysize)
    xmax = get_xaxis_max(hist)
    xmin = get_xaxis_min(hist)
    ymax = get_yaxis_max(hist)
    titles = ";"+xaxis_title+";"+yaxis_title
    canvas.DrawFrame(xmin, ymin, xmax, ymax, titles)
    hist.Draw(opt)
    canvas.Print(name+extension)


def get_xaxis_max(hist):
    xmax = hist.GetBinLowEdge(hist.GetNbinsX()) +
    hist.GetBinWidth(hist.GetNbinsX())
    return xmax


def get_xaxis_min(hist):
    xmin = hist.GetBinLowEdge(1)
    return xmin


def get_yaxis_max(hist):
    ymax = -1
    for x in xrange(1, hist.GetNbinsX() + 1):
        if hist.GetBinContent(x) > ymax:
            ymax = hist.GetBinContent(x)
    return ymax

