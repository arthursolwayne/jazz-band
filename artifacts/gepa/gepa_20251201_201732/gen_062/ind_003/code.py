
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Create instruments
drums = Instrument(program=10, is_drum=True, name='Drums')
bass = Instrument(program=33, name='Bass')
piano = Instrument(program=0, name='Piano')
sax = Instrument(program=64, name='Saxophone')

# Add instruments to the PrettyMIDI object
pm.instruments = [drums, bass, piano, sax]

# Define the key: Dm (D Dorian)
# Notes in D Dorian: D, E, F, G, A, B, C
# Chord progression: Dm7 -> G7 -> Cm7 -> F7 (but we're only using 4 bars, so maybe Dm7 -> G7 -> Cm7 -> F7 or just Dm7 for 4 bars)

# Define time per bar in seconds (160 BPM = 60/160 = 0.375 seconds per beat)
beats_per_bar = 4
beat_duration = 0.375
bar_duration = beat_duration * beats_per_bar

# Define timing for each bar
bar_times = [0.0, bar_duration, bar_duration * 2, bar_duration * 3]

# ------------------------ DRUMS (Little Ray) ------------------------
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0]:
    start = bar_times[bar]
    kick_notes = [Note(60, start, start + 0.1), Note(60, start + beat_duration * 2, start + beat_duration * 2 + 0.1)]
    snare_notes = [Note(62, start + beat_duration, start + beat_duration + 0.1), Note(62, start + beat_duration * 3, start + beat_duration * 3 + 0.1)]
    hihat_notes = []
    for i in range(8):
        hihat_notes.append(Note(42, start + beat_duration * i / 2, start + beat_duration * i / 2 + 0.05))
    for note in kick_notes + snare_notes + hihat_notes:
        drums.notes.append(note)

# Bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [1, 2, 3]:
    start = bar_times[bar]
    kick_notes = [Note(60, start, start + 0.1), Note(60, start + beat_duration * 2, start + beat_duration * 2 + 0.1)]
    snare_notes = [Note(62, start + beat_duration, start + beat_duration + 0.1), Note(62, start + beat_duration * 3, start + beat_duration * 3 + 0.1)]
    hihat_notes = []
    for i in range(8):
        hihat_notes.append(Note(42, start + beat_duration * i / 2, start + beat_duration * i / 2 + 0.05))
    for note in kick_notes + snare_notes + hihat_notes:
        drums.notes.append(note)

# ------------------------ BASS (Marcus) ------------------------
# Walking line: D2 (D), F2 (F), G2 (G), A2 (A), B2 (B), C3 (C), D3 (D), E3 (E), etc.
# We'll use roots and fifths with chromatic approaches

# Bar 1: Dm7 — Root D, 5th A, chromatic approach on the downbeat
# Bar 2: G7 — Root G, 5th D, chromatic approach
# Bar 3: Cm7 — Root C, 5th G, chromatic approach
# Bar 4: F7 — Root F, 5th C, chromatic approach

# Bar 1: D2 (D), D#2 (chromatic), A2 (5th), A2 (hold)
bass_notes = [
    Note(38, 0.0, 0.1),  # D2
    Note(40, 0.0, 0.1),  # D#2 (chromatic)
    Note(43, 0.1, 0.1),  # A2
    Note(43, 0.1, 0.1),  # A2 (hold)
]

# Bar 2: G2 (G), G#2 (chromatic), D3 (5th), D3 (hold)
bass_notes.extend([
    Note(47, bar_duration, 0.1),  # G2
    Note(49, bar_duration, 0.1),  # G#2
    Note(50, bar_duration + 0.1, 0.1),  # D3
    Note(50, bar_duration + 0.1, 0.1),  # D3
])

# Bar 3: C2 (C), C#2 (chromatic), G2 (5th), G2 (hold)
bass_notes.extend([
    Note(36, bar_duration * 2, 0.1),  # C2
    Note(38, bar_duration * 2, 0.1),  # C#2
    Note(43, bar_duration * 2 + 0.1, 0.1),  # G2
    Note(43, bar_duration * 2 + 0.1, 0.1),  # G2
])

# Bar 4: F2 (F), F#2 (chromatic), C3 (5th), C3 (hold)
bass_notes.extend([
    Note(41, bar_duration * 3, 0.1),  # F2
    Note(43, bar_duration * 3, 0.1),  # F#2
    Note(52, bar_duration * 3 + 0.1, 0.1),  # C3
    Note(52, bar_duration * 3 + 0.1, 0.1),  # C3
])

for note in bass_notes:
    bass.notes.append(note)

# ------------------------ PIANO (Diane) ------------------------
# Open voicings, different chord each bar, resolve on the last
# Bar 1: Dm7 (D, F, A, C)
# Bar 2: G7 (G, B, D, F)
# Bar 3: Cm7 (C, Eb, G, Bb)
# Bar 4: F7 (F, A, C, Eb)

# Bar 1: Dm7 (D, F, A, C)
piano_notes = [
    Note(62, 0.0, 0.1),  # D4
    Note(64, 0.0, 0.1),  # F4
    Note(67, 0.0, 0.1),  # A4
    Note(67, 0.0, 0.1),  # C5 (semi-resolved)
]

# Bar 2: G7 (G, B, D, F)
piano_notes.extend([
    Note(67, bar_duration, 0.1),  # G4
    Note(71, bar_duration, 0.1),  # B4
    Note(69, bar_duration, 0.1),  # D5
    Note(64, bar_duration, 0.1),  # F5
])

# Bar 3: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    Note(60, bar_duration * 2, 0.1),  # C4
    Note(63, bar_duration * 2, 0.1),  # Eb4
    Note(67, bar_duration * 2, 0.1),  # G4
    Note(62, bar_duration * 2, 0.1),  # Bb4
])

# Bar 4: F7 (F, A, C, Eb)
piano_notes.extend([
    Note(65, bar_duration * 3, 0.1),  # F4
    Note(69, bar_duration * 3, 0.1),  # A4
    Note(67, bar_duration * 3, 0.1),  # C5
    Note(63, bar_duration * 3, 0.1),  # Eb5
])

for note in piano_notes:
    piano.notes.append(note)

# ------------------------ SAX (You) ------------------------
# One short motif: D, F, G, A — but leave it hanging. Start it, let it breathe, come back.

# Bar 1: D (D4) at start, let it ring a little
sax_notes = [
    Note(62, 0.0, 0.3),  # D4
]

# Bar 2: F (F4) at start
sax_notes.append(Note(64, bar_duration, 0.3))

# Bar 3: G (G4) at start, leave it hanging
sax_notes.append(Note(67, bar_duration * 2, 0.3))

# Bar 4: A (A4) at start, resolve slightly
sax_notes.append(Note(69, bar_duration * 3, 0.3))

for note in sax_notes:
    sax.notes.append(note)

# Write the MIDI file
pm.write('dante_introduction.mid')

print("MIDI file 'dante_introduction.mid' has been created.")
