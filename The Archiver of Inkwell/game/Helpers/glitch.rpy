init python:
    class glitch(renpy.Displayable):
        """
        'randkey'
            follows rules of rand module's seed func
            if not set, rand seed generated when transform applied,
                and stays same after
            if want effect to be rand for each render op, set to None
        
        'chroma'
            boolean, whether to apply chromatic abberation effect
        
        'minbandheight'
            min height of each slice
        
        'offset'
            offset of each slice will be between -offset and offset pixels

        'nslices'
            num of slicings to do (num of slices will be nslices + 1)
            setting this to 0 is not supported
            None (default) makes it rand
        """
        NotSet = object()

        def __init__(self,child,*,randkey=NotSet,chroma=True,minbandheight=1,offset=30,nslices=None,**properties):
            super().__init__(**properties)
            self.child = renpy.displayable(child)
            if randkey is self.NotSet:
                randkey = renpy.random.random()
            self.randkey = randkey
            self.chroma = chroma
            self.minbandheight = minbandheight
            self.offset = offset
            self.nslices = nslices
        
        def render(self,width,height,st,at):
            child = self.child
            child_render = renpy.render(child,width,height,st,at)
            cwidth,cheight = child_render.get_size()
            if not (cwidth and cheight):
                return child_render
            render = renpy.Render(cwidth, cheight)
            randobj = renpy.random.Random(self.randkey)
            chroma = self.chroma and renpy.display.render.models
            offset = self.offset
            minbandheight = self.minbandheight
            nslices = self.nslices
            if nslices is None:
                nslices = min(int(cheight/minbandheight),randobj.randint(10,21))
            theights = sorted(randobj.randint(0,cheight+1) for k in range(nslices))
            offt = 0
            fheight = 0
            while fheight < cheight:
                if theights:
                    theight = max(theights.pop(0)-fheight,minbandheight)
                else:
                    theight = cheight - theight
                
                slice_render = child_render.subsurface((0,fheight,cwidth,theight))

                if offt and chroma:
                    for color_mask, chponder in ((False, False, True, True), 1.25), ((False, True, False, True), 1.), ((True, False, False, True), .75):
                        chroma_render = slice_render.subsurface((0,0,cwidth,theight))
                        chroma_render.add_property("gl_color_mask", color_mask)
                        render.blit(chroma_render,(round(offt*chponder),round(fheight)))
                else:
                    render.blit(slice_render,(offt,round(fheight)))
                
                fheight += theight
                if offt:
                    offt = 0
                else:
                    offt = randobj.randint(-offset,offset+1)
            return render
        
        def visit(self):
            return [self.child]
    
    class animated_glitch(glitch):
        """
        gltiches in way that changes over time, but consistently, unlike glitch(randkey=None)
        sets a timeout at the beginning. Att end of each timeout, sets a new one and changes glitching

        'timeout_base'
            time in seconds between two changes of glitching
            can be either single float (or int) value, or tuple of two values between which the timeout 
                will be chosen
            defaults to .1 seconds 
        
        'timeout_vanilla'
            length in seconds of periods of time over which child will be shown without glitch
            same values and meaning as 'timeout_base', except that if false, child will never be shown without glitch
            if 'timeout_base' is passed, defaults to same value. otherwise defaults to (1,3)
        """

        def __init__(self,*args,timeout_base=None,timeout_vanilla=None,**kwargs):
            super().__init__(*args,**kwargs)
            if timeout_vanilla is None:
                if timeout_base is None:
                    timeout_vanilla = (1,3)
                else:
                    timeout_vanilla = timeout_base
            
            if timeout_base is None:
                timeout_base = .1
            
            self.timeout_base = timeout_base
            self.timeout_vanilla = timeout_vanilla
            self.set_timeout(vanilla=(timeout_vanilla is not False))
        
        def set_timeout(self,vanilla,st=0):
            if vanilla:
                timeout = self.timeout_vanilla
            else:
                timeout = self.timeout_base
            
            if not isinstance(timeout,(int,float)):
                timeout = renpy.random.Random(self.randkey).uniform(*timeout)
            
            self.timeout = timeout + st
            self.showing_vanilla = vanilla
        
        def render(self,width,height,st,at):
            vanilla = self.showing_vanilla
            if st >= self.timeout:
                randkey = self.randkey
                randobj = renpy.random.Random(randkey)
                self.randkey = randobj.random()

                if vanilla or (self.timeout_vanilla is False):
                    vanilla = False
                else:
                    vanilla = (randobj.random() < .3)
                self.set_timeout(vanilla, st)
            
            renpy.redraw(self, st - self.timeout)

            if vanilla:
                return renpy.render(self.child, width, height, st, at)
            else:
                return super().render(width, height, st, at)
        
    class square_glitch(renpy.Displayable):
        """
        'squareside'
            size, in pixels, of side of squares the child image will be cut to. this will
                be adjusted so that all "squares" (actually rectangles) have same width and 
                height, and that none are cut at borders of the image. defaults to 20 pixels
        
        'chroma'
            probability for each square to get chromatic effect. defaults to .25
        
        'permutes'
            percentage of squares which will be moved to another square's place. if not passed,
                defaults to rand value between .1 and .4
        """
        NotSet = object()

        def __init__(self,child,*args,randkey=NotSet,**kwargs):
            super().__init__()
            self.child = renpy.displayable(child)
            self.args = args
            if randkey is self.NotSet:
                randkey = renpy.random.random()
            self.randkey = randkey
            self.kwargs = kwargs
        
        def render(self,width,height,st,at):
            cwidth, cheight = renpy.render(self.child, width, height, st, at).get_size()
            return renpy.render(self.glitch(self.child, cwidth, cheight, renpy.random.Random(self.randkey), *self.args, **self.kwargs),
                                width, height, st, at)
        
        @staticmethod
        def glitch(child,cwidth,cheight,randobj,squareside=20,chroma=.25,permutes=None,minbandheight=1):
            if not renpy.display.render.models:
                chroma = False
            if not (cwidth and cheight):
                return child

            ncols = round(cwidth / squareside)
            nrows = round(cheight/squareside)
            square_width = absolute(cwidth / ncols)
            square_height = absolute(cheight / nrows)

            lizt = []
            for y in range(nrows):
                for x in range(ncols):
                    lizt.append(Transform(child, crop = (absolute(x * square_width), absolute(y * square_height),
                                                            square_width, square_height), subpixel = True))
            
            if permutes is None:
                permutes = randobj.randint(10,40) / 100
            permutes = round(permutes * ncols * nrows)
            permute_a = randobj.sample(range(ncols * nrows), permutes)
            permute_b = randobj.sample(range(ncols * nrows), permutes)

            for a, b in zip(permute_a, permute_b):
                lizt[a], lizt[b] = lizt[b], lizt[a]
            
            for k, el in enumerate(lizt):
                if randobj.random() < chroma:
                    lizt[k] = Transform(el, gl_color_mask = (randobj.random() < .33, randobj.random() < .33,
                                                            randobj.random() < .33, True), 
                                                            # matrixcolor = HueMatrix(randobj.random() * 360),
                                                            )
            
            return Grid(ncols, nrows, *lizt)

        def __eq__(self,other):
            return (type(self) == type(other)) and (self.args == other.args) and (self.kwargs == other.kwargs)