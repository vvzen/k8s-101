update-cm:
	kubectl create configmap static-files-cm --dry-run=client --from-file=html -o yaml | kubectl apply -f -
