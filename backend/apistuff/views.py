from rest_framework.views import APIView
from rest_framework.response import Response
from .processor import guess
from .sample import add_sample, prepare
from .models import SampleData
from .serializers import SampleDataSerializer
from .training import train

class Process(APIView):

    def get(self, request, format=None):
        resp = "Process endpoint"
        return Response(resp)
    
    def post(self, request):
        prepared = prepare([x for y in request.data["data"] for x in y])#prepare(request.data["data"])
        best_guess = guess(prepared)
        return Response({"best_guess": best_guess})
   
       
class Sample(APIView):

    def get(self, request, format=None):
        data = SampleData.objects.all()
        serialized_data = SampleDataSerializer(data, many=True)        
        return Response({"all_data": serialized_data.data})
    
    def post(self, request):
        sample = request.data
        sample["data"] = [x for y in sample["data"] for x in y] # remove dimension for consistency
        serializer = SampleDataSerializer(data=sample)
        if serializer.is_valid(raise_exception=True):
            sample_saved = serializer.save()
        return Response({"result": f"{sample_saved.category} saved"})


class UpdateModel(APIView):

    def get(self, request):
        all_samples = SampleData.objects.all()
        resp = [add_sample(s.data, s.category) for s in all_samples] 
        return Response({"update": resp})

    def post(self, request):
        # pull in all the data, transform it, train model, save model
        all_samples = SampleData.objects.all()
        samples = [add_sample(s.data, s.category) for s in all_samples] 
        # use samples to retrain a model
        score = train(samples)
        # returns the accuracy of the model (if it's not high enough, you can retrain)
        return Response({"score": score})