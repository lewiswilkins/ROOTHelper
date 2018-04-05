from ROOT import TFile, TTree, TH1F, TH1D, TCanvas

class ROOTHelper():
    def __init__(self, file_name, tree_name="" opt="READ"):
        self.file_name = file_name
        self.file = TFile(file_name, opt)
        if len(tree_name) > 0:
            self.tree = load_tree(tree_name)

        
    
    def load_tree(self, tree_name):
        self.tree = self.file.Get(tree_name)


    # def tree_to_TH1F(self, var, tree, binning, cut="1", bins=0, xmin=0, xmax=0, opt=""):
    #     if bins == 0:
    #         bins = len(binning)-1
    #         name = var + "_hist"
    #         hist = TH1F(name, name, bins, binning)
    #         tree.Draw(var+">>"+name, cut, opt)
    #         return hist
    #     else:
    #         name = var + "_hist"
    #         hist = TH1F(name, name, bins, xmin, xmax)
    #         tree.Draw(var+">>"+name, cut, opt)
    #         return hist


    # def tree_to_TH1D(self, var, tree, binning, cut="1", bins=0, xmin=0, xmax=0, opt=""):
    #     if bins == 0:
    #         bins = len(binning)-1
    #         name = var + "_hist"
    #         hist = TH1D(name, name, bins, binning)
    #         tree.Draw(var+">>"+name, cut, opt)
    #         return hist
    #     else:
    #         name = var + "_hist"
    #         hist = TH1D(name, name, bins, xmin, xmax)
    #         tree.Draw(var+">>"+name, cut, opt)
    #         return hist


    # def plot_efficiency(self, name, numerator, denominator, xaxisTitle):
    #     efficiency = denominator.Clone()
    #     efficiency.Sumw2()
    #     efficiency.SetName(name)
    #     efficiency.SetTitle(name)
    #     efficiency.Divide(numerator, denominator, 1., 1., "B")
    #     efficiency.SetXTitle(xaxisTitle)
    #     efficiency.SetYTitle("Efficiency")
    #     return efficiency


    # def print_hist(self, hist, name, xsize=600, ysize=400,
    #             xaxis_title="", yaxis_title="", ymin=0, opt="hist",
    #             extension=".png"):
    #     canvas = TCanvas(name, name, xsize, ysize)
    #     xmax = get_xaxis_max(hist)
    #     xmin = get_xaxis_min(hist)
    #     ymax = get_yaxis_max(hist)
    #     titles = ";"+xaxis_title+";"+yaxis_title
    #     canvas.DrawFrame(xmin, ymin, xmax, ymax, titles)
    #     hist.Draw(opt)
    #     canvas.Print(name+extension)

    # def print_hist_list(self, hists, names=[]):
    #     if len(names) == 0:
    #         for hist in hists:
    #             print_hist(hist, hist.GetName())
    #     else:
    #         if len(hists) == len(names):
    #             for hist,name in zip(hists, names):
    #                 print_hist(hist, name)
    #         else:
    #             raise IndexError
            

        
    # def get_xaxis_max(self, hist):
    #     xmax = hist.GetBinLowEdge(hist.GetNbinsX()) + hist.GetBinWidth(hist.GetNbinsX())
    #     return xmax


    # def get_xaxis_min(self, hist):
    #     xmin = hist.GetBinLowEdge(1)
    #     return xmin


    # def get_yaxis_max(self, hist):
    #     ymax = -1
    #     for x in xrange(1, hist.GetNbinsX() + 1):
    #         if hist.GetBinContent(x) > ymax:
    #             ymax = hist.GetBinContent(x)
    #     return ymax

