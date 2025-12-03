
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
# Walking bass line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root), E (chromatic approach), G (fifth), F (root)
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=73, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),
    # Bar 3: A (chromatic), Bb (root), D (fifth), A (chromatic)
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),
    # Bar 4: C (chromatic), D (fifth), F (root), C (chromatic)
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane
# Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G#, Bb, A (1.5 - 2.25s), then leave it hanging, come back on 3.0 - 3.375s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=73, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=73, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    snare = pretty_midi.Note(velocity=90, pitch=38, start=start_time + 0.75, end=start_time + 1.125)
    hihat = [
        pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=start_time + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.375, end=start_time + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.75, end=start_time + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.125, end=start_time + 1.5),
    ]
    return [kick, snare] + hihat

# Bar 2 (1.5 - 3.0)
for note in add_drums(1.5):
    drums.notes.append(note)

# Bar 3 (3.0 - 4.5)
for note in add_drums(3.0):
    drums.notes.append(note)

# Bar 4 (4.5 - 6.0)
for note in add_drums(4.5):
    drums.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
# midi.write disabled
