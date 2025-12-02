
import pretty_midi

# Create a PrettyMIDI object with 160 BPM (4/4 time)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: Dm (D minor)
key = 'D minor'

# Define the instruments
# Tenor Sax (program 64)
tenor_sax = pretty_midi.Instrument(program=64)
pm.instruments.append(tenor_sax)

# Bass (program 33)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# Piano (program 0)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# Drums (program 128)
drums = pretty_midi.Instrument(program=128)
pm.instruments.append(drums)

# ---------------------------- DRUMS ----------------------------
# Bar 1: Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds per bar
beat_length = 0.375  # seconds per beat

# Bar 1: 0.0 to 1.5 seconds
# Kick on 1 (0.0) and 3 (0.75)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.05))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.8))

# Snare on 2 (0.375) and 4 (1.125)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.425))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.175))

# Hihat on every eighth (0.0, 0.375, 0.75, 1.125)
for t in [0.0, 0.375, 0.75, 1.125]:
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05))

# ---------------------------- BASS ----------------------------
# Marcus: Walking line, chromatic approaches, never the same note twice
# Bar 1: Open (no bass)
# Bar 2: Dm7 walking line, chromatic approaches
# Bar 3: Chromatic run up to D
# Bar 4: Chromatic run down from D

# Bar 2 (1.5 to 3.0 seconds)
# Dm7 chord: D F A C
# Walking line: D F# E F G A Bb C D
# Notes in MIDI: D (62), F# (66), E (64), F (65), G (67), A (69), Bb (67?), C (60), D (62)

# Walking line: D F# E F G A Bb C D
notes = [62, 66, 64, 65, 67, 69, 67, 60, 62]
positions = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5]
for i, note in enumerate(notes):
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=positions[i], end=positions[i] + 0.25))

# Bar 3 (3.0 to 4.5 seconds): Chromatic run up to D (62)
notes = [60, 61, 62]  # C, C#, D (chromatic up)
positions = [3.0, 3.375, 3.75]
for i, note in enumerate(notes):
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=positions[i], end=positions[i] + 0.25))

# Bar 4 (4.5 to 6.0 seconds): Chromatic run down from D (62)
notes = [62, 61, 60]  # D, C#, C (chromatic down)
positions = [4.5, 4.875, 5.25]
for i, note in enumerate(notes):
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=positions[i], end=positions[i] + 0.25))

# ---------------------------- PIANO ----------------------------
# Diane: 7th chords, comp on 2 and 4
# Bar 1: No piano
# Bar 2: Dm7 (D F A C) on 2 and 4
# Bar 3: Dm7 on 2 and 4
# Bar 4: Dm7 on 2 and 4

# Chord: Dm7 = D (62), F (65), A (69), C (60)

def add_chord_notes(chord, time):
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Bar 2: 1.5 to 3.0 seconds
add_chord_notes([62, 65, 69, 60], 1.875)
add_chord_notes([62, 65, 69, 60], 3.0)

# Bar 3: 3.0 to 4.5 seconds
add_chord_notes([62, 65, 69, 60], 3.375)
add_chord_notes([62, 65, 69, 60], 4.5)

# Bar 4: 4.5 to 6.0 seconds
add_chord_notes([62, 65, 69, 60], 4.875)
add_chord_notes([62, 65, 69, 60], 6.0)

# ---------------------------- TENOR SAX ----------------------------
# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 1: No sax
# Bar 2: Start motif
# Bar 3: Continue motif
# Bar 4: Resolve motif

# Motif: D (62), E (64), D (62), F# (66) — then leave it hanging
# Let it rest at D (62) and resolve in bar 4

# Bar 2 (1.5 to 3.0)
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6))
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.6, end=1.7))
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.7, end=1.8))
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.8, end=1.9))

# Bar 3 (3.0 to 4.5): Let it hang — D (62) at the end of the bar
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1))

# Bar 4 (4.5 to 6.0): Resolve back to D (62)
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6))
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.6, end=4.7))
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.7, end=4.8))
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=4.8, end=4.9))

# Save the MIDI file
pm.write("dante_russo_intro.mid")
