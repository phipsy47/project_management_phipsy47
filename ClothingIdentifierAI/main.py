import displaymodeldata as dm
import modelfitting as mf

def main():
    mod = mf.modelfitter
    mod.initFit(mod)
    dm.visualizeExamples(mod)
    
if __name__ == "__main__":
    main()
    