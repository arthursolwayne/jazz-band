
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

drum_notes = [
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in. Sax melody
# Start with a short motif, leave it hanging

# D7 chord (D F# A C#)
# Diane: Open voicing, C#, A, F#, D
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375),  # C#
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),  # F#
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.5 + 0.375),  # D
]

# Marcus: Walking bass line in D (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.5 + 0.375),  # D2
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 0.375, end=1.5 + 0.75),  # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + 0.75, end=1.5 + 1.125),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=1.5 + 1.125, end=1.5 + 1.5),  # F#2 (chromatic approach)
]

# Sax: Motif starting on D5 (MIDI 72)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.5 + 0.375),  # D5
    pretty_midi.Note(velocity=110, pitch=76, start=1.5 + 0.375, end=1.5 + 0.75),  # G5
    pretty_midi.Note(velocity=110, pitch=74, start=1.5 + 0.75, end=1.5 + 1.125),  # F#5
    pretty_midi.Note(velocity=110, pitch=72, start=1.5 + 1.125, end=1.5 + 1.5),  # D5
]

# Bar 3: Same structure, but shift the melody up a whole step
# D7 -> E7, so piano voicing: D, B, G, E (MIDI 64, 69, 67, 72)
piano_notes_3 = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 1.5, end=1.5 + 1.875),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 1.5, end=1.5 + 1.875),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5, end=1.5 + 1.875),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 1.5, end=1.5 + 1.875),  # E
]

# Marcus: Walking line in E (E2-B2, MIDI 41-46)
bass_notes_3 = [
    pretty_midi.Note(velocity=100, pitch=41, start=1.5 + 1.5, end=1.5 + 1.875),  # E2
    pretty_midi.Note(velocity=100, pitch=46, start=1.5 + 1.875, end=1.5 + 2.25),  # B2
    pretty_midi.Note(velocity=100, pitch=45, start=1.5 + 2.25, end=1.5 + 2.625),  # A2
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 2.625, end=1.5 + 3.0),  # G2
]

# Sax: Motif shifted up a whole step
sax_notes_3 = [
    pretty_midi.Note(velocity=110, pitch=74, start=1.5 + 1.5, end=1.5 + 1.875),  # E5
    pretty_midi.Note(velocity=110, pitch=78, start=1.5 + 1.875, end=1.5 + 2.25),  # A5
    pretty_midi.Note(velocity=110, pitch=76, start=1.5 + 2.25, end=1.5 + 2.625),  # G5
    pretty_midi.Note(velocity=110, pitch=74, start=1.5 + 2.625, end=1.5 + 3.0),  # E5
]

# Bar 4: Resolve back to D7
# Diane: Open voicing, F#, A, D, C#
piano_notes_4 = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 3.0, end=1.5 + 3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 3.0, end=1.5 + 3.375),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=1.5 + 3.0, end=1.5 + 3.375),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 3.0, end=1.5 + 3.375),  # C#
]

# Marcus: Walking back to D (D2-G2)
bass_notes_4 = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + 3.0, end=1.5 + 3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=43, start=1.5 + 3.375, end=1.5 + 3.75),  # A2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5 + 3.75, end=1.5 + 4.125),  # G2
    pretty_midi.Note(velocity=100, pitch=40, start=1.5 + 4.125, end=1.5 + 4.5),  # F#2
]

# Sax: Resolve the motif back to D5
sax_notes_4 = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5 + 3.0, end=1.5 + 3.375),  # D5
    pretty_midi.Note(velocity=110, pitch=76, start=1.5 + 3.375, end=1.5 + 3.75),  # G5
    pretty_midi.Note(velocity=110, pitch=74, start=1.5 + 3.75, end=1.5 + 4.125),  # F#5
    pretty_midi.Note(velocity=110, pitch=72, start=1.5 + 4.125, end=1.5 + 4.5),  # D5
]

# Add notes to instruments
for note in piano_notes:
    piano.notes.append(note)
for note in piano_notes_3:
    piano.notes.append(note)
for note in piano_notes_4:
    piano.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)
for note in bass_notes_3:
    bass.notes.append(note)
for note in bass_notes_4:
    bass.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)
for note in sax_notes_3:
    sax.notes.append(note)
for note in sax_notes_4:
    sax.notes.append(note)

# Drums for bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for start in [1.5, 1.5 + 1.125]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
for start in [1.5 + 0.375, 1.5 + 1.5]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
for start in [1.5, 1.5 + 0.375, 1.5 + 0.75, 1.5 + 1.125, 1.5 + 1.5]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))

# Bar 3
for start in [1.5 + 1.5, 1.5 + 2.625]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
for start in [1.5 + 1.875, 1.5 + 3.0]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
for start in [1.5 + 1.5, 1.5 + 1.875, 1.5 + 2.25, 1.5 + 2.625, 1.5 + 3.0]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))

# Bar 4
for start in [1.5 + 3.0, 1.5 + 4.125]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
for start in [1.5 + 3.375, 1.5 + 4.5]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
for start in [1.5 + 3.0, 1.5 + 3.375, 1.5 + 3.75, 1.5 + 4.125, 1.5 + 4.5]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
