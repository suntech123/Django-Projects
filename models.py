class Subject(models.Model):
    sub_id = models.IntegerField(primary_key=True)
    sub_name = models.CharField(max_length=100)
    sub_code = models.CharField(max_length=5)
    sub_alt_name = models.CharField(max_length=150)
    sub_desc = models.TextField()
    
class Topic(models.Model):
    topic_sub_id = models.ForeignKey(Subject,on_delete=)
    topic_id = models.IntegerField(primary_key=True)
    topic_name = models.CharField(max_length = 200)
    
class Subtopic(models.Model):
    subtopic_topic_id = models.ForeignKey(Topic,on_delete=)
    subtopic_id = models.IntegerField(primary_key=True)
    subtopic_name = models.CharField(max_length=300)
