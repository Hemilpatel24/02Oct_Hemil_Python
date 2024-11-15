class stdinfo:
    id = int
    nm = str

    def getdata(self):
        self.id = input("Enter ID:")
        self.nm = input("Enter your Name:")

    def printdata(self):
        print("ID:", self.id)
        print("Name:", self.nm)

st=stdinfo()
st.getdata()
st.printdata()