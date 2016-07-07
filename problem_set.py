from PIL import Image
import imageutil 
class ProblemSet:
    def __init__(self, name):
        self.max_id = int(open('%s/max.txt' % name).read())
        self.name = name
        self.problems = []
        for i in range(self.max_id):
            p = a = None
            try:
                p = Image.open('%s/%d_p.bmp' % (name, i)) 
                a = Image.open('%s/%d_a.bmp' % (name, i)) 
            except:
                continue
            self.problems.append((p, a))

    def add(self, p, a):
        self.problems.append((p, a))
        p.save('%s/%d_p.bmp' % (self.name, self.max_id))
        a.save('%s/%d_a.bmp' % (self.name, self.max_id))
        self.max_id = self.max_id + 1
        f = open('%s/max.txt' % self.name, 'w')
        f.write(str(self.max_id))
        f.close()

    def query(self, p):
        for candidate in self.problems:
            if imageutil.equal_image(p, candidate[0]):
                print imageutil.diff_image(p, candidate[0])
                return candidate[1]
        return None
