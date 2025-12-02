
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
kick1 = pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif: Dm7 -> F7 -> Bb7 -> Gm7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Bass line: chromatic walking line with tension
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),   # G#
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),   # D#
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=75, start=5.625, end=6.0),   # G#
]
bass.notes.extend(bass_notes)

# Piano chords: comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick2 = pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25)
hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)
hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625)
hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
kick3 = pretty_midi.Note(velocity=80, pitch=36, start=2.625, end=2.999)
snare3 = pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375)
hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375)
hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75)
hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125)
hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
kick4 = pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25)
hihat13 = pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25)
hihat14 = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625)
hihat15 = pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)

drums.notes.extend([kick2, snare2, hihat5, hihat6, hihat7, hihat8, kick3, snare3, hihat9, hihat10, hihat11, hihat12, kick4, snare4, hihat13, hihat14, hihat15])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
