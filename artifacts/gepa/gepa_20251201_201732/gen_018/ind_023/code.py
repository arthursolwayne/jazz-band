
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4 (but cut off at end of bar)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane (Piano) - Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.75),  # E
]

# Marcus (Bass) - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),  # F#
]

# Dante (Sax) - Motif: F - Bb - D - F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # F
]

for note in piano_notes:
    piano.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane (Piano) - G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=75, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25),  # F
]

# Marcus (Bass) - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=78, start=4.125, end=4.5),  # G#
]

# Dante (Sax) - Motif: G - Bb - D - F (but with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # F
]

for note in piano_notes:
    piano.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane (Piano) - Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # Bb
]

# Marcus (Bass) - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=66, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=80, pitch=68, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # C#
]

# Dante (Sax) - Motif resolution: F - Bb - D - F with slight delay
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # F
]

for note in piano_notes:
    piano.notes.append(note)
for note in bass_notes:
    bass.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Bar 2: Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
for bar in [1.5, 3.0, 4.5]:
    for i in range(4):
        start = bar + i * 0.375
        if i == 0 or i == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
        elif i == 1 or i == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375))

# Save the MIDI file
midi.write("dante_intro.mid")
