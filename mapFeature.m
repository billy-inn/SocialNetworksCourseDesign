function out = mapFeature(X, degree)

out = ones(size(X(:,1)));

for i = 1:degree
	for j = 0:i
		for k= 0:j
			for l = 0:k
				t1 = X(:,1).^(i-j);
				t2 = X(:,2).^(j-k);
				t3 = X(:,3).^(k-l);
				t4 = X(:,4).^l;
				out(:,end+1) = t1.*t2.*t3.*t4;
			end
		end
	end
end

end
