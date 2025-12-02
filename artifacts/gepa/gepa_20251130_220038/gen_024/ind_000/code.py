
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=73, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=75, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=80, start=5.625, end=6.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Tenor sax - melody in bars 2-4
# Motif: D (62), F# (67), B (71), A (69), leave it hanging, return to finish
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),
    # End of motif, leave it hanging
    # Return to complete the phrase
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),
    # End phrase
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)

    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    hihat5 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875)
    hihat6 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25)
    hihat7 = pretty_midi.Note(velocity=90, pitch=42, start=start + 2.25, end=start + 2.625)
    hihat8 = pretty_midi.Note(velocity=90, pitch=42, start=start + 2.625, end=start + 3.0)

    drums.notes.extend([kick1, snare2, kick3, snare4, hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
