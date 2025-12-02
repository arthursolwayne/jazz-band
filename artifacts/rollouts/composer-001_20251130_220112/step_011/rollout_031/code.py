
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

# Bass line: Marcus
# Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=73, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=75, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),   # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane
# 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=85, pitch=77, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=79, start=1.875, end=2.25),  # D
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=72, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=85, pitch=77, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75),  # D
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=72, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=85, pitch=77, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante
# Short motif - start it, leave it hanging, come back and finish it
# Motif: F - Bb - F# (with some space)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=77, start=1.75, end=1.875),  # F#
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=77, start=3.25, end=3.375),  # F#
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
