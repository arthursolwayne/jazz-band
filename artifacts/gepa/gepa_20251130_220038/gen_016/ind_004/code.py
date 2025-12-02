
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F
bass_notes = [
    # F (1st beat)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    # G (2nd beat)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    # Ab (3rd beat)
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625),
    # A (4th beat)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    # Bb (1st beat)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    # C (2nd beat)
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),
    # D (3rd beat)
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),
    # Eb (4th beat)
    pretty_midi.Note(velocity=90, pitch=73, start=4.125, end=4.5),
    # F (1st beat)
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),
    # G (2nd beat)
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    # Ab (3rd beat)
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),
    # A (4th beat)
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, F7 and Bb7
# Bar 2: F7 on beat 2
piano_notes = [
    # F7 = F, A, C, Eb
    pretty_midi.Note(velocity=95, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=73, start=1.875, end=2.25),
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.75),
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax - short motif, start it, leave it hanging, come back and finish it
# Motif: F - Ab - Bb - F (open fifth)
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=105, pitch=68, start=1.75, end=2.0),
    pretty_midi.Note(velocity=105, pitch=71, start=2.0, end=2.25),
    # Leave it hanging - no note on beat 3
    pretty_midi.Note(velocity=105, pitch=65, start=2.625, end=2.875),
    pretty_midi.Note(velocity=105, pitch=68, start=2.875, end=3.125),
    pretty_midi.Note(velocity=105, pitch=71, start=3.125, end=3.375),
    pretty_midi.Note(velocity=105, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=105, pitch=68, start=4.0, end=4.25),
    pretty_midi.Note(velocity=105, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=105, pitch=65, start=4.875, end=5.125),
    pretty_midi.Note(velocity=105, pitch=68, start=5.125, end=5.375),
    pretty_midi.Note(velocity=105, pitch=71, start=5.375, end=5.625),
    pretty_midi.Note(velocity=105, pitch=65, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
