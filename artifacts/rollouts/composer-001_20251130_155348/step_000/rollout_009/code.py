
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Saxophone motif (F7, G7, Ab7, Bb7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.75),  # F7
    pretty_midi.Note(velocity=100, pitch=88, start=1.75, end=2.0),  # G7
    pretty_midi.Note(velocity=100, pitch=89, start=2.0, end=2.25),  # Ab7
    pretty_midi.Note(velocity=100, pitch=90, start=2.25, end=2.5),  # Bb7
    pretty_midi.Note(velocity=100, pitch=87, start=2.5, end=2.75),  # F7
    pretty_midi.Note(velocity=100, pitch=88, start=2.75, end=3.0),  # G7
]
sax.notes.extend(sax_notes)

# Bass line (walking line in F, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=49, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=3.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.75),  # F7
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=84, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),  # F7
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=82, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=84, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Bar 3: Everyone in (3.0 - 4.5s)
# Saxophone motif repeats with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=100, pitch=88, start=3.25, end=3.5),  # G7
    pretty_midi.Note(velocity=100, pitch=89, start=3.5, end=3.75),  # Ab7
    pretty_midi.Note(velocity=100, pitch=90, start=3.75, end=4.0),  # Bb7
    pretty_midi.Note(velocity=100, pitch=87, start=4.0, end=4.25),  # F7
    pretty_midi.Note(velocity=100, pitch=88, start=4.25, end=4.5),  # G7
]
sax.notes.extend(sax_notes)

# Bass line (walking line in F, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.25, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=84, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),  # F7
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=84, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Everyone in (4.5 - 6.0s)
# Saxophone motif resolves and ends on Bb7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=100, pitch=88, start=4.75, end=5.0),  # G7
    pretty_midi.Note(velocity=100, pitch=89, start=5.0, end=5.25),  # Ab7
    pretty_midi.Note(velocity=100, pitch=90, start=5.25, end=5.5),  # Bb7
    pretty_midi.Note(velocity=100, pitch=90, start=5.5, end=5.75),  # Bb7
    pretty_midi.Note(velocity=100, pitch=90, start=5.75, end=6.0),  # Bb7
]
sax.notes.extend(sax_notes)

# Bass line resolves to Bb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=90, pitch=51, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=52, start=5.75, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano resolves to Bb7 on the last two beats
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.5),  # F7
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=82, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=84, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=76, start=5.5, end=5.75),  # F7
    pretty_midi.Note(velocity=90, pitch=79, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=82, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=84, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=89, start=5.75, end=6.0),  # Bb7
    pretty_midi.Note(velocity=90, pitch=92, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=96, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=98, start=5.75, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
