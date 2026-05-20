class Piece:
    def __init__(self):
        self.color=0
        self.name='Tas'
        self.figure=' '
        self.ts=''
        self.board=None

    def CheckRules(self, From, To):
        return True

    def CheckPiece(self, From, To):
        return True

    def Play(self,From, To):
        b=self.CheckRules(From, To)
        if b:
            To.piece, From.piece = self, Piece()
        return b

    def NotNull(self,p):
        return not(p.name=="Tas")
        #return isinstance(p,Sah) or isinstance(p,Piyon) or isinstance(p,Vezir) or isinstance(p,At) or isinstance(p,Fil)

    @staticmethod
    def Sign(sayi):
        if sayi > 0:
            return 1
        elif sayi < 0:
            return -1
        else:
            return 0

class Piyon(Piece):
    def __init__(self):
        super().__init__()
        self.name="Piyon"
        self.firstMove=True

    def CheckRules(self,From, To):

        frm=list(From.name)
        to=list(To.name)
        x=ord(frm[0])
        y=int(frm[1])
        add=int(self.firstMove)
        
            
        directions = [
            (0, 1+add), (0, 1), # Dikey ve yatay
            (1, 1), (-1, 1)  # Çapraz
        ]

        directions_new=[]
        if self.color==1:
            for i,j in directions:
                i = -1*i
                j = -1*j
                directions_new.append((i,j))
            directions=directions_new
                
        valid_moves = [
            (chr(x + dx) +str(y + dy)) for dx, dy in directions
            if 65 <= x + dx < 73 and 1 <= y + dy <= 8
        ]

        validMove=To.name in valid_moves
        b=self.CheckPiece(From,To)
        if validMove and b:
            self.firstMove=False
        return validMove

    def CheckPiece(self, From, To):
        frm=list(From.name)
        to=list(To.name)
        xf=ord(frm[0])
        yf=int(frm[1])

        xt=ord(to[0])
        yt=int(to[1])

        difX=(xt-xf)
        difY=(yt-yf)

        sx=Piece.Sign(difX)
        sy=Piece.Sign(difY)

        step=max(difX,difY)
        b=True
        s=0
        while s<step:
            xf = xf + sx
            yf = yf +sy

            p=chr(xf)+str(yf)
            piece=self.board.board[p].piece
            b = b and not(self.NotNull(piece))

            s +=1
        return b

class Sah(Piece):
    def __init__(self):
        super().__init__()
        self.name="Sah"

    def CheckRules(self, From, To):
        frm=list(From.name)
        to=list(To.name)
        x=ord(frm[0])
        y=int(frm[1])
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Dikey ve yatay
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Çapraz
        ]

        valid_moves = [
            (chr(x + dx) +str(y + dy)) for dx, dy in directions
            if 65 <= x + dx < 73 and 1 <= y + dy <= 8
        ]

        geoRule= To.name in valid_moves
        noPiece = self.CheckPiece(From,To)

        return geoRule and noPiece

    def CheckPiece(self, From, To):
        frm=list(From.name)
        to=list(To.name)
        xf=ord(frm[0])
        yf=int(frm[1])

        xt=ord(to[0])
        yt=int(to[1])

        difX=(xt-xf)
        difY=(yt-yf)

        sx=Piece.Sign(difX)
        sy=Piece.Sign(difY)
        step=max(difX,difY)
        
        b=True
        s=0
        while s<step:
            xf = xf + sx
            yf = yf +sy

            p=chr(xf)+str(yf)
            piece=self.board.board[p].piece
            b = b and not(self.NotNull(piece))

            s +=1

        piece=self.board.board[chr(xt)+str(yt)].piece
        if self.NotNull(piece):
            b = b and not(piece.color==self.color)

        return b


class Vezir(Piece):
    def __init__(self):
        super().__init__()
        self.name="Vezir"

    def CheckRules(self, From, To):
        frm=list(From.name)
        to=list(To.name)
        x=ord(frm[0])
        y=int(frm[1])
        directions = [
            (1, 0), (-1, 0),  # dikey (aşağı, yukarı)
            (0, 1), (0, -1),  # yatay (sağ, sol)
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # çaprazlar
        ]

        valid_moves = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 65 <= nx < 73 and 1 <= ny <= 8:
                valid_moves.append(chr(nx)+str(ny))
                nx += dx
                ny += dy

        return To.name in valid_moves



class Fil(Piece):
    def __init__(self):
        super().__init__()
        self.name="Fil"

    def CheckRules(self, From, To):
        frm=list(From.name)
        to=list(To.name)
        x=ord(frm[0])
        y=int(frm[1])

        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # 4 çapraz yön
        valid_moves = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 65 <= nx < 73 and 1 <= ny <= 8:
                nm=chr(nx)+str(ny)
                if self.board.board[nm].piece.name=='Tas' or (self.board.board[nm].piece==To.piece and not(To.piece.color==self.color)):
                    valid_moves.append(nm)
                else:
                    break
                nx += dx
                ny += dy

        return To.name in valid_moves


class At(Piece):
    def __init__(self):
        super().__init__()
        self.name="At"

    def CheckRules(self, From, To):
        frm=list(From.name)
        to=list(To.name)
        x=ord(frm[0])
        y=int(frm[1])
        toHarf=ord(to[0])
        toSayi=int(to[1])

        possible_moves=[chr(x+2)+str(y + 1), chr(x + 2)+str( y - 1),
            chr(x - 2)+str( y + 1), chr(x - 2)+str( y - 1),
            chr(x + 1)+str( y + 2), chr(x + 1)+ str(y - 2),
            chr(x - 1)+str( y + 2), chr(x - 1)+str(y - 2)]

        return To.name in possible_moves



class Kale(Piece):
    def __init__(self):
        super().__init__()
        self.name="Kale"

    def CheckRules(self, From, To):
        frm=list(From.name)
        to=list(To.name)
        x=ord(frm[0])
        y=int(frm[1])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Dikey ve yatay
        valid_moves = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 65 <= nx < 73 and 1 <= ny <= 8:
                valid_moves.append(chr(nx)+str(ny))
                nx += dx
                ny += dy

        return To.name in valid_moves

