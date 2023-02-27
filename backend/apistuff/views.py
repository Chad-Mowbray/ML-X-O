from rest_framework.views import APIView
from rest_framework.response import Response
from .processor import transform_raw_line_data, prepare_db_samples_for_training, guess
from .models import SampleData
from .serializers import SampleDataSerializer
from .training import train

class Process(APIView):

    def get(self, request, format=None):
        resp = "Process endpoint"
        return Response(resp)
    
    def post(self, request):
        try:
            sample = request.data
            flattened_filled_array = transform_raw_line_data(sample["rawLineData"])
            best_guess = guess(flattened_filled_array)
            num_samples = SampleData.objects.all().count()
            return Response({"best_guess": best_guess, "num_samples": num_samples})
        except:
            return Response({"best_guess": "NONE"})
   
       
class Sample(APIView):

    def get(self, request, format=None):
        data = SampleData.objects.all()
        serialized_data = SampleDataSerializer(data, many=True)        
        return Response({"all_data": serialized_data.data})
    
    def post(self, request):
        sample = request.data
        sample["data"] = transform_raw_line_data(sample["rawLineData"])
        serializer = SampleDataSerializer(data=sample)
        if serializer.is_valid(raise_exception=True):
            sample_saved = serializer.save()
        return Response({"result": f"{sample_saved.category} saved"})


class UpdateModel(APIView):

    def post(self, request):
        all_samples = SampleData.objects.all()
        prepared_db_samples_for_training = prepare_db_samples_for_training(all_samples)
        score = train(prepared_db_samples_for_training)
        return Response({"score": score})