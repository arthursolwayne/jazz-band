
import pretty_midi
from pretty_midi import Note, Instrument, MidiFile

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define the key: F major
key = 'F'

# Time per bar (in seconds)
bar_duration = 1.5  # 6 seconds for 4 bars
beat_duration = 0.375  # 60 / 160 = 0.375s per beat

# Define the bar boundaries in seconds
bar_times = [0, 1.5, 3.0, 4.5, 6.0]

# Define instruments
drums = Instrument(program=10, is_drum=True, name='Drums')
bass = Instrument(program=33, name='Bass')
piano = Instrument(program=0, name='Piano')
sax = Instrument(program=64, name='Saxophone')

pm.instruments = [drums, bass, piano, sax]

# --- DRUMS: Little Ray (Bar 1 only, fill) ---
# Kick on beat 1 and 3
drum_notes = [
    Note(36, 0, bar_times[0], bar_times[0] + 0.1),  # Kick on beat 1
    Note(36, 0, bar_times[0] + 0.75, bar_times[0] + 0.85),  # Kick on beat 3
    Note(38, 0, bar_times[0], bar_times[0] + 0.2),  # Snare on beat 2
    Note(38, 0, bar_times[0] + 0.5, bar_times[0] + 0.6),  # Snare on beat 4
    Note(42, 0, bar_times[0], bar_times[0] + 0.1),  # Hihat on beat 1
    Note(42, 0, bar_times[0] + 0.25, bar_times[0] + 0.35),  # Hihat on beat 2
    Note(42, 0, bar_times[0] + 0.5, bar_times[0] + 0.6),  # Hihat on beat 3
    Note(42, 0, bar_times[0] + 0.75, bar_times[0] + 0.85),  # Hihat on beat 4
]
for note in drum_notes:
    drums.notes.append(note)

# --- BASS: Marcus (Walking line with chromatic approaches over all 4 bars) ---
# F major scale: F G A Bb C D E
# Bass line in walking style with chromatic approach notes
# Root on beat 1, fifth on beat 3, chromatic approach on beat 2 and 4

# Define the bass line (F, G, A, Bb, C, D, E)
bass_notes = []
# Bar 1: F (root), G (fifth), Gb (chromatic), F (root)
bass_notes += [
    Note(70, 0, bar_times[0], bar_times[0] + 0.25),  # F
    Note(71, 0, bar_times[0] + 0.375, bar_times[0] + 0.625),  # G
    Note(70, 0, bar_times[0] + 0.75, bar_times[0] + 0.875),  # Gb
    Note(70, 0, bar_times[0] + 1.125, bar_times[0] + 1.375),  # F
]

# Bar 2: C (root), D (fifth), D# (chromatic), C (root)
bass_notes += [
    Note(72, 0, bar_times[1], bar_times[1] + 0.25),  # C
    Note(73, 0, bar_times[1] + 0.375, bar_times[1] + 0.625),  # D
    Note(74, 0, bar_times[1] + 0.75, bar_times[1] + 0.875),  # D#
    Note(72, 0, bar_times[1] + 1.125, bar_times[1] + 1.375),  # C
]

# Bar 3: G (root), A (fifth), Ab (chromatic), G (root)
bass_notes += [
    Note(71, 0, bar_times[2], bar_times[2] + 0.25),  # G
    Note(72, 0, bar_times[2] + 0.375, bar_times[2] + 0.625),  # A
    Note(71, 0, bar_times[2] + 0.75, bar_times[2] + 0.875),  # Ab
    Note(71, 0, bar_times[2] + 1.125, bar_times[2] + 1.375),  # G
]

# Bar 4: C (root), D (fifth), D# (chromatic), C (root)
bass_notes += [
    Note(72, 0, bar_times[3], bar_times[3] + 0.25),  # C
    Note(73, 0, bar_times[3] + 0.375, bar_times[3] + 0.625),  # D
    Note(74, 0, bar_times[3] + 0.75, bar_times[3] + 0.875),  # D#
    Note(72, 0, bar_times[3] + 1.125, bar_times[3] + 1.375),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# --- PIANO: Diane (Open voicings, comp on 2 and 4) ---
# Bar 1: F7 (F, A, C, E) – comp on beat 2
piano_notes = [
    Note(69, 0, bar_times[0] + 0.375, bar_times[0] + 0.625),  # A
    Note(67, 0, bar_times[0] + 0.375, bar_times[0] + 0.625),  # C
    Note(64, 0, bar_times[0] + 0.375, bar_times[0] + 0.625),  # F
    Note(72, 0, bar_times[0] + 0.375, bar_times[0] + 0.625),  # E
]

# Bar 2: G7 (G, B, D, F) – comp on beat 4
piano_notes += [
    Note(71, 0, bar_times[1] + 0.75, bar_times[1] + 1.0),  # B
    Note(74, 0, bar_times[1] + 0.75, bar_times[1] + 1.0),  # D
    Note(69, 0, bar_times[1] + 0.75, bar_times[1] + 1.0),  # G
    Note(67, 0, bar_times[1] + 0.75, bar_times[1] + 1.0),  # F
]

# Bar 3: C7 (C, E, G, B) – comp on beat 2
piano_notes += [
    Note(72, 0, bar_times[2] + 0.375, bar_times[2] + 0.625),  # E
    Note(74, 0, bar_times[2] + 0.375, bar_times[2] + 0.625),  # G
    Note(76, 0, bar_times[2] + 0.375, bar_times[2] + 0.625),  # B
    Note(72, 0, bar_times[2] + 0.375, bar_times[2] + 0.625),  # C
]

# Bar 4: F7 (F, A, C, E) – comp on beat 4
piano_notes += [
    Note(69, 0, bar_times[3] + 0.75, bar_times[3] + 1.0),  # A
    Note(67, 0, bar_times[3] + 0.75, bar_times[3] + 1.0),  # C
    Note(64, 0, bar_times[3] + 0.75, bar_times[3] + 1.0),  # F
    Note(72, 0, bar_times[3] + 0.75, bar_times[3] + 1.0),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# --- SAX: Your Motif (Bar 2–4) ---
# You start the motif at bar 2, with a search, a question, notes that don't quite resolve
# F, A, D, E – the first four notes of the motif
# Play them in a way that feels incomplete, like the beginning of something

# Bar 2: Start the motif
sax_notes = [
    Note(72, 100, bar_times[1], bar_times[1] + 0.25),  # C
    Note(76, 100, bar_times[1] + 0.25, bar_times[1] + 0.5),  # E
    Note(77, 100, bar_times[1] + 0.5, bar_times[1] + 0.75),  # F#
    Note(79, 100, bar_times[1] + 0.75, bar_times[1] + 1.0),  # A
]

# Bar 3: Repeat the motif with slight variation
sax_notes += [
    Note(72, 100, bar_times[2], bar_times[2] + 0.25),  # C
    Note(76, 100, bar_times[2] + 0.25, bar_times[2] + 0.5),  # E
    Note(77, 100, bar_times[2] + 0.5, bar_times[2] + 0.75),  # F#
    Note(79, 100, bar_times[2] + 0.75, bar_times[2] + 1.0),  # A
]

# Bar 4: End the motif with a resolution
sax_notes += [
    Note(64, 100, bar_times[3], bar_times[3] + 0.25),  # F
    Note(72, 100, bar_times[3] + 0.25, bar_times[3] + 0.5),  # C
    Note(76, 100, bar_times[3] + 0.5, bar_times[3] + 0.75),  # E
    Note(79, 100, bar_times[3] + 0.75, bar_times[3] + 1.0),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Save the MIDI file
pm.write("jazz_intro_dante.mid")
