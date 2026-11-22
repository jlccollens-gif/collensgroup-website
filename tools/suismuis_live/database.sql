-- Suismuis Home: database voor bestellingen, berichten en de bestelbalie.
-- Plak dit in Supabase > SQL Editor en klik op Run.
create table if not exists public.suismuis_orders (
  id bigint generated always as identity primary key,
  nr text not null unique,
  created_at timestamptz not null default now(),
  test boolean not null default false,
  status text not null default 'open' check (status in ('open','wacht_op_betaling','betaald','besteld','verzonden','geleverd','geannuleerd','terugbetaald')),
  klant_naam text not null, klant_email text not null, klant_tel text,
  adres jsonb not null, regels jsonb not null,
  subtotaal numeric(10,2) not null, verzending numeric(10,2) not null, cadeau numeric(10,2) not null default 0, totaal numeric(10,2) not null,
  betaalmethode text, paypal_order_id text, paypal_capture_id text, betaald_op timestamptz,
  status_token_hash text not null, site text,
  leverancier_ordernr text, vervoerder text, track_trace text, notitie text,
  mails jsonb not null default '[]'::jsonb,
  log jsonb not null default '[]'::jsonb
);
create index if not exists suismuis_orders_created on public.suismuis_orders (created_at desc);
create index if not exists suismuis_orders_paypal on public.suismuis_orders (paypal_order_id);
create table if not exists public.suismuis_berichten (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  soort text not null check (soort in ('contact','herroeping','nieuwsbrief','maatprijs')),
  naam text, email text not null, velden jsonb not null default '{}'::jsonb,
  afgehandeld boolean not null default false
);
create table if not exists public.suismuis_beheer (
  id int primary key default 1 check (id = 1),
  wachtwoord_hash text, setup_token_hash text, setup_verloopt timestamptz
);
insert into public.suismuis_beheer (id) values (1) on conflict do nothing;
create table if not exists public.suismuis_sessies (token_hash text primary key, verloopt timestamptz not null);
-- Alleen de server-functie mag erbij (geen openbare toegang):
alter table public.suismuis_orders enable row level security;
alter table public.suismuis_berichten enable row level security;
alter table public.suismuis_beheer enable row level security;
alter table public.suismuis_sessies enable row level security;
