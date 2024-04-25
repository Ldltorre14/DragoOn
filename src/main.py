from DragoOn import DragoOn


compiler = DragoOn("""
                   begin\n
    \tvar1 = 2\n
    \tvar2 = 6\n
    \tvar3 = 0\n

    \tif(var1 <= var2)\n
        \tvar1 = var1 + 1\n
    \telse\n
        \tvar3 = var1\n    
end
                   """)

if __name__ == "__main__":
    compiler.run()
    compiler.scanner.printTokens()
    