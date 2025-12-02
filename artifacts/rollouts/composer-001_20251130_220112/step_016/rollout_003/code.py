
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
# Fm = F, Ab, Bb, Db
# Bass line: F, Gb, Ab, A, Bb, B, Db, C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # Db
    pretty_midi.Note(velocity=90, pitch=63, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # Db
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),  # Gb
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, comping
# Fm7 = F, Ab, Bb, C
# Bb7 = Bb, Db, F, Ab
# Fm7 again on 4
piano_notes = [
    # Bar 2, measure 2: Bb7
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=73, start=2.0, end=2.25),  # Db
    pretty_midi.Note(velocity=80, pitch=76, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=77, start=2.0, end=2.25),  # Ab

    # Bar 3, measure 2: Fm7
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.25),  # C

    # Bar 4, measure 2: Bb7
    pretty_midi.Note(velocity=80, pitch=71, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=73, start=4.0, end=4.25),  # Db
    pretty_midi.Note(velocity=80, pitch=76, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=77, start=4.0, end=4.25),  # Ab

    # Bar 4, measure 4: Fm7
    pretty_midi.Note(velocity=80, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=5.0, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Saxophone - short motif, make it sing
# Fm scale: F, Gb, Ab, A, Bb, B, Db, C
# Motif: F, Gb, Ab, A
# Repeat on bar 3 with a half-step descent: F, Eb, Db, C

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5),  # A
]

# Bar 3
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # Db
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.0),  # C
]

# Bar 4
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.5),  # A

    # Leave it hanging, don't resolve
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_intro.mid")
