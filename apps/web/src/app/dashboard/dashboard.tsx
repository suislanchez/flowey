"use client";
import { Button } from "@/components/ui/button";
import { authClient } from "@/lib/auth-client";
import { useQuery } from "@tanstack/react-query";
import { trpc } from "@/utils/trpc";

export default function Dashboard({
	session,
}: {
	session: typeof authClient.$Infer.Session;
}) {
	const privateData = useQuery({
		queryKey: ["privateData"],
		queryFn: async () => {
			const res = await fetch(`${process.env.NEXT_PUBLIC_SERVER_URL}/trpc/privateData`, {
				credentials: "include",
				headers: { "content-type": "application/json" },
			});
			if (!res.ok) throw new Error("Failed to fetch private data");
			const json = await res.json();
			return json?.result?.data ?? null;
		},
	});

	return (
		<>
			<p>API: {privateData.data?.message}</p>
		</>
	);
}
