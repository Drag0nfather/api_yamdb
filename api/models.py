from django.db import models


class Review(models.Model):
    RATING_RANGE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    )
    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='reviews'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(choices=RATING_RANGE)
    text = models.TextField(max_length=5000)
    title = models.ForeignKey(
        'Title', on_delete=models.CASCADE, related_name='reviews'
    )

    class Meta:
        ordering = ('-pub_date',)
        unique_together = ('author', 'title')

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField(max_length=500)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text
