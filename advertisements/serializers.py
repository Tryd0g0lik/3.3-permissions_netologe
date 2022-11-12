import psycopg2
from django.contrib.auth.models import User
from rest_framework import serializers
from advertisements.models import Advertisement
from config import USER, PASS


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)
        read_only_fields = ['username', ]

class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""
    """
    
    :type - Serializer for relationship with Advertisement model of models.py 
    :param - validate_advertesmentd_count is Validator
    :param - validate_update is Validator
    :param - create() is def for requests the POST
    :param - update()  is def for requests the PUT
    :return of action for work with thw db from ads
    """

    creator = UserSerializer(
        read_only=True,
    )

    def validate_advertesmentd_count(self, number : int,
                                     creator_id : id):
        # ----------------
        # The Validator
        # TODO: The ads with the status 'OPEN' is more 'number' it's False, else True
        # ----------------
        print(creator_id)
        with psycopg2.connect(database="classified_ads", user=USER, password=PASS) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""
SELECT count(%s) FROM advertisements_advertisement
WHERE status = 'OPEN'
""" % (creator_id, ))

                response_count_open_adv = (cur.fetchall())[0][0]
        # cur.close()

        if response_count_open_adv < int("%s" % (number, )):
            return True

        raise serializers.ValidationError("Your 'OPEN-status advertisements more number 10")
        return False

    def validate_update(self, dict_instance, dict_responce):
        # ----------------
        # The Validator
        # TODO: This's varifacation  the instance data User with request data User
        # ----------------

        if len(str(dict_instance)) > 3\
          and len(str(dict_responce)) > 3\
          and str(dict_instance) == str(dict_responce):

            print(('True'))
            return True
        else:
            print(('False'))
            # HttpResponse('Unauthorized', status=401)
            raise serializers.ValidationError("This's not your advertisement")

            return False
    class Meta:

        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )



    def create(self, validated_data):
        i = self.context['request'].user.id
        response_boolen = AdvertisementSerializer.validate_advertesmentd_count(
            self, number=10,
            creator_id=i
            ) # Validation

        if response_boolen == True:
            validated_data["creator"] = self.context["request"].user
            return super().create(validated_data)

        return



    def update(self, instance, validated_data):
        # ----------------
        # TODO: The update datas
        # ----------------

        responce_instance = instance.creator.username # The data from database (old data)
        responce_context = self.context['request']._user # The request data (new data)

        response = AdvertisementSerializer.validate_update(
            self,
            dict_instance=responce_instance,
            dict_responce=responce_context
        ) # Validation


        if response == False:
            return serializers.ValidationError

        else:

            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.save()

            return instance
